#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    employee_name = user.get("name")

    todos = requests.get("{}/todos?userId={}".format(
        url, employee_id)).json()

    done = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done), len(todos)))

    for task in done:
        print("\t {}".format(task.get("title")))
