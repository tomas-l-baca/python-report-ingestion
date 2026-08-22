# Lesson 7: Google Drive OAuth Authentication and Token Persistence

## Objective

Establish authenticated Google Drive access for the standalone Python report-ingestion application using OAuth 2.0, while keeping all authentication material out of GitHub and maintaining a strict boundary between development testing and the active production email/report workflow.

The lesson began from the MacBook environment completed in Lesson 6.

The intended stopping point was authentication itself. No Google Drive file operation, production Gmail access, real operational email processing, or production report download was to be implemented during this lesson.

## What Was Completed

- Resumed development from the MacBook configured during Lesson 6.
- Activated the MacBook project's `.venv`.
- Verified the existing Python project structure before adding authentication.
- Created a Google OAuth Desktop client named:
  - `Python Report Ingestion Desktop`
- Located and downloaded the OAuth credential JSON despite a mismatch between Google's documentation and the current Google Cloud interface.
- Renamed the local OAuth credential file:
  - `credentials.json`
- Moved `credentials.json` into the repository root.
- Verified that `credentials.json` was excluded from Git by the existing `.gitignore`.
- Identified macOS Finder's generated `.DS_Store` file.
- Added `.DS_Store` to `.gitignore`.
- Committed, pushed, and publicly verified the `.DS_Store` ignore rule.
- Reviewed the existing `src` project structure before adding authentication code.
- Created:
  - `src/ingestion/google_auth.py`
- Added Google OAuth flow creation.
- Added Google Drive authorization scope configuration.
- Added browser-based OAuth authentication.
- Added the personal development Google account as an OAuth test user.
- Successfully completed Google's OAuth authorization flow.
- Added local `token.json` persistence.
- Added support for loading previously authorized credentials.
- Added credential-refresh logic.
- Verified that subsequent authentication reused `token.json` without reopening the browser.
- Verified that both `credentials.json` and `token.json` remained excluded from Git.
- Committed, pushed, and publicly verified `google_auth.py`.

## What Was Tested and Verified

### Repository State at Lesson Start

The MacBook repository was synchronized and the project virtual environment was activated.

The macOS/Linux activation command was:

```bash
source .venv/bin/activate
```

The active environment was confirmed by:

```text
(.venv)
```

### OAuth Credential Git Protection

After `credentials.json` was moved into the repository root, the following command was run:

```bash
git status
```

Git did not list:

```text
credentials.json
```

This verified that the credential file was protected by `.gitignore`.

### `.DS_Store` Protection

Git initially reported:

```text
.DS_Store
```

as an untracked file.

The following rule was added to `.gitignore`:

```text
.DS_Store
```

A subsequent `git status` showed only the intentional `.gitignore` modification.

The `.gitignore` update was staged, committed, pushed, and publicly verified.

Commit message:

```text
Ignore macOS Finder metadata
```

### Existing Python Structure

Before adding OAuth code, the existing project structure was inspected:

```text
src/
├── ingestion/
│   ├── __pycache__/
│   ├── file_naming.py
│   └── message_parser.py
└── main.py
```

The current `main.py` still used simulated test data:

```python
subject = "UbiVu | City of Santa Fe New Mexico | Santa Fe Nodes"
body = '<a href="https://reports.example.com/sample-report.csv">Download</a>'
```

This verified that the active production email system was not being accessed.

### OAuth Flow Object

The first direct import test failed with:

```text
ModuleNotFoundError: No module named 'ingestion'
```

The corrected macOS/Linux command was:

```bash
PYTHONPATH=src python -c "from ingestion.google_auth import create_auth_flow; flow = create_auth_flow(); print(type(flow).__name__)"
```

Output:

```text
InstalledAppFlow
```

This verified that:

- Python could locate the `ingestion` package when `src` was included in the module search path.
- `google_auth.py` imported successfully.
- `credentials.json` could be read.
- Google could construct the installed-application OAuth flow.

### Python Syntax and Indentation

After indentation problems occurred during editing, the module was repeatedly checked using:

```bash
PYTHONPATH=src python -m py_compile src/ingestion/google_auth.py
```

Successful checks produced no output.

This verified Python syntax and indentation without running OAuth.

### First Google Authorization Attempt

The browser authentication command was:

```bash
PYTHONPATH=src python -c "from ingestion.google_auth import authenticate; creds = authenticate(); print(type(creds).__name__)"
```

Google initially returned:

```text
403 access_denied
```

The OAuth application was in Testing mode and the personal Google account had not yet been added under Test users.

The development account was added under:

```text
Google Auth Platform
→ Audience
→ Test users
```

### Successful OAuth Authorization

After the account was added as an authorized test user, the authentication command was run again.

Google displayed explicit Drive-permission warnings.

After authorization was approved, Google reported:

```text
The authentication flow has completed. You may close this window.
```

The VS Code Terminal printed:

```text
Credentials
```

This verified successful end-to-end OAuth authorization.

### Token Persistence

After token-writing logic was added, authentication was run again.

Python created:

```text
token.json
```

The same authentication command was then executed a second time.

The browser remained closed and the terminal printed:

```text
Credentials
```

This verified that the saved authorization token was being loaded and reused successfully.

### Final Git Safety Check

After `token.json` existed, the following command was run:

```bash
git status
```

Git listed only:

```text
src/ingestion/google_auth.py
```

Neither:

```text
credentials.json
```

nor:

```text
token.json
```

appeared.

This verified that sensitive authentication material remained outside Git.

### Authentication Module Publication

The authentication module was staged:

```bash
git add src/ingestion/google_auth.py
```

It was committed with:

```text
Add Google Drive OAuth authentication
```

The commit was pushed to GitHub.

The repository returned to:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

The file and commit were manually verified on GitHub.

## New Python Concepts Learned

### `PYTHONPATH`

The prefix:

```bash
PYTHONPATH=src
```

temporarily adds the project's `src` directory to Python's module search path.

This allowed:

```python
from ingestion.google_auth import ...
```

to work when Python was launched from the repository root.

### `None`

The authentication function initializes:

```python
creds = None
```

`None` represents the absence of an assigned credentials object.

The variable later receives loaded, refreshed, or newly authorized Google credentials.

### Conditional Logic

The completed authentication flow introduced nested conditional logic:

```python
if os.path.exists("token.json"):
```

checks whether stored authorization exists.

```python
if not creds or not creds.valid:
```

checks whether usable credentials are available.

```python
if creds and creds.expired and creds.refresh_token:
```

checks whether expired credentials can be refreshed.

### `else`

If credentials cannot be reused or refreshed, the `else` branch starts a new browser-based authorization flow.

### File Existence Checks

The module uses:

```python
os.path.exists("token.json")
```

to determine whether previously stored credentials exist.

### File Writing

Token persistence introduced:

```python
with open("token.json", "w") as token:
    token.write(creds.to_json())
```

This introduced:

- `with`
- `open()`
- write mode `"w"`
- file handles
- writing text to disk
- JSON serialization

### Logical Indentation

Python indentation was shown to be part of program syntax rather than only visual formatting.

The lesson adopted the term:

```text
logical indentation level
```

to describe actual nested Python blocks.

### Continuation Indentation

Lines inside a multi-line function call may be visually farther to the right without creating another logical Python block.

This was identified as:

```text
continuation indentation
```

### `py_compile`

The command:

```bash
python -m py_compile
```

was introduced as a way to validate Python syntax without executing the application logic.

## New Git and GitHub Concepts Learned

### Platform-Generated Files Can Affect Repository State

macOS Finder created:

```text
.DS_Store
```

inside the repository.

Git correctly identified it as an untracked file until it was explicitly ignored.

This demonstrated that operating-system behavior can create files that must be considered when maintaining a cross-platform repository.

### Secret Exclusion Must Be Verified After Files Exist

Lesson 5 added:

```text
credentials.json
token.json
```

to `.gitignore` before either file existed.

Lesson 7 verified those protections with the real files present.

This demonstrated the difference between defining a security control and later proving that the control works.

### Source Files and Local Authentication State Are Separate

`google_auth.py` was appropriate repository source code.

`credentials.json` and `token.json` were local authentication state and were intentionally excluded.

### Public Verification Remains a Separate Step

A successful `git push` was not treated as the final proof.

The source file and commit were manually checked on GitHub after pushing.

## Google Cloud and OAuth Concepts Learned

### OAuth Desktop Client

The Python application uses an OAuth client of type:

```text
Desktop app
```

This type is appropriate for an application running locally rather than as a hosted web application.

### OAuth Client ID Versus Authorization

The OAuth Client ID identifies the application.

It does not by itself grant access to Google Drive.

Actual Drive access requires user authorization.

### OAuth Scope

The application requested:

```python
SCOPES = ["https://www.googleapis.com/auth/drive"]
```

Google correctly warned that this scope permits broad Drive access.

### OAuth Testing Mode

The application remained in Testing mode.

Only explicitly approved Test users could authorize the application.

### OAuth Test Users

The selected personal Google account was added as a development Test user.

This allowed controlled OAuth testing without publishing the application.

### Access Credentials and Refresh Capability

The returned Google `Credentials` object represents the application's authorized access.

Stored credentials can later be reused and, when possible, refreshed without requiring another interactive browser authorization.

### Token Persistence

`token.json` stores reusable authorization state locally.

It is not application source code and must not be committed publicly.

## macOS/Linux Concepts Learned

### Finder and Repository Files

macOS Finder can create `.DS_Store` metadata files inside directories being viewed.

That behavior became relevant once Finder was used to move OAuth credentials into the project.

### Command+C Versus Control+C

During the failed OAuth attempt, the Python process remained active.

On macOS:

```text
Command+C
    Copies text.

Control+C
    Interrupts the running terminal process.
```

Using `Control+C` correctly stopped the waiting Python process.

### macOS/Linux Environment Variable Syntax

The command:

```bash
PYTHONPATH=src python ...
```

uses a macOS/Linux shell convention in which an environment variable can be set for one command by placing it before the command.

## Meaningful Questions Raised

### Does the OAuth Client ID need to be stored somewhere secret?

This clarified that the Client ID identifies the application but does not independently grant Google Drive access.

The credential secret and authorization token require stronger protection.

### Are we faking the incoming email or accessing the active system email and previously used report links?

This question forced an explicit production-versus-development boundary review.

The email data remained simulated.

No production mailbox or operational download link was touched.

### Which Google account should be added as the Test user?

The account intentionally selected for development Google Drive testing.

A personal Google account was used.

### Why could Python not find `ingestion`?

Because the application package was under `src`, but that directory was not automatically part of the module search path for the one-line command.

### Why did the copied Python code produce an `IndentationError`?

Because the pasted function body did not preserve the required logical indentation.

### Is there terminology for first, second, and third indentation levels?

Yes.

The term `logical indentation level` was adopted to describe actual Python block nesting.

### Why are visually farther-indented lines sometimes called continuation indentation instead of another logical level?

Because they remain part of the same statement inside parentheses rather than defining another nested Python block.

### Can copied code be trusted to land correctly in VS Code?

No.

VS Code attempted to modify pasted indentation based on context.

The resulting Python structure must be inspected and validated.

### How can the code be checked without repeatedly launching OAuth?

Using:

```bash
PYTHONPATH=src python -m py_compile src/ingestion/google_auth.py
```

### Why did Google deny access with `403 access_denied`?

Because the application was in Testing mode and the selected account had not yet been added as a Test user.

### Why did Command+C not stop the running Python process?

Because Command+C is the macOS copy shortcut.

Terminal interruption uses Control+C.

## What Was Independently Noticed, Challenged, or Verified

- The Google Cloud documentation did not match the live credential-download interface.
- The OAuth credential download was independently found behind the information icon.
- `credentials.json` was verified as ignored before any staging operation.
- Finder-generated `.DS_Store` was recognized as non-project metadata.
- The active production-versus-test boundary was challenged before connecting additional systems.
- The existing `main.py` was inspected to prove that email input remained simulated.
- Python package discovery behavior was tested rather than assumed.
- The OAuth flow was tested separately before full browser authorization.
- Google's Test-user restriction was identified from an actual failed authorization.
- Python indentation was challenged when pasted code visually appeared incorrect.
- It was recognized that visible indentation and logical indentation are not always identical.
- VS Code's automatic paste behavior was identified as a source of risk.
- `py_compile` was adopted as an objective validation step.
- Token persistence was tested by running authentication twice.
- The second authentication was verified not to reopen the browser.
- Git was checked after real credential and token files existed.
- GitHub was manually checked after the authentication module was pushed.

## What Those Questions and Observations Taught

The lesson established several important engineering boundaries.

```text
Source code
vs
authentication material

OAuth client identity
vs
user authorization

API enabled
vs
account authorized

Test Google account
vs
production operational account

Simulated email
vs
production email

Repository structure
vs
Python module search path

Visual indentation
vs
logical Python nesting

Editor contents
vs
saved filesystem contents

Local Git state
vs
public GitHub state
```

The repeated verification steps reinforced the principle that system state should be observed and tested rather than inferred.

## Mistakes Encountered and Corrected

### Google Credential Download Location Was Initially Misidentified

The expected JSON download action was not present where Google's documentation suggested.

Several interface locations were checked before the correct information-icon location was discovered.

The lesson reinforced the need to verify current UI behavior rather than repeatedly assuming outdated documentation was correct.

### `.DS_Store` Appeared as an Untracked File

Finder generated `.DS_Store`.

The file was intentionally excluded through `.gitignore`.

### Python Could Not Import `ingestion`

Initial error:

```text
ModuleNotFoundError: No module named 'ingestion'
```

Correction:

```bash
PYTHONPATH=src
```

### Python Indentation Error

The first authentication attempt failed with:

```text
IndentationError
```

The pasted function body had landed at the wrong logical indentation.

The structure was corrected.

### VS Code Altered Pasted Code

VS Code attempted to automatically reposition pasted Python code.

This caused repeated uncertainty about where blocks belonged.

The correction was to inspect logical indentation explicitly and validate with `py_compile`.

### Ambiguous Instruction Terminology

The word `section` was used when a single line was actually meant.

This caused uncertainty about how much existing code should be replaced.

The terminology was corrected to distinguish lines, blocks, functions, import blocks, logical indentation, and continuation indentation.

### A Partial-Code Editing Approach Became Error-Prone

Incremental block replacement became unreliable after VS Code repeatedly adjusted pasted indentation.

The safer recovery was to replace the complete contents of `google_auth.py` with one known-good full version and then syntax-test it.

### Google OAuth Returned `403 access_denied`

The selected development account had not been added as an OAuth Test user.

The account was added under Google Auth Platform → Audience → Test users.

Authorization then succeeded.

### Wrong macOS Shortcut Was Used to Interrupt Python

Command+C copied instead of stopping the process.

Control+C correctly interrupted Python.

## Commit, Push, and Public Verification Status

Completed during Lesson 7:

### macOS Finder Metadata Protection

`.gitignore` was updated to exclude:

```text
.DS_Store
```

Commit message:

```text
Ignore macOS Finder metadata
```

The commit was:

- saved locally
- staged
- committed
- pushed to `origin/main`
- publicly verified on GitHub

### Google OAuth Authentication Module

File:

```text
src/ingestion/google_auth.py
```

Commit message:

```text
Add Google Drive OAuth authentication
```

The authentication implementation was:

- saved locally
- syntax-tested
- OAuth-tested
- token-persistence tested
- token-reuse tested
- checked for credential leakage
- staged
- committed
- pushed to `origin/main`
- publicly verified on GitHub

Before creation of this Lesson 7 learning log, the repository was:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

The Lesson 7 learning log still requires its own:

1. local save,
2. public-safety review,
3. Git staging,
4. commit,
5. push,
6. public GitHub verification.

## Public Safety Review

This learning log intentionally excludes:

- personal email addresses
- OAuth Client ID values
- OAuth Client Secret values
- `credentials.json` contents
- `token.json` contents
- access tokens
- refresh tokens
- production email content
- customer data
- protected company information
- production report URLs
- private account identifiers

The public Python source refers only to the local filenames:

```text
credentials.json
token.json
```

Their sensitive contents remain local and excluded from Git.

## What Was New Compared With Prior Lessons

Lesson 7 introduced:

- creation of a real OAuth Desktop client
- downloading real OAuth client credentials
- real Google browser authorization
- OAuth Testing mode behavior
- OAuth Test users
- Google Drive authorization scopes
- reusable Google `Credentials`
- local OAuth token persistence
- token refresh logic
- Python `None`
- nested conditional logic
- Python file writing
- JSON serialization
- `PYTHONPATH`
- `py_compile`
- logical indentation terminology
- continuation indentation terminology
- macOS Finder project-file management
- `.DS_Store` handling
- Control+C process interruption
- explicit verification of the development-versus-production boundary
- proof that the credential protections created in Lesson 5 work with real credential files

This lesson marked the transition from Google Cloud configuration to an actually authenticated standalone Python application.

## Current Boundary

Lesson 7 ends with Google Drive authentication working.

The Python project can now:

```text
Create the OAuth flow
→ authorize an approved test user
→ receive Google Credentials
→ save authorization to token.json
→ reload saved authorization
→ refresh credentials when possible
→ avoid unnecessary browser reauthorization
```

The following have not yet been implemented:

- creating a Google Drive API service object for actual file operations
- listing Drive files
- creating Drive folders
- uploading reports to Drive
- downloading real reports
- Gmail API authentication
- reading production Gmail
- modifying production email
- processing production report links
- reproducing the JavaScript Drive-storage behavior

Those items belong to later lessons after they are individually implemented and verified.