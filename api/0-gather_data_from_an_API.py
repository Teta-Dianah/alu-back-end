#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get("name")

    todos = requests.get(f"{base_url}/todos",
                         params={"userId": employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    num_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
