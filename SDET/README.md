# SDET Technical Interview Exercise

## Overview

You are given a small Python CLI application that reads a JSON file and counts tasks with a specified status.

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

The implementation may contain defects. Your tests should be based on the requirements described below rather than on the application's current behavior.

A failing test that correctly identifies a violation of the specification is considered a valid result.

---

## Application

The application is a command-line utility called:

```text
task_stats.py
```

It counts the number of tasks with a particular status in a JSON file.

### Example

Given the following `tasks.json`:

```json
[
  {"id": 1, "status": "completed"},
  {"id": 2, "status": "failed"},
  {"id": 3, "status": "completed"}
]
```

Running:

```bash
python task_stats.py tasks.json --status completed
```

should produce:

```text
2
```

---

## CLI Interface

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

---

## Requirements

### Input File

The provided file must:

* exist;
* contain valid JSON;
* contain a JSON array as its root element.

Each item in the array must represent a task.

A valid task must contain:

* an `id` field;
* a `status` field.

The value of `status` must be one of:

```text
completed
failed
pending
```

---

## Status Matching

The application must count tasks whose `status` **exactly matches** the value passed through `--status`.

For example:

```text
completed
```

and:

```text
Completed
```

are considered different values.

---

## Successful Execution

On success, the application must:

* exit with code `0`;
* print the number of matching tasks to `stdout`.

Example:

```bash
python task_stats.py tasks.json --status failed
```

Output:

```text
1
```

---

## Invalid Input

If the input is invalid, the application must:

* exit with code `2`;
* print an error message to `stderr`.

Invalid input includes, but is not limited to:

* a missing input file;
* malformed JSON;
* a JSON root value that is not an array;
* a task without an `id`;
* a task without a `status`;
* a task with an unsupported status.

---

## Testing Requirements

Use `pytest` to implement your tests.

You may:

* test individual Python functions directly;
* execute the application through `subprocess`;
* use pytest fixtures;
* use parametrized tests;
* create temporary files using pytest utilities such as `tmp_path`.

Your solution must contain **at least one end-to-end test that executes the CLI**.

There is no required number of test cases.

Focus on selecting tests that provide meaningful coverage of the specification rather than maximizing the number of tests.
