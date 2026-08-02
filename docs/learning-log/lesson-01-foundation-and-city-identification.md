# Engineering Learning Log 01: Foundation and City Identification

## Objective

Create the local and public foundation for a Python recreation of an existing report-ingestion automation, then translate and test the first behavior: identifying a city from an email subject.

## What Was Completed

- Verified Python 3.14.6 was installed and available through both `py` and `python`.
- Installed Git and Visual Studio Code.
- Installed the Microsoft Python extension.
- Configured Git author information using a GitHub private `noreply` email.
- Created the local `python-report-ingestion` project folder.
- Initialized a Git repository and renamed the default branch from `master` to `main`.
- Created a Python virtual environment named `.venv`.
- Created `.gitignore` rules for `.venv/` and `__pycache__/`.
- Created and published the initial README.
- Created the initial project folder structure.
- Created and ran `src/main.py`.
- Created `src/ingestion/message_parser.py`.
- Recreated the city-identification behavior for Rio Rancho, Santa Fe, and Belen.
- Connected the local repository to the public GitHub repository.

## What Was Tested and Verified

- Confirmed Python executed `src/main.py`.
- Confirmed `.venv` was excluded from Git tracking.
- Confirmed the city-identification function returned the correct city for matching subjects.
- Tested multiple city subjects.
- Confirmed exact subject matching depended on punctuation, spacing, and capitalization.
- Verified each pushed file and commit publicly on GitHub.

## Python Concepts Learned

- A `.py` file contains Python code.
- `main.py` can act as the program entry point and coordinate other modules.
- `def` defines a function.
- Function parameters receive input values.
- `return` sends a result back to the caller.
- `if` and `elif` test alternative conditions.
- `=` assigns a value.
- `==` compares two values.
- `from ... import ...` allows one Python file to use a function from another file.
- Python indentation defines code structure.
- Saving a file is required before Python can run its newest contents.
- Splitting code into focused modules is a normal professional practice, not merely a beginner technique.

## Git and GitHub Concepts Learned

- Git stores local version history; GitHub stores the remote public copy.
- `git init` creates a local repository.
- A branch is a line of project history.
- `git status` reports tracked, modified, staged, and untracked files.
- Git tracks files, not empty folders.
- Git may summarize a new untracked folder rather than list every file inside it.
- `git status --untracked-files=all` reveals every untracked file.
- `git add` places selected changes into the staging area.
- `git commit` records a local checkpoint.
- `git push` uploads commits to GitHub.
- A commit ID uniquely identifies a checkpoint.
- `.gitignore` contains rules telling Git which generated files not to track.

## Questions Raised and What They Taught Me

### What does `py -m venv .venv` mean?

This question established that commands must be understood in parts rather than copied blindly. I learned that `py` invokes Python, `-m` runs a module, `venv` creates a virtual environment, and `.venv` is the destination folder.

### Is `.gitignore .venv/ __pycache__/` one filename?

This exposed the difference between a file name and file contents. `.gitignore` is the file name; `.venv/` and `__pycache__/` are separate lines inside it.

### Should `.gitignore` be saved beside `.venv`?

I learned that project configuration files normally live at the repository root and can control folders beside them.

### Why did the dot disappear from the VS Code tab after saving?

I learned that the dot marks unsaved changes. Its disappearance confirms the file was saved.

### Why did Git show `src/` instead of `src/main.py`?

I learned that Git may summarize new folders. The longer status command can reveal each contained file.

### How are `main.py` and `message_parser.py` related?

I learned that both are Python code. `main.py` coordinates the workflow while `message_parser.py` performs a specialized task.

### Is modular code structure elementary or professional?

I learned that the implementation was intentionally simple, but modular separation is common professional design because it supports testing, maintenance, and clearer responsibilities.

### Would changing the sample subject produce another city?

I verified that the function selects the matching `elif` branch and returns the corresponding city.

### Why did copying an `elif` line into `main.py` cause an error?

I learned that `main.py` needed an assignment using `=`, while `message_parser.py` used comparison conditions with `==`.

## What I Independently Noticed or Challenged

- Commands were being provided faster than I could interpret them, so I required plain-English explanations.
- I distinguished the Windows File Explorer from the VS Code Explorer panel after interface confusion.
- I recognized that `main.py` was acting as a coordinator and questioned whether that structure was standard.
- I noticed Git summarized folders rather than showing the exact new file.
- I tested another subject independently to verify the function’s behavior.
- I recognized that exact subject text controlled the result.
- I noticed when unsaved code caused Python to execute the previous version.

## Mistakes Encountered and Corrected

- PowerShell blocked the virtual-environment activation script. A temporary process-scoped execution-policy change allowed activation without permanently weakening the system setting.
- VS Code and Windows File Explorer were confused. The interfaces were explicitly distinguished.
- `main.py` was run before being saved, so Python executed the previous version. Saving corrected the result.
- An `elif` comparison line was copied where a variable assignment was required. Replacing `==` with the correct assignment form fixed the error.
- New folders appeared absent from Git because they were empty. I learned Git records files rather than folders.

## Commit, Push, and Public Verification

The following commits were created, pushed, and publicly verified:

- `6603f2c` — Add Python project gitignore
- `5e10349` — Add initial project README
- `14aed73` — Add initial Python entry point
- `6e72d38` — Add city identification from email subject

Public verification confirmed:

- Branch `main`
- `.gitignore`
- `README.md`
- `src/main.py`
- `src/ingestion/message_parser.py`
- Correct commit messages and file contents

## What Was New Compared With Prior Learning

This was the foundation lesson. It introduced the complete local-to-public development cycle and established the first working JavaScript-to-Python translation unit. The most important shift was moving from using isolated commands to understanding how Python files, Git history, VS Code, PowerShell, and GitHub cooperate as one development system.