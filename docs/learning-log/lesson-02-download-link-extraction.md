# Engineering Learning Log 02: Download-Link Extraction

## Objective

Recreate the next existing Apps Script behavior in Python: extracting a downloadable report URL from an email’s HTML body while preserving the city-identification behavior completed in Lesson 1.

## What Was Completed

- Added Python’s `re` module to `message_parser.py`.
- Created `extract_download_url(body)`.
- Used a sanitized `reports.example.com` URL instead of the production AWS address.
- Updated `main.py` to test both city identification and URL extraction.
- Preserved previously completed behavior instead of replacing it.
- Committed and pushed the working feature.

## What Was Tested and Verified

- Confirmed the function extracted the complete CSV download URL from sample HTML.
- Confirmed city identification still returned `Santa Fe`.
- Confirmed both functions worked together through `main.py`.
- Verified the updated files and commit publicly on GitHub.

## Python Concepts Learned

- `import re` loads Python’s regular-expression tools.
- `re.search()` looks for a text pattern.
- A regular expression can locate a URL inside HTML.
- `match.group(1)` returns the captured portion of a match.
- `None` represents the absence of a matching value.
- One coordinator file can import multiple functions from the same module.
- Existing behavior should remain visible when adding the next translated component.

## Git and GitHub Concepts Learned

- Git preserves committed versions even after the current file changes.
- `git log --oneline` displays commit history.
- `git show` displays changes stored in a commit.
- `git show COMMIT_ID:path` can display an earlier version of one file.
- Local Git history is stored in the hidden `.git` folder.
- VS Code Source Control is a graphical interface controlling the same Git repository used by PowerShell.
- A file appearing under Source Control does not necessarily mean it is staged.
- `git status` remains the authoritative check before committing.
- `git push` sends local commits to `origin/main`.
- Git commonly displays file paths with `/`, while Windows commonly displays paths with `\`.

## Questions Raised and What They Taught Me

### If `main.py` is replaced, will GitHub lose the earlier behavior?

I recognized that replacing the file would make the current public version show only the newest test. Git would preserve the previous committed version, but the visible current program would no longer demonstrate both completed behaviors. I learned to preserve working functionality while adding the next component.

### Why does Git preserve an earlier version?

I learned that each commit is a saved snapshot. Older versions remain accessible through commit history even when the current file changes.

### Where is Git visible on the PC?

I learned that Git’s repository data is stored in the hidden `.git` folder and can also be viewed through VS Code’s Source Control panel.

### Why did VS Code say Source Control was unavailable in Restricted Mode?

I learned that VS Code limits extensions and Git integration until a workspace is trusted.

### Does the VS Code Commit button bypass PowerShell?

I learned that VS Code is a graphical front end for the same Git commands. It does not replace Git, but it can hide staging details that are useful while learning.

### What is the normal workflow after editing files?

I reinforced the sequence:

`edit → status → add → commit → push → verify`

I also learned that each command represents a separate state transition rather than one combined save operation.

### Why does Git place quotes around `'origin/main'`?

I learned that Git uses quotes to identify an exact branch name within its message. Those quotes are not PowerShell syntax.

### Why do some paths use backslashes and others use forward slashes?

I learned that Windows normally uses `\`, while Git, URLs, macOS, and Linux commonly use `/`. Git uses forward slashes for consistency across operating systems.

## What I Independently Noticed or Challenged

- I noticed that replacing `main.py` would remove the earlier visible demonstration.
- I questioned how historical code remains recoverable.
- I investigated the VS Code Source Control interface instead of relying only on PowerShell.
- I recognized that files shown under the Commit button were not necessarily staged.
- I asked for the Git workflow in operational order rather than memorizing isolated commands.
- I noticed inconsistent-looking slash directions and asked how they were used.
- I verified GitHub after pushing instead of assuming the command output alone was sufficient.

## Mistakes Encountered and Corrected

- `main.py` was initially replaced with a test containing only URL extraction. It was corrected to test both completed behaviors.
- The commit command was run before the files were staged. Git refused to create the commit, and the files were then staged with `git add`.
- VS Code Source Control was initially disabled by Restricted Mode. Trusting the workspace enabled Git integration.
- Files visible in Source Control were mistaken for staged files. `git status` clarified their actual state.

## Commit, Push, and Public Verification

Commit created and publicly verified:

- `09b28f4` — Add download link extraction

Public verification confirmed:

- `src/main.py` contained both city identification and URL extraction.
- `src/ingestion/message_parser.py` contained `extract_download_url`.
- The sanitized sample URL was visible instead of the production address.
- Branch `main` showed the correct latest commit.

## What Was New Compared With Prior Learning

Lesson 1 established the development environment, repository, and first Python module. Lesson 2 introduced pattern-based text extraction, preservation of earlier behavior, inspection of historical commits, and the distinction between seeing changes in VS Code and actually staging them in Git.

The major reasoning advance was recognizing that adding a feature is not only about making new code work. It also requires protecting completed behavior, understanding repository state, and verifying that the public version accurately represents the current system.