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

## Application Code

```python
import argparse
import json
import sys


ALLOWED_STATUSES = {"completed", "failed", "pending"}


def count_tasks(tasks, status):
    return sum(
        1
        for task in tasks
        if task.get("status", "").lower() == status.lower()
    )


def load_tasks(path):
    with open(path, encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Expected a list")

    for task in tasks:
        if "id" not in task:
            raise ValueError("Missing id")

        status = task.get("status", "pending")

        if status not in ALLOWED_STATUSES:
            raise ValueError("Invalid status")

    return tasks


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")

    parser.add_argument(
        "--status",
        required=True,
        choices=sorted(ALLOWED_STATUSES),
    )

    args = parser.parse_args()

    try:
        tasks = load_tasks(args.file)
        result = count_tasks(tasks, args.status)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 2

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

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

---

## What We Are Looking For

We will primarily evaluate:

* test case selection;
* coverage of positive and negative scenarios;
* handling of edge cases;
* understanding of the specification;
* appropriate use of `pytest`;
* test readability and maintainability;
* assertions that clearly describe expected behavior;
* appropriate separation between unit and end-to-end tests.

You are not expected to build a production-level test framework within the available time.

---

## Submission

Your solution should contain:

```text
task_stats.py
test_task_stats.py
```

Run the tests with:

```bash
pytest -v
```

Some tests may fail because of defects in the provided implementation. This is expected.

Do not change the application solely to make your tests pass.

---

## If You Have Extra Time

If you finish early, consider briefly explaining:

1. Which test cases you consider the most important and why.
2. What additional tests you would add in a production environment.
3. Which parts of the application you would test at the unit level versus through the CLI.
4. How you might change the application design to improve testability.
