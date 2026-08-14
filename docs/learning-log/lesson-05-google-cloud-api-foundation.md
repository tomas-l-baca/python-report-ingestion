# Lesson 5: Google Cloud and API Foundation

## Objective

Prepare the Python report-ingestion project for future Google Drive integration without accessing production systems or exposing authentication material.

This lesson expanded the migration beyond Python syntax and Git by introducing the infrastructure required when moving from Google Apps Script's built-in Google services to a standalone Python application.

## What Was Completed

- Began the lesson from a clean, synchronized `main` branch.
- Activated the project's Python virtual environment.
- Added the following security exclusions to `.gitignore`:
  - `credentials.json`
  - `token.json`
- Staged, committed, pushed, and publicly verified the `.gitignore` protection.
- Installed the official Google Python packages required for future Google API authentication and access:
  - `google-api-python-client`
  - `google-auth-httplib2`
  - `google-auth-oauthlib`
- Verified that the requested Google packages were installed inside the project's `.venv`.
- Learned why standalone Python requires Google client libraries while Google Apps Script provides built-in service objects such as `GmailApp` and `DriveApp`.
- Created the first Google Cloud project used in this learning progression.
- Enabled the Google Drive API for the sandbox Cloud project.
- Configured the Google Auth Platform / OAuth consent foundation.
- Configured the OAuth application as an external testing application for use with a personal Google account.
- Stopped before creating OAuth client credentials or allowing Python to access Google Drive.

## What Was Tested and Verified

### Git Safety

The repository was confirmed clean and synchronized before new work began.

After adding authentication-file exclusions, the `.gitignore` change was:

1. reviewed,
2. staged,
3. committed,
4. pushed to GitHub,
5. publicly verified.

The public repository was checked to confirm that both credential filenames were excluded.

### Python Package Installation

The Google API packages were installed only inside the project's active virtual environment.

`google-api-python-client` was explicitly verified with:

```powershell
python -m pip show google-api-python-client
```

The output confirmed:

- the expected Google API Client Library package,
- an installed version,
- its dependencies,
- installation under the project's `.venv\Lib\site-packages` directory.

The remaining two requested packages were also confirmed installed.

This established that installing Python libraries does not place those libraries in the project's `src` directory and does not involve files stored in Google Drive.

### Google Cloud Configuration

The following were visually verified in Google Cloud:

- the sandbox Cloud project was successfully created,
- the project was selected as the active Cloud project,
- Google Drive API showed `Status: Enabled`,
- the OAuth application setup was completed,
- the audience was configured for external testing,
- support/contact information was configured,
- the Google API Services agreement was accepted.

No OAuth client credential was created during this lesson.

## New Python Concepts Learned

### Third-Party Libraries

A Python library is reusable code written by someone else that can be installed and imported rather than recreated manually.

The Google libraries installed in this lesson provide the Python-side plumbing required to communicate with Google APIs.

Conceptually:

```text
Our Python code
        ↓
Google Python client libraries
        ↓
Google APIs
        ↓
Google services
```

This differs in appearance from Apps Script, but both environments depend on Google-provided software.

Apps Script effectively provides:

```text
Our JavaScript
        ↓
GmailApp / DriveApp
        ↓
Google services
```

### `python -m pip`

The command:

```powershell
python -m pip
```

runs Python's package installer through the same Python interpreter associated with the active environment.

This helps ensure packages are installed into the intended virtual environment.

### `site-packages`

Installed Python libraries live in the virtual environment's `site-packages` directory.

They are dependencies used by our code, not project source files that we manually write in `src`.

## New Git and GitHub Concepts Learned

### Protect Sensitive Files Before They Exist

A `.gitignore` rule can be added before a sensitive file is created.

This creates a safety boundary in advance so future OAuth credential and token files are not accidentally staged or committed.

The lesson established that `.gitignore`:

- contains patterns telling Git what not to track,
- does not create the ignored files,
- does not delete ignored files,
- can protect future files before they appear.

### Credential Safety and Public Repositories

Authentication configuration must be separated into two categories:

```text
Safe to document publicly:
API architecture, setup process, library names, concepts

Not safe to publish:
OAuth credentials, access tokens, private account information
```

This distinction became important before any Google authentication files were created.

## Google Cloud and API Concepts Learned

### Google Cloud Project

A Google Cloud project acts as a configuration container for APIs, credentials, and application settings.

The sandbox project created in this lesson is separate from the production report-ingestion system.

### API

An API is an interface that allows one program to request functionality or data from another system.

Enabling the Google Drive API means the Cloud project is allowed to make Drive API requests once valid authentication is later provided.

Enabling the API alone does not grant access to a Google Drive account.

### OAuth

OAuth provides a controlled authorization process through which a user can give an application permission to access specified Google services.

The consent configuration created during this lesson defines the identity and audience of the application that will later request authorization.

No account authorization occurred yet.

### Apps Script Versus Standalone Python

An important architectural difference became visible during this lesson.

Google Apps Script hides much of the infrastructure because services such as `DriveApp` and `GmailApp` are integrated into the Apps Script environment.

Standalone Python must explicitly establish:

```text
Python application
→ Google client library
→ OAuth authorization
→ Google API
→ Google service
```

This is not an enhancement to the original report-ingestion behavior. It is infrastructure required to reproduce that behavior outside Apps Script.

## Meaningful Questions Raised

### What does `.gitignore` actually do?

This clarified that `.gitignore` is a tracked text file containing patterns for files Git should not track. It does not delete files or create the files listed within it.

### Do `credentials.json` and `token.json` already exist?

No. They had not been created. Their filenames were added to `.gitignore` first as a preventive security measure.

This demonstrated the value of building security controls before introducing sensitive material.

### Why are we moving from our own Python modules to Google libraries, and what is a library?

This revealed an important distinction between application code and dependencies.

Our `src` files contain behavior we write. Google libraries contain reusable Google-provided code our application can call when communicating with Google APIs.

### Are Google Python libraries the same thing as files in Google Drive?

No.

The libraries are installed locally inside the Python virtual environment. Google Drive files are remote user data stored in Google's service.

### Did the JavaScript version require us to write the Google communication code ourselves while Python uses Google's prewritten code?

Not exactly.

Apps Script also relied on Google-provided code, but exposed it through built-in objects such as `GmailApp` and `DriveApp`.

Python makes that dependency more visible because the client libraries must be installed and the APIs configured explicitly.

### What is the Google Cloud Console?

This was the first introduction to Google Cloud in the project.

The Cloud Console was understood as the administrative interface used to create Cloud projects, enable APIs, and configure authentication for applications outside Apps Script.

### What did the Google Cloud and OAuth setup actually accomplish?

The setup created the permission framework that the Python application will eventually use.

It did not yet allow Python to access Google Drive.

## Independent Observations, Challenges, and Verification

### Google Cloud Was an Unexpected Part of the Migration

It was independently noticed that Google Cloud and non-Apps-Script APIs had become substantial parts of the Python migration.

This matters beyond simply making the program work because the project now documents practical exposure to:

- cloud projects,
- APIs,
- OAuth,
- external application authentication,
- Google client libraries.

It was decided that these technologies should eventually be represented in the repository README once the integration has actually been completed and verified.

### Enabling an API Does Not Grant Data Access

A useful distinction was repeatedly verified:

```text
API enabled ≠ account authorized
```

The Drive API is available to the Cloud project, but no Python program currently has permission to read or modify Google Drive data.

### Sandbox Separation Remains Important

The Cloud work was intentionally performed for a personal sandbox rather than the production report-ingestion environment.

The production automation was not modified or interrupted.

## Mistakes Encountered and Corrected

### Google Cloud Project Name Length

The initially suggested Cloud project name exceeded Google's 30-character project-name limit by one character.

Google returned:

```text
The name must be between 4 and 30 characters
```

A shorter project name was selected and creation then succeeded.

This demonstrated that platform constraints should be verified rather than assumed.

### Accidental Git Commit Editor From Earlier Log Publication

While publishing the Lesson 4 learning log at the beginning of this lesson, `git commit` was entered without the `-m` option, which opened Git's default Vim editor.

The first attempted instruction assumed text could immediately be entered on the first line. The cursor position showed that assumption was incorrect.

The safe recovery was:

```text
Esc
:q!
Enter
```

This exited Vim without saving editor changes while leaving the staged file intact.

The commit was then completed explicitly with:

```powershell
git commit -m "Add Lesson 4 engineering learning log"
```

This taught that Git staging survives cancellation of the commit-message editor and that `-m` provides a simpler beginner-friendly commit workflow.

## Commit, Push, and Public Verification Status

Completed during Lesson 5:

- Lesson 4 Engineering Learning Log was committed, pushed, and publicly verified as opening work for this lesson.
- `.gitignore` OAuth credential protection was committed.
- Commit message:

```text
Protect Google OAuth credential files
```

- The commit was pushed to GitHub.
- The public `.gitignore` was verified to contain rules protecting:
  - `credentials.json`
  - `token.json`

Google Python libraries were installed inside `.venv`, which is intentionally ignored by Git, so installing those packages did not create repository changes requiring a commit.

The Google Cloud configuration exists outside the Git repository and therefore does not itself produce Git changes.

## Public Safety Review

This log intentionally excludes:

- personal email addresses,
- OAuth client IDs,
- OAuth client secrets,
- OAuth credential files,
- authorization tokens,
- production URLs,
- customer information,
- protected company information,
- production email content.

No sensitive authentication material was created or published during the technical portion of this lesson.

## What Was New Compared With Prior Lessons

Previous lessons focused primarily on:

- local Python project structure,
- reproducing JavaScript logic in Python,
- Git and GitHub workflow,
- parsing report email information,
- deterministic filename generation.

Lesson 5 introduced an entirely new infrastructure layer:

- Python package dependencies,
- Google's Python client libraries,
- Google Cloud projects,
- Google Drive API enablement,
- OAuth concepts,
- external application authorization architecture,
- preventive credential-file security.

This marked the transition from reproducing isolated application logic to preparing the Python application to communicate with an external cloud service.

## Current Boundary

Lesson 5 technical work ends with the Google Cloud, Drive API, and OAuth consent foundation configured.

Not yet completed:

- OAuth client creation,
- downloading `credentials.json`,
- creating `token.json`,
- Python authentication,
- accessing Google Drive from Python,
- Gmail API configuration,
- reproducing Drive storage behavior,
- updating the README with verified Google Cloud/API experience.

Those items belong to subsequent lessons after they are actually implemented and tested.