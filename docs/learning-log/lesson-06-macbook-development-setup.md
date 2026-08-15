# Lesson 6: MacBook Development Environment Setup

## Purpose

Lesson 6 established the MacBook as a second development workstation for the `python-report-ingestion` project.

The goal was not merely to copy project files to another computer. The goal was to reproduce the development environment correctly using GitHub as the shared repository while keeping machine-specific components, such as Python virtual environments, local to each computer.

This lesson also introduced cross-platform development concepts involving Windows, macOS, and Linux-compatible command-line workflows.

## What Was Completed

- Installed Apple's Command Line Developer Tools.
- Verified Git installation on the MacBook:
  - `git version 2.50.1 (Apple Git-155)`
- Installed Visual Studio Code for Apple Silicon.
- Signed VS Code into GitHub.
- Created a local `Projects` directory on the MacBook.
- Cloned the existing GitHub repository into:
  - `~/Projects/python-report-ingestion`
- Opened the cloned repository in VS Code.
- Verified that the repository file tree matched the project stored on the Windows PC.
- Verified the MacBook repository was on `main`, synchronized with `origin/main`, and clean.
- Compared Python versions between the Windows PC and MacBook.
- Identified that the MacBook initially had Python 3.9.6.
- Verified that the Windows project `.venv` uses Python 3.14.6.
- Installed Python 3.14.6 on the MacBook to match the Windows project environment.
- Created a new Mac-specific `.venv`.
- Activated the Mac virtual environment using the macOS/Linux workflow.
- Verified the Mac `.venv` uses Python 3.14.6.
- Inspected the Windows virtual environment's installed Python packages.
- Identified the three intentionally installed Google API packages.
- Installed matching versions of those packages on the MacBook.
- Verified the Google package versions.
- Successfully executed the existing Python project on macOS.
- Verified that `.venv` remained excluded from Git.
- Verified the MacBook repository remained synchronized and clean.

## What Was Tested and Verified

### Git Installation

The initial MacBook Git check was:

```bash
git --version
```

macOS reported that the Command Line Developer Tools were not installed.

After installing them, Git reported:

```text
git version 2.50.1 (Apple Git-155)
```

This verified that Git was available on the MacBook.

### Repository Clone

The existing GitHub repository was cloned into:

```text
~/Projects/python-report-ingestion
```

The VS Code Explorer panel showed the same tracked repository structure that existed on the Windows PC.

The MacBook repository was then checked with:

```bash
git status
```

Git reported:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This verified that the clone was synchronized with GitHub.

### Python Version Matching

The MacBook initially reported:

```text
Python 3.9.6
```

The Windows project's active `.venv` reported:

```text
Python 3.14.6
```

Python 3.14.6 was therefore installed on the MacBook before creating the new virtual environment.

After installation:

```bash
python3 --version
```

reported:

```text
Python 3.14.6
```

### Mac Virtual Environment

A new Mac-specific virtual environment was created using the macOS/Linux command:

```bash
python3 -m venv .venv
```

It was activated using:

```bash
source .venv/bin/activate
```

The active environment was verified with:

```bash
python --version
```

which returned:

```text
Python 3.14.6
```

### Google API Dependencies

The Windows `.venv` was inspected using:

```powershell
python -m pip list
```

The three intentionally installed Google packages were identified as:

```text
google-api-python-client 2.198.0
google-auth-httplib2     0.4.1
google-auth-oauthlib     1.4.0
```

The same versions were installed into the Mac `.venv` using:

```bash
python -m pip install google-api-python-client==2.198.0 google-auth-httplib2==0.4.1 google-auth-oauthlib==1.4.0
```

Running:

```bash
python -m pip list
```

on the MacBook confirmed that all three versions matched.

### Existing Python Application

The existing project was executed from the MacBook VS Code Terminal:

```bash
python src/main.py
```

Output:

```text
Santa Fe
https://reports.example.com/sample-report.csv
Santa Fe_Report_2026-08-15.csv
```

This verified that the existing local parsing and filename-generation behavior worked correctly on macOS.

### Git Safety After Environment Creation

After creating `.venv`, installing dependencies, and running the Python project, the MacBook repository was checked again:

```bash
git status
```

Result:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This verified that `.gitignore` correctly prevented the Mac-specific `.venv` from becoming repository content.

## Python Concepts Learned

### Virtual Environments Are Machine-Specific

The Windows `.venv` was not copied through GitHub.

Instead, the MacBook created its own:

```bash
python3 -m venv .venv
```

This demonstrated that the source code is portable through Git, while the runtime environment is reconstructed locally on each development machine.

### Matching Python Versions Across Development Machines

The MacBook already contained Python 3.9.6, but the Windows project used Python 3.14.6.

Rather than accepting different Python versions, the MacBook was configured with Python 3.14.6 before its `.venv` was created.

This reduced an unnecessary source of cross-platform differences.

### Python Package Dependencies

Running:

```bash
python -m pip list
```

showed many packages even though only three Google packages had intentionally been installed.

This demonstrated that top-level Python packages can automatically require and install supporting dependencies.

It was therefore unnecessary to manually install every package shown in the Windows `pip list`.

### Exact Package Versions

The syntax:

```text
package-name==version
```

was introduced.

For example:

```text
google-api-python-client==2.198.0
```

The `==` specifies an exact package version.

This allowed the MacBook to reproduce the intentional Google dependency versions already used by the Windows project.

## Git and GitHub Concepts Learned

### GitHub Enables Multi-Computer Development

The project now operates conceptually as:

```text
Windows PC
    ↕
  GitHub
    ↕
MacBook
```

Each computer maintains its own local repository.

GitHub acts as the shared remote repository through which committed project changes can move between machines.

The Windows PC does not need to remain powered on for the MacBook to work with repository content already pushed to GitHub.

### Cloning a Repository

The MacBook did not receive the project directly from the Windows PC.

Instead, it cloned the repository stored on GitHub.

Cloning created a new local Git repository containing the tracked project files and Git history.

### Ignored Files Are Not Distributed Through GitHub

The Windows `.venv` did not appear on the MacBook after cloning.

The MacBook created its own `.venv`, and that environment also remained absent from `git status`.

This demonstrated the practical purpose of `.gitignore` in a multi-machine development workflow.

### Git Commands Can Be Cross-Platform

Commands such as:

```bash
git status
```

work the same across Windows, macOS, and Linux.

The operating-system differences encountered during this lesson were primarily related to shells, paths, environment activation, and local software installation rather than Git itself.

## macOS/Linux Concepts Learned

### macOS and Linux Are Different Operating Systems

Linux was introduced during this lesson for the first time.

The distinction established was:

```text
Windows  = Microsoft operating system
macOS    = Apple operating system
Linux    = open-source family of operating systems
```

The MacBook is running macOS, not Linux.

However, macOS is Unix-based, and many command-line conventions are shared between macOS and Linux.

### macOS/Linux Command Compatibility

The virtual-environment activation command:

```bash
source .venv/bin/activate
```

is an example of a workflow shared by macOS and Linux.

Windows PowerShell uses a different command:

```powershell
.\.venv\Scripts\Activate.ps1
```

A documentation convention was established during this lesson:

When a command or procedure is compatible across macOS and Linux, future lessons should identify it as:

```text
macOS/Linux
```

When commands differ by platform, they should be clearly separated.

### VS Code Terminal Versus macOS Terminal

The MacBook provides a standalone Terminal application.

VS Code also provides an integrated Terminal inside the editor.

Both can execute shell commands.

For project work, the VS Code integrated Terminal was preferred because it was already operating inside the cloned repository and kept the command-line work visually connected to the project.

## Meaningful Questions Raised

### How can the project be worked on away from the home PC?

This question led directly to the multi-computer development architecture.

The key lesson was that GitHub is not merely a public backup location. It can function as the synchronization point between independent development machines.

### What does it mean when Git is unavailable on a new Mac?

Running `git --version` caused macOS to request Apple's Command Line Developer Tools.

This established that Git was not yet available and that Apple's developer command-line package provides it.

### Is VS Code available through the Mac App Store?

VS Code was not found in the Mac App Store.

It was learned that VS Code is installed directly from Microsoft's distribution.

### Does the MacBook require the Intel or Apple Silicon version of VS Code?

The MacBook reported an Apple A18 Pro chip.

This identified the machine as Apple Silicon and determined which VS Code build to install.

### Should the MacBook use its existing Python 3.9.6 installation?

No assumption was made.

The Windows project's active `.venv` was checked first and found to use Python 3.14.6.

The MacBook was then deliberately configured to match the project's existing Python version.

### Why were many packages shown when only three Google packages had been installed?

This revealed the distinction between directly installed packages and their dependencies.

The three intentional Google packages caused supporting libraries to be installed automatically.

### What is Linux?

Linux was identified as a separate operating-system family heavily used in software engineering, cloud systems, servers, containers, and development environments.

The important immediate lesson was that macOS and Linux frequently share command-line conventions even though they are not the same operating system.

### Should Python commands be run in VS Code or the MacBook Terminal?

Both can run the commands.

For this project, the VS Code integrated Terminal was preferred because it maintains clearer project context.

## What Was Independently Noticed, Challenged, or Verified

- The MacBook already contained Python before the project environment was created.
- The existing Python version was significantly older than the Windows project's version.
- The correct Python version was verified from the Windows `.venv` rather than assumed.
- VS Code required architecture selection between Intel and Apple Silicon.
- The cloned repository visually matched the Windows repository in the VS Code Explorer panel.
- Installing three Google packages resulted in many supporting dependencies being installed.
- The Mac-specific `.venv` did not appear in Git status.
- The same Python application produced the expected output on a second operating system.
- macOS and Linux share many terminal conventions despite being different operating systems.
- The distinction between the standalone macOS Terminal and the VS Code integrated Terminal became operationally important.

## What Those Questions and Observations Taught

The project is not tied to a single physical workstation.

Portable project state includes:

```text
Source code
Git history
Tracked documentation
Dependency requirements
Python version expectations
Configuration rules
```

Machine-specific state includes:

```text
.venv
Locally installed Python packages
Operating-system-specific activation commands
VS Code installation
Local filesystem paths
```

This distinction is important for reproducible development and systems engineering.

A repository should contain what another workstation needs to reconstruct the project, rather than attempting to store every local runtime artifact.

## Mistakes Encountered and Corrected

### Git Was Not Initially Available on the MacBook

Running:

```bash
git --version
```

produced a message that developer tools were missing.

Apple's Command Line Developer Tools were installed.

Git was then successfully verified.

### The MacBook Initially Used a Different Python Version

The MacBook reported:

```text
Python 3.9.6
```

The Windows project environment reported:

```text
Python 3.14.6
```

Python 3.14.6 was installed on the Mac before creating the project's Mac `.venv`.

### VS Code Installation Source Was Initially Unclear

VS Code could not be found in the Mac App Store.

The correct installation method was identified as Microsoft's direct macOS distribution.

### Platform Architecture Had to Be Identified

The VS Code download required choosing Intel or Apple Silicon.

The Mac's chip information was checked before selecting the installer rather than guessing.

### PowerShell Script Execution Was Blocked on Windows

When the Windows `.venv` needed to be activated for Python-version verification, PowerShell reported that script execution was disabled.

The execution policy was temporarily changed for that PowerShell process, after which the virtual environment could be activated.

This reinforced that Windows PowerShell security behavior differs from macOS/Linux shell behavior.

## Commit, Push, and Public Verification Status

At the end of the technical portion of Lesson 6:

- MacBook Git installation: verified
- MacBook VS Code installation: verified
- GitHub sign-in: completed
- Repository clone: verified
- Branch: `main`
- Remote synchronization: verified
- Python 3.14.6: verified
- Mac `.venv`: created and verified
- Google dependency versions: verified
- Existing Python behavior on macOS: verified
- `.gitignore` behavior on Mac: verified
- Working tree before learning-log creation: clean

The Lesson 6 learning log is being created from the MacBook.

The remaining lesson-close repository workflow is:

1. Save this learning log locally.
2. Review it for public safety.
3. Stage it with Git.
4. Commit it with a descriptive message.
5. Push it to GitHub.
6. Verify the file and commit publicly on GitHub.

These steps must be completed before the Lesson 6 learning log itself is considered fully published and verified.

## Public Safety Review

This learning log contains no:

- credentials
- authentication tokens
- OAuth secrets
- customer data
- production email content
- real secure URLs
- protected company information

Example URLs used by the test program are non-production sample values.

## What Was New Compared With Prior Lessons

Lesson 6 introduced:

- macOS development
- Apple Command Line Developer Tools
- Apple Silicon application selection
- multi-machine Git/GitHub development
- Git repository cloning onto a second workstation
- cross-platform Python-version matching
- machine-specific Python virtual environments
- dependency reproduction on a second computer
- exact Python package-version installation
- macOS/Linux shell conventions
- the distinction between macOS and Linux
- the distinction between VS Code Terminal and the standalone macOS Terminal
- cross-platform execution of the existing Python project
- verification that `.gitignore` behaves correctly on a second operating system

This was the first lesson in which the project was successfully reconstructed and executed on a second physical computer and a second operating system.