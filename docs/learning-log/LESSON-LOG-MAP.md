# Engineering Learning Log Map

## Purpose

This file defines the standardized structure, documentation rules, and completion process for every Engineering Learning Log in the `python-report-ingestion` project.

The purpose of the learning logs is not merely to summarize completed instructions.

Each log must preserve the engineering reasoning of the lesson, including:

- what was built or configured,
- what was tested,
- what was independently verified,
- what questions were raised,
- what those questions taught,
- what failed,
- how failures were corrected,
- what Python concepts were learned,
- what Git and GitHub concepts were learned,
- what other technical domains were introduced,
- what was committed and published,
- what remains intentionally incomplete.

The logs form a chronological engineering-learning history of the JavaScript-to-Python migration.

---

## Why This Standard Exists

Lessons 4, 5, and 6 established a recurring engineering-log structure, but the headings were not completely standardized.

Lesson 7 exposed the need for a permanent schema.

Differences had developed in areas such as:

- `Objective` versus `Purpose`,
- naming of observation sections,
- placement of public-safety review,
- when domain-specific concept sections were added,
- how lesson boundaries were documented.

Beginning with Lesson 8, all learning logs will use the canonical structure defined in this file.

Older logs remain valid historical records and do not need to be rewritten solely for formatting consistency.

---

## Canonical Learning Log Structure

Every completed lesson must use the following top-level structure in this order.

```text
# Lesson N: Descriptive Title

## Objective

## What Was Completed

## What Was Tested and Verified

## New Python Concepts Learned

## New Git and GitHub Concepts Learned

## [Domain-Specific Concepts Learned]

## Meaningful Questions Raised

## What Was Independently Noticed, Challenged, or Verified

## What Those Questions and Observations Taught

## Mistakes Encountered and Corrected

## Commit, Push, and Public Verification Status

## Public Safety Review

## What Was New Compared With Prior Lessons

## Current Boundary
```

The domain-specific concepts section is conditional.

Examples include:

```text
## Google Cloud and OAuth Concepts Learned

## macOS/Linux Concepts Learned

## API Concepts Learned

## VS Code Concepts Learned

## PowerShell Concepts Learned
```

A domain-specific section should exist only when the lesson introduces or materially deepens that technical domain.

---

# Section Mapping Rules

## Objective

### Purpose

State what the lesson was intended to accomplish.

This section should establish:

- the technical goal,
- the controlled scope,
- the starting boundary,
- any deliberate limitations.

### Include

Examples:

```text
Recreate a specific JavaScript behavior in Python.
Establish Google OAuth authentication.
Configure a second development workstation.
Standardize the learning-log documentation process.
```

### Do Not Include

Do not describe accomplishments here as though they were already completed.

Those belong under:

```text
## What Was Completed
```

---

## What Was Completed

### Purpose

Record concrete work that was actually completed during the lesson.

### Include

- files created,
- files modified,
- configuration performed,
- packages installed,
- APIs enabled,
- functionality implemented,
- environment setup,
- Git operations completed,
- public verification completed.

### Rule

Do not include planned work that was not completed.

Use factual past-tense statements.

---

## What Was Tested and Verified

### Purpose

Document evidence that the completed work actually behaved as intended.

### Include

- terminal commands,
- program output,
- `git status` results,
- browser behavior,
- API behavior,
- version checks,
- syntax checks,
- visual verification,
- GitHub verification,
- regression checks.

### Evidence Pattern

When useful, document:

```text
Command
→ observed output
→ engineering conclusion
```

Example:

```bash
python src/main.py
```

Output:

```text
Santa Fe
https://reports.example.com/sample-report.csv
Santa Fe_Report_2026-08-15.csv
```

Conclusion:

```text
The existing parsing and filename-generation behavior remained intact.
```

### Rule

Do not claim something was verified unless an actual observation supported it.

---

## New Python Concepts Learned

### Purpose

Record Python concepts that were introduced or materially deepened during the lesson.

### Include

Examples:

```text
functions
imports
None
if / else
nested conditionals
file handling
virtual environments
third-party libraries
PYTHONPATH
py_compile
datetime
f-strings
```

### Rule

Do not repeatedly list basic Python concepts in every lesson unless the lesson materially expanded understanding of them.

---

## New Git and GitHub Concepts Learned

### Purpose

Record Git or GitHub concepts introduced or materially deepened during the lesson.

### Include

Examples:

```text
git status
git fetch
staging
commits
push
clone
remote-tracking branches
.gitignore
multi-machine development
public verification
tracked versus untracked files
```

### Rule

Routine repetition of an already-mastered command does not automatically make it a new concept.

Document new understanding rather than merely every command executed.

---

## Domain-Specific Concepts Learned

### Purpose

Capture substantial technical learning outside Python and Git/GitHub.

### Examples

```text
Google Cloud
OAuth
Google APIs
macOS/Linux
PowerShell
VS Code
HTTP
CSV processing
filesystem behavior
```

### Rule

Add this section only when the domain is substantial enough to justify its own learning category.

Use a specific heading.

Example:

```text
## Google Cloud and OAuth Concepts Learned
```

Do not use a generic heading such as:

```text
## Other Concepts
```

---

## Meaningful Questions Raised

### Purpose

Preserve the learner's actual technical questions.

Questions are part of the engineering record because they reveal:

- uncertainty,
- assumptions being challenged,
- architectural concerns,
- security concerns,
- emerging understanding.

### Include

Questions actually raised during the lesson.

Example:

```text
### Why did Python report `No module named 'ingestion'`?

The package lived under `src`, which was not in the module search path for that command.
```

### Critical Rule

Never invent questions that were not actually raised.

If no meaningful questions occurred, write:

```text
No meaningful questions were raised during this lesson.
```

---

## What Was Independently Noticed, Challenged, or Verified

### Purpose

Document observations that were not merely passive completion of instructions.

This section records active technical reasoning.

### Include

Examples:

- noticing conflicting documentation,
- questioning whether production data was being touched,
- recognizing an unexpected Git file,
- detecting inconsistent Python indentation,
- comparing two environments,
- independently checking GitHub,
- recognizing a platform difference,
- verifying an assumption before proceeding.

### Rule

This section should demonstrate active engagement with the system.

It must not simply duplicate:

```text
## What Was Completed
```

---

## What Those Questions and Observations Taught

### Purpose

Explain why the questions and observations mattered.

This converts events into engineering understanding.

### Good Pattern

```text
Observation:
Git showed a file as untracked.

Lesson:
The file existed locally but had never been added to repository history.
```

### Include

- system boundaries,
- causal relationships,
- architectural distinctions,
- reproducibility lessons,
- security implications,
- development workflow lessons.

---

## Mistakes Encountered and Corrected

### Purpose

Preserve failures as engineering evidence.

### Include

- Python errors,
- Git mistakes,
- command errors,
- UI misunderstandings,
- incorrect assumptions,
- ambiguous instructions,
- copy/paste failures,
- wrong filesystem locations,
- credential or configuration issues.

### Required Structure

For meaningful mistakes, identify:

```text
What happened
→ why it happened
→ how it was corrected
→ what was learned
```

### Critical Rule

Do not hide mistakes simply because they were corrected.

A corrected failure is often more educational than a successful first attempt.

---

## Commit, Push, and Public Verification Status

### Purpose

Document repository publication state precisely.

### Include

For each meaningful repository change:

- file or feature,
- commit message,
- saved status,
- staged status,
- committed status,
- pushed status,
- public GitHub verification status.

Example:

```text
File:

src/ingestion/google_auth.py

Commit message:

Add Google Drive OAuth authentication

Status:

Saved locally: Yes
Staged: Yes
Committed: Yes
Pushed: Yes
Publicly verified: Yes
```

### Learning Log Publication

The lesson log itself must also be tracked separately.

When the log is first written, the section should state that the log still requires:

1. save,
2. safety review,
3. staging,
4. commit,
5. push,
6. public verification.

The lesson is not fully published until those steps are complete.

---

## Public Safety Review

### Purpose

Ensure public GitHub documentation does not expose protected information.

### Review For

Never publish:

- passwords,
- OAuth Client Secrets,
- OAuth tokens,
- refresh tokens,
- credential file contents,
- personal email addresses unless intentionally public,
- customer data,
- production email content,
- secure production URLs,
- internal identifiers,
- protected company information,
- secrets embedded in screenshots or examples.

### Safe Documentation

Generally safe to document:

- architecture,
- filenames,
- public library names,
- commands,
- test/sample URLs,
- sanitized output,
- error types,
- conceptual explanations.

### Rule

Every learning log must receive this review before it is committed.

---

## What Was New Compared With Prior Lessons

### Purpose

Show progression rather than repeating the entire learning history.

### Include

Only capabilities or concepts genuinely new to that lesson.

Examples:

```text
first use of Google OAuth
first macOS development environment
first Python datetime handling
first Git clone onto a second computer
first token persistence
```

### Rule

Do not list concepts merely because they appeared again.

This section should answer:

```text
What could the learner understand or do after this lesson that was not true before it?
```

---

## Current Boundary

### Purpose

Define exactly where the project stands when the lesson ends.

This section creates the starting point for the next lesson.

### Include

What now works.

Example:

```text
OAuth authentication works.
Saved tokens are reused.
Sensitive credentials remain outside Git.
```

Also include what deliberately does not yet work.

Example:

```text
Google Drive file operations are not implemented.
Gmail API authentication is not implemented.
Production email is not accessed.
```

### Rule

Do not describe future work as though it has already been completed.

This section is the handoff between lessons.

---

# Documentation Style Rules

## Accuracy Over Appearance

The learning log is an engineering record.

Accuracy takes priority over making the lesson appear smoother than it actually was.

Record:

- failures,
- confusion,
- corrections,
- unexpected system behavior,
- changed assumptions.

---

## Preserve Chronological Logic

Sections are organized by category, but descriptions should still preserve cause and effect.

Example:

```text
The OAuth command failed.
The error was examined.
The test-user restriction was identified.
The account was added.
The command was rerun.
Authentication succeeded.
```

Do not rewrite this as though authentication worked immediately.

---

## Do Not Invent History

The log must not contain:

- questions that were never asked,
- tests that were never run,
- conclusions that were never verified,
- commands that were never used,
- capabilities that were not implemented.

If uncertain, document the uncertainty rather than manufacture completeness.

---

## Distinguish Instruction From Observation

The log should distinguish:

```text
What was instructed
```

from:

```text
What was actually observed
```

Verification requires observation.

---

## Distinguish Technical State From Repository State

A feature can work locally without being committed.

A file can be committed locally without being pushed.

A push can succeed without having been manually verified on GitHub.

These states must remain distinct.

```text
Local file
→ staged file
→ local commit
→ remote push
→ public verification
```

---

## Cross-Platform Documentation

When commands are shared by macOS and Linux, identify them as:

```text
macOS/Linux
```

When Windows PowerShell differs, document it separately.

Example:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Code Terminology

Use the following terminology consistently:

```text
line
    One specific line of code.

block
    A related group of code lines.

function
    A block beginning with def.

import block
    The group of import statements near the top of a Python file.

section
    A larger conceptual portion of a file or document.

logical indentation level
    Actual Python block nesting.

continuation indentation
    Visual indentation used when one statement spans multiple lines.
```

Avoid using `section` when referring to a single code line.

---

# Markdown Delivery Standard

When a lesson is completed, ChatGPT must provide the learning log as:

```text
one complete Markdown block
```

The entire log must be copyable as one unit.

The user will:

1. create the `.md` file in the VS Code Explorer panel,
2. paste the complete Markdown content,
3. save the file,
4. verify the saved filesystem state,
5. stage the file,
6. commit it,
7. push it,
8. verify it publicly on GitHub.

Do not split a completed learning log across multiple independent code blocks intended for separate copying.

Internal Markdown code fences may appear inside the single outer delivery block.

---

# Learning Log Filename Standard

Learning logs belong in:

```text
docs/learning-log/
```

Use:

```text
lesson-NN-descriptive-title.md
```

Examples:

```text
lesson-04-report-filename-generation.md
lesson-05-google-cloud-api-foundation.md
lesson-06-macbook-development-setup.md
lesson-07-google-drive-oauth-authentication.md
```

Use two-digit lesson numbers.

The filename should describe the primary technical focus of the lesson.

---

# Lesson Completion Workflow

Every lesson closes using the following sequence.

## Step 1: Confirm Technical Boundary

Determine that the lesson's technical objective has reached a logical stopping point.

Do not create the final log while major lesson work is still underway.

## Step 2: Reconstruct the Lesson

Review the entire lesson from its starting boundary.

Identify:

- completed work,
- tests,
- questions,
- observations,
- errors,
- corrections,
- concepts,
- repository actions,
- safety issues,
- final boundary.

## Step 3: Build the Log Using This Map

Use every required canonical section.

Add domain-specific concept sections only when justified.

## Step 4: Public Safety Review

Remove or sanitize protected information before publication.

## Step 5: Create the Markdown File

Create the file in:

```text
docs/learning-log/
```

Paste the complete standardized log.

## Step 6: Save Before Git

The file must be saved to disk before running Git staging commands.

An unsaved VS Code editor buffer is not part of the filesystem and cannot be committed correctly.

## Step 7: Verify With Git

Run:

```bash
git status
```

Confirm that the intended learning-log file appears.

## Step 8: Stage Only the Intended File

Example:

```bash
git add docs/learning-log/lesson-NN-descriptive-title.md
```

## Step 9: Verify Staging

Run:

```bash
git status
```

Confirm that only intended files are staged.

## Step 10: Commit

Use a descriptive commit message.

Example:

```bash
git commit -m "Document Lesson 7 Google Drive OAuth authentication"
```

## Step 11: Verify Local Commit State

Run:

```bash
git status
```

Expected condition before push:

```text
branch ahead of origin/main by 1 commit
working tree clean
```

## Step 12: Push

Run:

```bash
git push
```

## Step 13: Verify Synchronization

Run:

```bash
git status
```

Expected result:

```text
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Step 14: Public GitHub Verification

Manually verify:

- learning-log filename,
- file contents,
- commit message,
- correct repository location,
- absence of sensitive information.

Only after this step is the lesson log considered fully published.

---

# Required Lesson Completion Checklist

Every completed lesson must demonstrate:

```text
[ ] Objective documented
[ ] Completed work documented
[ ] Testing and verification documented
[ ] Python learning documented
[ ] Git/GitHub learning documented
[ ] Relevant domain learning documented
[ ] Meaningful questions documented
[ ] Independent observations documented
[ ] Lessons from observations documented
[ ] Mistakes and corrections documented
[ ] Commit/push/public-verification status documented
[ ] Public safety review completed
[ ] New learning compared with prior lessons documented
[ ] Current technical boundary documented
[ ] Markdown file saved locally
[ ] Git status checked
[ ] File staged
[ ] Staging verified
[ ] File committed
[ ] Local commit state verified
[ ] File pushed
[ ] Repository synchronization verified
[ ] File publicly verified on GitHub
```

---

# Role of the Learning Logs

These files serve multiple purposes.

They are:

- a chronological engineering record,
- a Python learning history,
- a Git and GitHub learning history,
- a systems-engineering reasoning record,
- evidence of troubleshooting experience,
- documentation of the JavaScript-to-Python migration,
- a record of security decisions,
- a record of cross-platform development,
- a reproducibility aid,
- a source for future portfolio and README documentation.

The logs should therefore preserve not only successful results, but the reasoning that produced those results.

---

# Standard Going Forward

Beginning with Lesson 8, every Engineering Learning Log will use this map.

The structure may gain a new domain-specific concepts section when a lesson genuinely introduces another technical domain, but the canonical top-level progression will remain stable.

Any future change to the learning-log standard should be made deliberately by updating this map rather than silently changing the structure of individual lesson files.