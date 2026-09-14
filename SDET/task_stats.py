import argparse
import json
import sys


ALLOWED_STATUSES = {"completed", "failed", "pending"}


def count_tasks(tasks, status):
    return sum(
        1
        for task in tasks
        if task.get("status") == status
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

        if not isinstance(status, str):
            raise ValueError("Invalid status")

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
    
