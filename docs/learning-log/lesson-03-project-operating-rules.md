# Engineering Learning Log 03: Project Operating Rules

## Objective

Convert the project’s working rules into a permanent, public, version-controlled Markdown document and publish it inside the repository.

## What Was Completed

- Consolidated the project operating rules.
- Added the rules to the ChatGPT Project Instructions.
- Saved the source Markdown file in Google Drive.
- Copied the file into the local repository as:

  `docs/project-operating-rules.md`

- Created the `docs/learning-log/` folder.
- Confirmed the operating-rules file remained separate from the Python source-code folder.
- Committed, pushed, and publicly verified the rules on GitHub.

## What Was Tested and Verified

- Confirmed PowerShell could copy the file from Google Drive when the path was enclosed in quotation marks.
- Confirmed Git detected the new `docs` content.
- Used `git status --untracked-files=all` to reveal the exact new file.
- Confirmed the file was staged before committing.
- Confirmed the push created the same `docs/project-operating-rules.md` structure on GitHub.
- Refreshed the public repository and verified the folder and file were visible.

## Python Concepts Learned

No new Python behavior was introduced in this lesson. The lesson intentionally focused on project governance, PowerShell paths, repository organization, and Git publication.

## Git and GitHub Concepts Learned

- Git preserves a file’s location relative to the repository root.
- A file committed as `docs/project-operating-rules.md` appears in the GitHub `docs` folder.
- Git does not move files into `src` merely because the repository contains source code.
- New folders commonly appear as untracked when their first file is created.
- `git status` may summarize an untracked folder.
- `git status --untracked-files=all` reveals every file inside an untracked folder.
- The longer status command is a diagnostic tool, not a mandatory replacement for normal `git status`.
- Repository documentation can be version-controlled using the same stage, commit, push, and verification process as Python code.

## Questions Raised and What They Taught Me

### Why were quotation marks required around the Google Drive path?

The path contained spaces and an ampersand. I learned that quotation marks tell PowerShell to interpret the entire path as one value. Without quotes, spaces can divide the path into separate command arguments, and `&` can be interpreted as a PowerShell operator.

### Are untracked files common in new projects?

I recognized that untracked files repeatedly appeared whenever new files or folders were created. I learned that this is expected: Git does not automatically begin tracking newly created files.

### Must I always use `git status --untracked-files=all`?

I learned that normal `git status` is still the everyday command. The longer command is useful when Git summarizes a folder and I need to inspect the exact files inside it.

### Where will the pushed file appear on GitHub?

I questioned whether the file would appear as a separate folder or inside `src`. I learned that Git reproduces the path recorded in the commit. Because the file was stored under `docs`, GitHub created or updated the top-level `docs` folder.

### Does pushing determine the destination folder?

I learned that `git push` does not choose the destination folder. The file path is established locally before staging and committing. Push transfers the recorded repository structure.

## What I Independently Noticed or Challenged

- I had begun recognizing that quotation marks were connected to paths containing spaces.
- I specifically noticed that the ampersand could affect how PowerShell interpreted the command.
- I recognized a recurring pattern in how Git reports new files and folders.
- I asked where the pushed file would appear instead of assuming GitHub would organize it automatically.
- I distinguished project documentation from Python source code and verified that each belonged in a separate top-level folder.
- I requested that operating rules become durable project artifacts rather than remain only in conversation memory.

## Mistakes Encountered and Corrected

- The first compiled operating-rules draft omitted several required teaching and learning-log controls. It was reviewed and expanded.
- Earlier memory guidance did not match the available ChatGPT interface. The project settings were rechecked and confirmed.
- The new `docs` content initially appeared only as the summarized folder `docs/`. The exact file was revealed using `git status --untracked-files=all`.
- The destination of the pushed file was uncertain until the local repository path was traced and explained.

## Commit, Push, and Public Verification

Commit message:

`Add project operating rules`

The commit was pushed to the public `main` branch.

Public verification confirmed:

- The `docs` folder appeared at the repository root.
- `docs/project-operating-rules.md` was visible.
- The file was not placed inside `src`.
- The published structure matched the local repository structure.

## What Was New Compared With Prior Learning

Earlier lessons focused on Python execution and translating application behavior. This lesson introduced governance as code-adjacent engineering work.

The main advance was understanding that repository structure, documentation standards, operating rules, shell syntax, and public verification are part of engineering discipline. I moved from merely following repository steps to predicting how file paths, quoting, Git tracking, commits, and remote folder structure interact.