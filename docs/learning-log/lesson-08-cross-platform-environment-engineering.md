# Lesson 8: Cross-Platform Environment Engineering and Documentation Standardization

## Objective

Resume development on the Windows PC after completing Google Drive OAuth authentication on the MacBook, synchronize the two development environments, establish equivalent persistent OAuth authentication on Windows, verify credential security, and standardize the project's engineering-learning documentation.

The lesson intentionally stopped before implementing Google Drive API file operations.

Its technical boundary was environment readiness. Lesson 9 will begin with Python application-code development.

## What Was Completed

- Returned development from the MacBook to the Windows PC.
- Located the project repository from a newly opened PowerShell session.
- Refreshed the PC's Git remote-tracking information.
- Discovered that the PC was six commits behind `origin/main`.
- Fast-forwarded the Windows repository to the current GitHub state.
- Verified a clean, synchronized working tree.
- Reactivated the Windows Python virtual environment.
- Resolved PowerShell's script-execution restriction using a process-scoped execution-policy change.
- Verified that `credentials.json` and `token.json` had correctly remained machine-local rather than being transferred through Git.
- Investigated how to provision OAuth credentials on the second machine.
- Confirmed that Google's current interface no longer allowed the existing OAuth client secret to be downloaded.
- Created an additional OAuth client secret for the Windows environment while preserving the existing MacBook secret.
- Downloaded and installed a Windows-local `credentials.json`.
- Verified that Git continued to ignore the credential file.
- Completed OAuth authorization independently on Windows.
- Created a Windows-local `token.json`.
- Verified persistent authentication by running authentication again without browser login or additional authorization.
- Verified that both authentication files remained excluded from Git.
- Analyzed Lessons 4, 5, and 6 to establish a permanent Engineering Learning Log structure.
- Re-created Lesson 7 using the standardized structure.
- Created and published:
  - `docs/learning-log/LESSON-LOG-MAP.md`
- Created and published the recruiter-focused:
  - `docs/learning-log/environment-engineering-learning-log.md`
- Established the Environment Engineering Summary as a separate portfolio/resume evidence artifact rather than overloading individual lesson logs.

## What Was Tested and Verified

### Windows Repository Location

The first Git command after returning to the PC failed with:

```text
fatal: not a git repository (or any of the parent directories): .git
```

The PowerShell session was located at:

```text
C:\Users\t_bac
```

rather than inside the repository.

After changing into:

```text
C:\Users\t_bac\Projects\python-report-ingestion
```

Git recognized the repository.

### Remote Repository Synchronization

The PC initially reported that its branch was current.

After:

```powershell
git fetch
```

Git reported that the Windows branch was six commits behind and could be fast-forwarded.

The repository was updated using:

```powershell
git pull --ff-only
```

Final verification showed:

```text
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This proved that the Windows machine had received the work completed previously on the MacBook.

### Windows Virtual Environment

Activation initially failed because PowerShell script execution was disabled.

The restriction was bypassed for the current PowerShell process only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

The virtual environment was then activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

The prompt displayed:

```text
(.venv)
```

confirming activation.

### Machine-Local Authentication State

After synchronizing the repository, PowerShell tested:

```powershell
Test-Path credentials.json
Test-Path token.json
```

Both returned:

```text
False
```

This verified that the files intentionally excluded through `.gitignore` had not traveled from the MacBook through GitHub.

### Windows OAuth Credential Provisioning

The existing Google OAuth client was inspected.

Google's current interface stated that existing client secrets could no longer be viewed or downloaded and that a new secret should be created if the original was unavailable.

A second client secret was created.

The original secret was left enabled to avoid disrupting the working MacBook environment.

The newly downloaded Windows credential file was installed locally as:

```text
credentials.json
```

PowerShell verified:

```powershell
Test-Path credentials.json
```

returned:

```text
True
```

`git status` did not list the file.

### Windows OAuth Authorization

The Windows PowerShell session configured the project's Python module path:

```powershell
$env:PYTHONPATH="src"
```

Authentication was executed through the existing Python `authenticate()` function.

The browser authorization completed successfully.

Python printed:

```text
Credentials
```

### Windows Token Persistence

After authorization:

```powershell
Test-Path token.json
```

returned:

```text
True
```

Authentication was executed again.

Observed behavior:

- the browser remained closed,
- Google login was not requested,
- additional authorization approval was not requested,
- Python printed `Credentials`.

This verified actual token reuse rather than merely verifying that `token.json` existed.

### Final Credential-Safety Verification

After both Windows authentication files existed, `git status` reported:

```text
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This verified that neither sensitive file had entered Git.

### Documentation Standardization

The standardized Learning Log Map was:

- created,
- saved,
- staged,
- committed,
- pushed,
- publicly verified on GitHub.

The recruiter-focused Environment Engineering Summary was also:

- created,
- saved,
- staged,
- committed,
- pushed,
- publicly verified on GitHub.

## New Python Concepts Learned

Lesson 8 deliberately contained limited new Python syntax because its primary purpose became completing the cross-platform environment.

The Python-related learning centered on runtime behavior rather than application logic.

### Environment-Dependent Module Resolution

The Windows PowerShell session used:

```powershell
$env:PYTHONPATH="src"
```

to make the project's `src` directory available to Python's module search path.

This reinforced the distinction between:

```text
Python source structure
```

and:

```text
Python runtime configuration
```

### Persistent Authentication as Observable Program Behavior

The existing Python authentication function was exercised on a second operating system.

The same Python code successfully:

- initiated OAuth,
- returned a Google `Credentials` object,
- created local authorization state,
- loaded that authorization state on a subsequent execution.

This demonstrated that application behavior depends partly on the environment surrounding the Python code.

### Python Training Balance

A significant observation during the lesson was that much of the project time had shifted toward environment engineering rather than direct Python coding practice.

This was explicitly recognized rather than allowing the distinction to remain hidden.

Lesson 9 will intentionally move the center of the training back to writing, understanding, predicting, testing, and debugging Python application code.

## New Git and GitHub Concepts Learned

### `git status` Can Use Stale Remote Information

The Windows repository initially appeared current.

After `git fetch`, Git revealed that it was actually six commits behind GitHub.

This demonstrated that `git status` does not necessarily contact the remote repository before reporting the local branch relationship.

### `git fetch`

`git fetch` refreshes the local repository's knowledge of remote history without immediately changing local working files.

This became an important cross-machine startup step.

### `git pull --ff-only`

The Windows repository was synchronized using:

```powershell
git pull --ff-only
```

This permitted a direct fast-forward while preventing Git from automatically creating a merge commit if histories had diverged.

### Repository State Versus Machine State

The PC successfully received six repository commits but did not receive:

```text
credentials.json
token.json
```

This provided direct evidence that Git synchronization and machine-environment synchronization are different processes.

### Documentation as Version-Controlled Engineering Material

Two documentation artifacts were deliberately treated like engineering deliverables:

```text
LESSON-LOG-MAP.md
environment-engineering-learning-log.md
```

Both followed controlled save, stage, commit, push, and public-verification workflows.

## Windows / PowerShell Concepts Learned

### Current Working Directory

Opening a terminal does not guarantee that the shell is inside the repository.

The initial:

```text
fatal: not a git repository
```

failure demonstrated that commands execute relative to the shell's current location.

### Process-Scoped Execution Policy

PowerShell prevented virtual-environment activation because script execution was disabled.

Using:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

changed the policy only for the active PowerShell process.

This avoided making an unnecessary permanent system-wide security-policy change.

### PowerShell Environment Variables

The syntax:

```powershell
$env:PYTHONPATH="src"
```

was used to configure Python's module path for the active PowerShell session.

### `Test-Path`

PowerShell's:

```powershell
Test-Path
```

was used to verify filesystem state directly.

It provided objective checks for the existence of:

```text
credentials.json
token.json
```

rather than relying on assumptions based on VS Code or Git.

## Google Cloud and OAuth Concepts Learned

### OAuth Credentials Are Not Repository State

The MacBook possessed working OAuth credentials and authorization.

Synchronizing the repository to Windows did not transfer those files because they were intentionally excluded from Git.

Each machine therefore required valid local authentication material.

### Existing Client Secrets May Not Be Recoverable

Google's current interface prevented re-downloading the existing OAuth client secret.

This demonstrated that secret material may be intentionally shown or downloadable only under limited circumstances.

### Multiple Client Secrets

A second client secret was created for the Windows environment while preserving the existing MacBook secret.

This allowed both environments to continue functioning without distributing the MacBook's private credential through GitHub or chat.

### Authentication Versus Persistent Authorization

Successful first-time OAuth authentication did not by itself prove that future executions would avoid login.

Token persistence was separately verified by executing authentication again and observing that no browser authorization was required.

## Documentation and Configuration Management Concepts Learned

### Standardized Documentation Schema

Review of prior learning logs showed that the same general engineering categories were being captured, but headings and organization had drifted.

A permanent canonical structure was therefore created in:

```text
docs/learning-log/LESSON-LOG-MAP.md
```

The map defines:

- required headings,
- heading order,
- evidence standards,
- terminology,
- public-safety requirements,
- completion workflow,
- Git publication workflow,
- lesson-boundary documentation.

### Historical Records Versus Standards

Older learning logs remain valid historical records.

The new map governs future logs rather than rewriting previous history merely to make old documents cosmetically identical.

### Summary Versus Forensic Record

While creating the Environment Engineering Summary, an important documentation distinction was identified.

A recruiter-focused summary should not reproduce every command or conversational step.

Instead, it should:

- consolidate repeated actions into competencies,
- retain representative technical evidence,
- emphasize outcomes,
- preserve defensible claims,
- remove procedural noise.

The first overly granular approach was rejected and the document was rewritten from scratch as a recruiter-focused engineering capability summary.

## Meaningful Questions Raised

### What does `.venv` mean?

This clarified that `.venv` represents the project's Python virtual environment.

### Why did Git say this was not a repository?

Because PowerShell had opened in the Windows user directory rather than the repository.

### Why did the PC initially appear synchronized but later show six missing commits?

Because Git's local knowledge of `origin/main` had not yet been refreshed from GitHub.

### Why did PowerShell refuse to activate the virtual environment?

Because PowerShell's script-execution policy blocked the activation script.

### Why were `credentials.json` and `token.json` missing after the repository was synchronized?

Because those files were intentionally excluded from Git and are machine-local authentication state.

### Should the existing OAuth secret be replaced?

No.

The existing secret was preserved because the MacBook could still depend on it.

A second secret was created for Windows instead.

### Don't we need to configure authentication so Google login is not required every time?

Yes.

The presence of `token.json` suggested persistence, but actual reuse was verified by executing authentication again and confirming that no browser login occurred.

### Why has so much project time not involved practicing Python coding?

Because substantial environment engineering was required to establish a secure, reproducible, cross-platform runtime around the Python application.

This question resulted in explicitly separating environment-engineering learning from Python application-code training.

### Should the environment-engineering experience be preserved separately?

Yes.

The accumulated experience was substantial enough to justify its own recruiter-focused portfolio artifact.

### Should the Environment Engineering Summary contain every procedural action?

No.

A first draft became too granular.

The distinction between a detailed engineering summary and a conversational/forensic transcript was identified, and the document was redesigned around competencies, representative evidence, outcomes, and defensible resume claims.

## What Was Independently Noticed, Challenged, or Verified

- The initial Windows Git status was challenged rather than assumed to prove current GitHub synchronization.
- Refreshing the remote state revealed six missing commits.
- The distinction between Git repository state and machine-local environment state was verified using real credential files.
- PowerShell's security restriction was identified as a shell issue rather than a Python failure.
- The current Google Cloud interface was inspected rather than relying on previous interface behavior.
- Google's inability to re-download the existing client secret was recognized as a changed provider behavior.
- The existing MacBook secret was deliberately preserved rather than unnecessarily replaced.
- Credential existence was verified directly through the filesystem.
- Credential exclusion was independently verified through Git.
- Token persistence was behaviorally tested rather than inferred from file existence.
- The amount of environment work relative to Python coding was explicitly challenged.
- The environment-engineering work was recognized as independently valuable professional experience.
- The initial recruiter document was challenged for being too granular.
- The documentation strategy was corrected from procedural transcript to competency-focused summary.
- Prior learning-log inconsistencies were challenged and converted into a permanent version-controlled standard.

## What Those Questions and Observations Taught

Lesson 8 reinforced several important engineering distinctions:

```text
Clean Git working tree
≠
latest GitHub state
```

```text
Repository synchronization
≠
environment synchronization
```

```text
Source code
≠
runtime state
```

```text
OAuth client configuration
≠
machine-local credentials
```

```text
Successful first authorization
≠
verified persistent authorization
```

```text
Python failure
≠
environment failure
```

```text
Detailed documentation
≠
repetition of every procedural action
```

```text
Learning Python
≠
learning the environment required to run Python
```

The lesson also demonstrated that environment engineering is not merely preparatory overhead.

It involves:

- reproducibility,
- configuration management,
- security,
- identity,
- version control,
- operating-system behavior,
- cloud configuration,
- troubleshooting,
- verification.

At the same time, those skills should not displace the project's explicit Python-learning objective indefinitely.

## Mistakes Encountered and Corrected

### Git Was Run Outside the Repository

Git initially returned:

```text
fatal: not a git repository
```

The shell was in the Windows user directory.

The terminal was moved into the repository before continuing.

### The PC Was Initially Assumed to Be Current

`git status` initially reported synchronization based on stale remote-tracking information.

After `git fetch`, the PC was shown to be six commits behind.

The repository was fast-forwarded.

This corrected the assumption that a locally clean branch necessarily represents current GitHub state.

### PowerShell Blocked `.venv` Activation

The Windows execution policy prevented `Activate.ps1` from running.

A process-scoped bypass was used rather than changing the policy permanently.

### Credential Transfer Was Initially Considered

The existing MacBook `credentials.json` was considered for transfer to Windows.

No appropriate local transfer mechanism was available.

Rather than moving the secret through GitHub, email, or chat, the Google OAuth configuration was used to provision a new Windows-local secret.

### Existing Google Secret Could Not Be Downloaded

The Google interface no longer permitted downloading the existing secret.

The live provider behavior was accepted as authoritative.

A second secret was created instead.

### Token Existence Was Initially Treated as Nearly Sufficient

`Test-Path token.json` returning `True` proved that the file existed.

It did not prove that the Python application would actually reuse it.

Authentication was run again, and browser-free credential reuse was verified.

### Environment Summary Became Too Granular

The first Environment Engineering document draft resembled a forensic reconstruction of the project.

This did not match the intended recruiter/hiring-manager audience.

The document was rewritten to:

- consolidate repeated activity,
- emphasize competencies,
- retain representative evidence,
- support interview discussion,
- provide defensible resume language.

## Commit, Push, and Public Verification Status

### Lesson 7 Learning Log

Before the main Lesson 8 environment work continued, the corrected Lesson 7 learning log was:

- saved locally,
- staged,
- committed,
- pushed,
- publicly verified on GitHub.

Commit message:

```text
Document Lesson 7 Google Drive OAuth authentication
```

### Standardized Learning Log Map

File:

```text
docs/learning-log/LESSON-LOG-MAP.md
```

Commit message:

```text
Add standardized engineering learning log map
```

Status:

```text
Saved locally: Yes
Staged: Yes
Committed: Yes
Pushed: Yes
Publicly verified: Yes
```

### Environment Engineering Summary

File:

```text
docs/learning-log/environment-engineering-learning-log.md
```

Commit message:

```text
Add environment engineering learning summary
```

Status:

```text
Saved locally: Yes
Staged: Yes
Committed: Yes
Pushed: Yes
Publicly verified: Yes
```

### Lesson 8 Learning Log

This Lesson 8 learning log still requires:

1. local save,
2. public-safety review,
3. Git staging,
4. staging verification,
5. commit,
6. local commit verification,
7. push,
8. repository synchronization verification,
9. public GitHub verification.

## Public Safety Review

This learning log intentionally excludes:

- OAuth Client ID values,
- OAuth Client Secret values,
- `credentials.json` contents,
- `token.json` contents,
- access tokens,
- refresh tokens,
- personal email addresses,
- production email content,
- customer data,
- protected company information,
- production report URLs,
- private account identifiers.

The document identifies sensitive filenames only where necessary to explain architecture and security controls.

The Windows filesystem path documented here identifies only the local project structure and contains no authentication material.

No production Gmail access or production report processing occurred during Lesson 8.

## What Was New Compared With Prior Lessons

Lesson 8 introduced or materially deepened:

- cross-machine return synchronization after development occurred elsewhere,
- understanding that Git remote-tracking information can become stale,
- `git fetch` as a cross-machine synchronization checkpoint,
- `git pull --ff-only`,
- Windows PowerShell process-scoped execution-policy handling,
- PowerShell `Test-Path`,
- PowerShell environment-variable syntax,
- direct verification that ignored authentication files do not travel through Git,
- provisioning OAuth credentials independently on a second development machine,
- working with multiple OAuth client secrets,
- preserving an existing working secret while provisioning another environment,
- independent Windows OAuth authorization,
- Windows-local token persistence,
- behavioral verification of Windows token reuse,
- standardized learning-log configuration management,
- creation of a canonical Learning Log Map,
- formal distinction between chronological lesson logs and recruiter-focused capability summaries,
- creation of a standalone Environment Engineering professional evidence artifact,
- recognition and correction of excessive documentation granularity,
- explicit assessment of environment-engineering training as a separate professional competency,
- explicit decision to rebalance subsequent training toward Python coding.

## Current Boundary

Lesson 8 ends with the cross-platform development environment established and verified.

### Windows

The Windows PC now has:

```text
current GitHub repository state
working Python virtual environment
required source code
local OAuth credentials
local persistent authorization token
working Google authentication
verified token reuse
clean Git state
```

### macOS

The MacBook retains:

```text
working repository
working Python virtual environment
local OAuth credentials
local persistent authorization token
working Google authentication
verified token reuse
```

### GitHub

The repository now contains:

```text
current Python source
completed Lesson 7 learning log
standardized Learning Log Map
recruiter-focused Environment Engineering Summary
```

Sensitive authentication state remains outside Git.

### Documentation

The project now has a canonical learning-log standard.

Future lesson logs will follow:

```text
docs/learning-log/LESSON-LOG-MAP.md
```

rather than reconstructing their organization from memory.

### Application Boundary

The Python application can authenticate to Google successfully.

It does not yet perform actual Google Drive file operations.

The following remain deliberately unimplemented:

- creating the Google Drive API service object for file operations,
- listing Drive files,
- locating or creating Drive folders,
- uploading reports,
- downloading real reports,
- Gmail API integration,
- production email access,
- production report processing,
- complete reproduction of the original JavaScript workflow.

## Lesson 9 Starting Point

Lesson 9 begins after the environment-engineering foundation.

Its focus will shift deliberately toward direct Python training.

The next phase should emphasize:

```text
writing Python
→ understanding each new construct
→ predicting behavior
→ executing the code
→ inspecting results
→ debugging when necessary
```

Environment work should now support the Python implementation rather than dominate the lesson.

The technical starting point is:

```text
Authenticated Google credentials
        ↓
NEXT: Python Google Drive API service construction
        ↓
controlled Drive API operations
```

Lesson 9 therefore begins the next application-development step: using the authenticated credentials from Python to interact with Google Drive while continuing to reproduce the existing JavaScript system behavior without introducing unrelated enhancements.