# Lesson 9: Google Drive Service and Folder Lookup

## Objective

Begin the first substantive Google Drive API coding work in Python after completing the cross-platform environment and OAuth foundation.

The lesson focused on faithfully recreating the first Google Drive behaviors from the existing JavaScript system:

- convert authenticated Google credentials into a usable Drive API service
- locate the existing `Ubivu Ubicquia` root folder
- safely handle a missing root folder
- locate a city subfolder beneath the correct root folder
- safely handle a missing city subfolder
- verify the behavior against a controlled personal Google Drive sandbox

The lesson deliberately stopped before connecting the email parser to the Drive workflow or downloading report files.

## What Was Completed

Created:

`src/ingestion/google_drive.py`

The module imports the Google API client:

```python
from googleapiclient.discovery import build
```

and reuses the existing authentication function:

```python
from ingestion.google_auth import authenticate
```

A new function was created to construct the Google Drive API service:

```python
def create_drive_service():
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)
    return service
```

This separates authentication from Drive API operations.

A root-folder lookup function was then implemented:

```python
def find_root_folder(service):
    query = (
        "name = 'Ubivu Ubicquia' "
        "and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )

    results = service.files().list(
        q=query,
        spaces="drive",
        fields="files(id, name)",
    ).execute()

    folders = results.get("files", [])

    if not folders:
        print("Error: Root folder 'Ubivu Ubicquia' not found in My Drive.")
        return None

    return folders[0]
```

This reproduces the relevant behavior of the original JavaScript:

- search for the named root folder
- exclude trashed folders
- stop safely when no matching folder exists
- use the first returned matching folder

A city-subfolder lookup function was also created:

```python
def find_city_folder(service, root_folder_id, city_name):
    query = (
        f"name = '{city_name}' "
        "and mimeType = 'application/vnd.google-apps.folder' "
        f"and '{root_folder_id}' in parents "
        "and trashed = false"
    )

    results = service.files().list(
        q=query,
        spaces="drive",
        fields="files(id, name)",
    ).execute()

    folders = results.get("files", [])

    if not folders:
        print(f"Warning: Subfolder '{city_name}' not found under Ubivu Ubicquia.")
        return None

    return folders[0]
```

A controlled personal Google Drive sandbox was manually created with this structure:

```text
Ubivu Ubicquia/
├── Rio Rancho/
├── Santa Fe/
└── Belen/
```

The folders were created manually rather than automatically through Python because the original JavaScript expects the folders to already exist. Automatically creating missing folders would have changed the original system's behavior.

## What Was Tested and Verified

The new module was syntax-checked using:

```powershell
python -m py_compile src\ingestion\google_drive.py
```

No syntax errors were reported.

The Drive service construction was tested independently.

The returned Python object type was:

```text
Resource
```

This verified that:

- existing OAuth authentication remained functional
- valid credentials were returned
- `googleapiclient.discovery.build()` successfully created a Google Drive API v3 service object

The root-folder success path was tested against the personal Drive sandbox.

Python successfully returned a dictionary containing:

```text
name: Ubivu Ubicquia
id: [redacted]
```

The real Google Drive folder ID was intentionally excluded from public documentation.

The root-folder failure path was then tested by temporarily renaming the sandbox folder.

The function correctly produced:

```text
Error: Root folder 'Ubivu Ubicquia' not found in My Drive.
None
```

The original folder name was restored after testing.

The city-folder success path was tested using the `Santa Fe` subfolder.

Python successfully:

1. authenticated
2. located the root folder
3. obtained the root folder ID
4. searched only within that root folder
5. found the `Santa Fe` subfolder
6. returned its name and folder ID

The real city-folder ID was also excluded from public documentation.

The city-folder failure path was tested by temporarily renaming the `Santa Fe` sandbox folder.

The function correctly produced:

```text
Warning: Subfolder 'Santa Fe' not found under Ubivu Ubicquia.
None
```

The folder name was restored afterward.

The final Python source file was staged, reviewed, committed, pushed, and manually verified on GitHub.

## New Python Concepts Learned

### Returning and Reusing Objects

The lesson reinforced that a Python function can return an object for use elsewhere:

```python
return service
```

The object returned by `create_drive_service()` becomes the interface used for later Google Drive API operations.

### Separating Responsibilities Between Functions

The new module separates distinct responsibilities:

- `authenticate()` obtains valid credentials
- `create_drive_service()` constructs the Drive API interface
- `find_root_folder()` searches for the required root folder
- `find_city_folder()` searches for a city folder within the root

This demonstrated how multiple small functions can cooperate while each performs one specific job.

### Chained Method Calls

The following structure was examined:

```python
service.files().list(...).execute()
```

This was understood as a sequence:

1. `service.files()` selects the Drive file resource
2. `.list(...)` constructs a file-search request
3. `.execute()` actually sends the request to Google

An important distinction was learned: constructing an API request and executing that request are separate operations.

### Dictionaries

The Google API response is returned as a Python dictionary.

This line:

```python
folders = results.get("files", [])
```

retrieves the `files` value if it exists and otherwise supplies an empty list.

This provides a safe way to handle a response containing no matching files.

Dictionary indexing was also used:

```python
root["id"]
```

to obtain the root folder ID needed for the child-folder search.

### Lists and First-Match Behavior

The Drive API returns matching folders as a list.

This line:

```python
return folders[0]
```

returns the first matching folder.

This was intentionally retained because the original JavaScript also takes the first folder returned by its iterator rather than adding new sorting or duplicate-resolution behavior.

### Formatted Strings

The city-folder query introduced Python f-strings:

```python
f"name = '{city_name}' "
```

and:

```python
f"and '{root_folder_id}' in parents "
```

The lesson demonstrated that the `f` prefix allows values from Python variables to be inserted directly into strings.

### Truth Testing

The condition:

```python
if not folders:
```

was used to detect an empty list.

Instead of explicitly checking the list length against zero, Python can treat an empty list as false.

### `None` as an Explicit Failure Result

Both lookup functions return:

```python
None
```

when the required folder cannot be found.

This gives calling code an explicit result representing the absence of a usable folder.

### Import Resolution and `PYTHONPATH`

The lesson reinforced that Python must know where the `src` directory is in order to import:

```python
ingestion.google_drive
```

The PowerShell environment variable used for the current terminal session is:

```powershell
$env:PYTHONPATH="src"
```

A typo in this variable demonstrated that environment-variable names must be exact.

## New Git and GitHub Concepts Learned

### Reviewing a Newly Staged File

The normal workflow for a new file was clarified as:

```text
Create
→ Save
→ git add
→ git diff --cached
→ commit
→ push
```

After `google_drive.py` was staged, this command was used:

```powershell
git diff --cached
```

This allowed the exact staged contents to be inspected before committing.

### `git diff --no-index` Is Optional

An unfamiliar command was initially introduced:

```powershell
git diff --no-index NUL src\ingestion\google_drive.py
```

This can compare an untracked file against an empty source before the file has been staged.

However, this was not required for the established project workflow.

The simpler and more consistent process is to stage the intended new file and then inspect it with:

```powershell
git diff --cached
```

This distinction became an explicit learning point because the unfamiliar command was challenged rather than being accepted as a required new Git procedure.

### Staged State Versus Committed State

After staging, `git status` confirmed that `google_drive.py` was ready to commit.

After committing, Git reported that the local branch was ahead of `origin/main` by one commit.

This demonstrated again that:

```text
staged ≠ committed
committed locally ≠ pushed remotely
```

### Public Verification Remains a Separate Step

After pushing, the new source file was manually checked on GitHub.

The lesson therefore continued the established distinction between:

- successful local commit
- successful push
- successful public verification

## Google Drive API Concepts Learned

### Credentials Versus an API Service

Authentication credentials and a Drive API service are related but distinct objects.

The existing authentication code answers:

> Is this application authorized to act?

The new code:

```python
build("drive", "v3", credentials=creds)
```

creates the interface that can actually issue Drive API requests.

### Drive API Version

The service was explicitly constructed using:

```text
drive
v3
```

This identifies the Google Drive API and the version being used.

### File Search Queries

The root-folder query uses:

```text
name = 'Ubivu Ubicquia'
and mimeType = 'application/vnd.google-apps.folder'
and trashed = false
```

This limits results to:

- the exact expected name
- Google Drive folders
- items that have not been trashed

### Folder MIME Type

Google Drive represents folders using the MIME type:

```text
application/vnd.google-apps.folder
```

Searching by name alone would not guarantee that the returned item was actually a folder.

### Parent Relationships

The city lookup adds:

```text
'<root_folder_id>' in parents
```

This constrains the search to folders located beneath the specific `Ubivu Ubicquia` root folder.

This matters because another folder named `Santa Fe` could exist elsewhere in Drive.

The parent condition prevents such an unrelated folder from being selected.

### Limiting Returned Fields

The request uses:

```python
fields="files(id, name)"
```

Only the fields required by the current behavior are requested.

The lesson therefore introduced the idea that an API response can be deliberately limited to the data currently needed.

### Controlled API Testing

Both successful and unsuccessful search behavior were tested against a personal Drive sandbox rather than production resources.

Temporary folder renaming was used to create predictable failure conditions without modifying production systems or adding behavior that does not exist in the JavaScript system.

## Meaningful Questions Raised

### Is saying that the virtual environment is "engaged" normal technical terminology?

The question arose after reopening VS Code and confirming the Python environment.

The more conventional wording is that the virtual environment is:

- active
- activated

This improved technical vocabulary without changing the underlying concept.

### Why was `git diff --no-index` different from the normal Git staging and pushing process?

This was raised when an unfamiliar Git command was introduced during final review.

The question correctly identified that the command did not resemble the established workflow used for previous new files.

### Why had earlier new files not required `git diff --no-index`?

This follow-up challenged whether the new command was actually required.

The answer was that it was optional.

The established staging workflow remained fully valid:

```text
git add
→ git diff --cached
→ git commit
→ git push
```

## What Was Independently Noticed, Challenged, or Verified

The unfamiliar `git diff --no-index` step was independently recognized as inconsistent with the Git workflow used during previous lessons.

Rather than assuming that a new command was mandatory because it had been suggested, the difference was challenged directly.

This resulted in distinguishing an optional Git inspection technique from the project's normal workflow.

The exact environment-variable spelling was also exposed through an actual import failure. The failure was traced to:

```powershell
$env:PYTHONSOURCEPATH="src"
```

instead of:

```powershell
$env:PYTHONPATH="src"
```

The correction immediately restored Python's ability to locate the `ingestion` package.

The folder lookup logic was not considered complete after only a successful API request. Both root-folder and city-folder failure paths were deliberately tested.

The user also verified that the Drive queries returned the intended folders from the controlled sandbox rather than assuming that syntactically valid API code meant logically correct behavior.

## What Those Questions and Observations Taught

A Git command can be legitimate without being required.

Understanding whether a command is part of the necessary workflow is more important than simply memorizing additional commands.

The `git diff --no-index` discussion reinforced the distinction between:

- required repository operations
- optional inspection techniques

It also reinforced the value of consistency in a beginner engineering workflow.

The `PYTHONPATH` failure demonstrated that shell environment variables are exact identifiers. A variable with a plausible but incorrect name does nothing for Python's module search process.

The Drive tests demonstrated that code should be evaluated through behavior, not merely syntax.

The successful paths proved that the API could find the intended resources.

The failure paths proved that the Python functions respond safely when those resources are absent.

Testing both paths provides stronger evidence than demonstrating only a successful case.

## Mistakes Encountered and Corrected

### Incorrect `PYTHONPATH` Variable Name

What happened:

The PowerShell session was configured with:

```powershell
$env:PYTHONSOURCEPATH="src"
```

The subsequent Python command failed with:

```text
ModuleNotFoundError: No module named 'ingestion'
```

Why:

Python recognizes `PYTHONPATH`, not `PYTHONSOURCEPATH`.

The incorrectly named environment variable existed in PowerShell but had no effect on Python's import search path.

Correction:

```powershell
$env:PYTHONPATH="src"
```

After the correction, the exact same Python folder-lookup test succeeded.

Lesson:

Environment-variable names must be exact. A successful shell assignment does not prove that the target application recognizes the variable.

### Unnecessary Introduction of `git diff --no-index`

What happened:

An optional command was introduced to inspect the new untracked file before staging:

```powershell
git diff --no-index NUL src\ingestion\google_drive.py
```

Why this became a problem:

Although technically valid, it introduced unnecessary complexity and appeared inconsistent with the Git workflow already learned during previous lessons.

Correction:

The workflow returned to the simpler established process:

```powershell
git add src/ingestion/google_drive.py
git diff --cached
```

Lesson:

A technically valid command is not automatically the best teaching or workflow choice. When an existing process already provides the needed verification safely and clearly, consistency has value.

### Temporary Filename Confusion in Conversation

The new file was verbally referred to once as:

```text
google-drive.py
```

The actual file was verified to be correctly named:

```text
src/ingestion/google_drive.py
```

No repository correction was necessary.

The distinction reinforced that Python module filenames in this project use underscores rather than hyphens.

## Commit, Push, and Public Verification Status

The Lesson 9 Python source was staged and reviewed before committing.

Commit message:

```text
Add Google Drive folder lookup
```

Status:

- source file saved locally: complete
- syntax verification: complete
- staged-content review: complete
- Git commit: complete
- push to `origin/main`: complete
- GitHub public verification: complete
- repository synchronized after push: verified
- Lesson 9 Engineering Learning Log publication: pending at the time this log was drafted

The Lesson 9 learning log itself must still be:

1. saved under `docs/learning-log/`
2. reviewed for public safety
3. staged
4. committed
5. pushed
6. manually verified on GitHub

## Public Safety Review

This lesson used a personal Google Drive sandbox rather than production resources.

The public repository and this log must not contain:

- OAuth client secrets
- `credentials.json` contents
- `token.json` contents
- personal Google account information
- real secure production URLs
- customer information
- production report contents
- internal protected company information
- actual Google Drive folder IDs returned during testing

Real sandbox folder IDs were observed during testing but are deliberately omitted from this public learning log.

Only generic folder names required to reproduce the existing application's behavior are documented.

## What Was New Compared With Prior Lessons

Lesson 7 established Google OAuth authentication.

Lesson 8 established reliable cross-platform development and authentication state.

Lesson 9 moved beyond authentication and began using Google credentials to perform real Google Drive API operations from Python.

New capabilities demonstrated in this lesson include:

- constructing a Google Drive API v3 service object
- issuing live Drive API requests
- understanding `service.files().list(...).execute()`
- interpreting API responses as Python dictionaries and lists
- querying Drive by exact folder name
- filtering for Google Drive folder MIME types
- excluding trashed resources
- constraining searches by parent-folder relationship
- safely handling missing folders with `None`
- testing both success and failure API paths
- using f-strings to dynamically construct API queries
- distinguishing an optional Git inspection command from the required Git workflow

This was also the first lesson in which the project moved from establishing Google authentication infrastructure to actively reproducing the original JavaScript system's Google Drive behavior.

## Current Boundary

At the end of Lesson 9:

- the Python virtual environment works
- Google OAuth authentication works
- persistent authentication remains available
- a Google Drive API v3 service can be constructed
- Python can locate the existing `Ubivu Ubicquia` root folder
- Python safely handles the root folder being absent
- Python can locate a named city folder beneath the correct root
- Python safely handles a city folder being absent
- successful and unsuccessful folder-search behavior has been tested against a controlled personal Drive sandbox
- the Lesson 9 Python source has been committed, pushed, and publicly verified

The system does **not yet**:

- connect the existing email parser output to the Drive lookup functions
- search Gmail through the Gmail API
- download a report from a URL
- create a CSV file in Google Drive
- mark an email as read
- reproduce the complete JavaScript control flow
- operate against production email or production report data

The next lesson should resume from this boundary by connecting existing parsed values such as `city_name` and `download_url` to the Drive-side control flow before implementing report downloading.