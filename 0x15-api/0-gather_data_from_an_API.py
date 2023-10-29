#!/usr/bin/python3
"""returns information using REST API"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    url_employee = "{}/users/{}".format(base_url, employee_id)
    response = requests.get(url_employee)
    employee_data = response.json()

    todo_url = "{}/users/{}/todos".format(base_url, employee_id)
    response = requests.get(todo_url)
    tasks = response.json()

    completed_tasks = [task for task in tasks if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_data.get('name'), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
