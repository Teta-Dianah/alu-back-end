#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            f"{base_url}/users/{employee_id}") as response:
        user = json.loads(response.read().decode())
    employee_name = user.get("name")

    with urllib.request.urlopen(
            f"{base_url}/todos?userId={employee_id}") as response:
        todos = json.loads(response.read().decode())

    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed") is True]
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
