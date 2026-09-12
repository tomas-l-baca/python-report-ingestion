# Python Report Ingestion

A hands-on software engineering and systems-learning project centered on reconstructing an existing Gmail-to-Google-Drive report ingestion automation in Python.

This repository began with a relatively narrow goal: faithfully recreate an existing JavaScript automation in Python.

It has evolved into something considerably broader.

The project now documents the process of learning how application code, cloud services, APIs, authentication, operating systems, development environments, version control, debugging, security boundaries, and technical documentation fit together as one working system.

## Project Purpose

The original automation processes recurring report emails, identifies the appropriate destination based on the email subject, extracts a report download link, generates a standardized filename, and stores the resulting report in the correct Google Drive folder.

Rather than redesigning that system immediately, this project follows a deliberate engineering constraint:

> First understand and faithfully reproduce the existing behavior. Improve it only after the original workflow has been successfully reconstructed.

That constraint turns the project into more than a code translation exercise.

The goal is to understand why each component exists, how it interacts with the rest of the system, how to verify that it works, and how to reproduce the development environment safely across machines.

## What I Am Learning

### Python

Python is a new programming language for this project.

The migration is being built incrementally while learning concepts such as:

- functions and return values
- conditional logic and control flow
- modules and imports
- regular expressions
- date and time handling
- `None` and guard conditions
- logical versus continuation indentation
- package dependencies
- application structure
- syntax validation
- integration between independently developed modules

The emphasis is not simply on producing working syntax. Each new Python concept is connected to an actual requirement from the existing automation.

## Systems Integration

One of the most important lessons to emerge from this project is that working software is much more than application code.

The project requires understanding the relationships between:

```text
email data
    ↓
message parsing
    ↓
application control flow
    ↓
authentication
    ↓
Google APIs
    ↓
Google Drive
    ↓
filesystem and project environment
    ↓
Git and GitHub
```

A function can be correct while the overall system still fails because of authentication, environment configuration, path resolution, API configuration, operating-system differences, Git state, or external-service behavior.

Learning to reason across those boundaries has become a major objective of the project.

## Cloud and API Engineering

The reconstruction requires hands-on work with Google Cloud and Google APIs.

Work completed so far includes:

- creating and configuring a Google Cloud project
- enabling the Google Drive API
- configuring OAuth consent
- creating a Desktop OAuth client
- understanding OAuth credentials and access tokens
- implementing browser-based OAuth authentication in Python
- persisting and refreshing authentication tokens
- constructing a Google Drive API service
- querying Drive for folders
- locating nested city-specific folders
- testing successful and unsuccessful API lookup paths

Development is performed against a personal sandbox environment rather than production data.

## Cross-Platform Development

The project is intentionally being developed across both Windows and macOS.

This has required learning that source-code synchronization and development-environment synchronization are separate problems.

The Windows environment includes:

- PowerShell
- Python virtual environments
- PowerShell execution-policy behavior
- Windows filesystem conventions
- VS Code
- Git

The macOS environment introduces:

- Unix-style terminal commands
- shell environment variables
- macOS filesystem conventions
- different virtual-environment activation commands
- different keyboard and editor behavior
- Unix/Linux-style command-line conventions

Both machines use independent virtual environments, credentials, and authentication tokens while sharing source code through GitHub.

This has made environment reproducibility and cross-platform configuration first-class parts of the project rather than incidental setup work.

## Git and GitHub

Git and GitHub are being learned as engineering tools rather than treated only as a place to upload finished files.

The project has included hands-on work with:

- repositories
- staging
- commits
- branches
- local versus remote state
- `HEAD`
- `origin/main`
- fetching
- pulling
- fast-forward-only synchronization
- pushing
- staged diff inspection
- ignored files
- cross-machine synchronization
- commit verification
- public repository verification

An important recurring lesson has been that editor state, filesystem state, Git staging state, local repository state, and GitHub state are different layers and must be verified independently.

## Debugging and Verification

A major learning objective is developing the discipline to verify what the system is actually doing rather than assuming the cause of a problem.

Examples have included:

- syntax checking before execution
- isolating modules before integrating them
- testing both successful and unsuccessful control-flow paths
- inspecting Git state before committing
- reviewing staged diffs
- distinguishing unsaved editor content from saved filesystem content
- distinguishing stale Git remote information from current GitHub state
- deliberately testing missing folders
- deliberately testing invalid parser input
- verifying persistent OAuth behavior
- checking assumptions when observed behavior differs from expectations

Mistakes are documented rather than hidden because the diagnosis and correction often demonstrate more engineering reasoning than the successful command that follows.

## Security and Public-Safety Practices

This is a public repository, so security boundaries are part of the engineering process.

The project intentionally keeps sensitive material outside Git, including:

```text
credentials.json
token.json
```

The repository does not publish:

- OAuth secrets
- authentication tokens
- production report URLs
- customer data
- production email content
- internal identifiers
- real Google Drive folder IDs
- protected company information

Synthetic and sanitized values are used for development and documentation whenever possible.

## Engineering Learning Logs

A defining part of this repository is the Engineering Learning Log system.

Every completed lesson receives its own chronological learning log stored in:

```text
docs/learning-log/
```

These are not simple progress notes.

Each log documents:

- the lesson objective
- what was actually completed
- what was tested and verified
- new Python concepts learned
- new Git and GitHub concepts learned
- relevant environment or platform concepts
- meaningful questions raised during the work
- observations or assumptions that were independently challenged
- what those questions and observations taught
- mistakes encountered
- why those mistakes occurred
- how they were corrected
- commit and push status
- public GitHub verification
- public-safety review
- what was genuinely new compared with previous lessons
- the exact technical boundary at which the lesson ended

The logs are designed to preserve engineering reasoning, not merely a history of commands.

A standardized lesson-log map is maintained at:

```text
docs/learning-log/LESSON-LOG-MAP.md
```

The repository also contains a separate environment-engineering learning summary focused on the cross-platform, tooling, configuration, and troubleshooting work that has emerged throughout the migration.

## Current Implementation

The Python project currently includes separate components for:

- identifying a target city from an email subject
- extracting a sanitized report download URL
- generating the expected report filename
- authenticating with Google through OAuth
- constructing a Google Drive API service
- locating the required root Drive folder
- locating the appropriate city subfolder
- coordinating parser output with downstream Drive lookup
- stopping downstream processing when required parser or Drive values are unavailable

The current application can therefore connect several independently developed modules into one controlled execution path.

## Current Boundary

The reconstruction is intentionally incomplete.

The Python application does not yet:

- search Gmail through the Gmail API
- retrieve production email messages
- download the actual report file
- upload the report CSV into Google Drive
- mark a processed email as read
- reproduce the complete original JavaScript workflow

Those capabilities will be added incrementally and tested before the project moves beyond faithful reconstruction into possible improvements.

## What This Repository Demonstrates

This repository is intended to show the development process, not just the final program.

It demonstrates growing practical experience with:

- Python software development
- systems-oriented problem solving
- API integration
- OAuth authentication
- Google Cloud configuration
- Google Drive API interaction
- Git and GitHub
- Windows PowerShell
- macOS and Unix-style terminal environments
- VS Code
- virtual environments
- dependency management
- cross-platform development
- debugging
- controlled testing
- secure handling of credentials
- technical documentation
- incremental software reconstruction
- verification-driven engineering

The larger objective is to develop the ability to understand, reconstruct, test, document, and eventually improve a real automation system across the full stack of technologies required to make it work.