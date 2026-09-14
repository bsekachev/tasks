# SDET Technical Interview Exercise

## Overview

You are given a small Python CLI application.

Your goal is to write an effective test suite for the application.

**Expected duration:** 30–40 minutes.

---

## Your Task

Create a test file:

```text
test_task_stats.py
```

and implement a set of automated tests using `pytest`.

You do **not** need to modify or fix the application code.

The implementation may contain defects. Your tests should be based on the
application specification described below rather than on the application's
current behavior.

A failing test that correctly identifies a violation of the specification is
considered a valid result.

### Testing Requirements

Use `pytest` to implement your tests.

You may:

* execute the application through `subprocess`;
* use pytest fixtures;
* use parametrized tests;
* create temporary files using pytest utilities such as `tmp_path`.

All tests should execute the application through the CLI.
Treat `task_stats.py` as a black-box command-line tool; you do not need to read
or import the application code.

There is no required number of test cases.

Focus on selecting tests that provide meaningful coverage of the specification
rather than maximizing the number of tests.

---

## Application Specification

The application is a command-line utility called:

```text
task_stats.py
```

It counts the number of tasks with a particular status in a JSON file.

### Usage

The application is executed as:

```bash
python task_stats.py <file> --status <status>
```

The following statuses are supported:

```text
completed
failed
pending
```

Status values are case-sensitive; only these exact lowercase values are
supported.

For example, given the following `tasks.json`:

```json
[
  {"id": 1, "status": "completed"},
  {"id": 2, "status": "failed"},
  {"id": 3, "status": "completed"},
  {"id": 4, "status": "pending"},
  {"id": 5, "status": "failed"}
]
```

Running:

```bash
python task_stats.py tasks.json --status completed
```

should print:

```text
2
```

On success, the application must exit with code `0` and print the number of
matching tasks to `stdout`.

If the input is invalid, the application must exit with code `2` and print an
error message to `stderr`.

### Input File

The provided file must:

* exist;
* contain a valid JSON;
* contain a JSON array as its root element.

Each item in the array must be a **Task** object with the following fields:

* `id`: required; an integer identifier;
* `status`: required; a string containing one of the supported status values.
