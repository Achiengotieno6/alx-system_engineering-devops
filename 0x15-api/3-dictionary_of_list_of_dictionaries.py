#!/usr/bin/python3
"""Exports task data of all employees to a JSON file.
"""
import json
import requests


def get_url(url):
    """Returns the json response of a call to the API.
    """
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(base_url)
    users = get_url(users_url)

    employees_tasks = {}

    for user in users:
        task_url = "{}/users/{}/todos".format(base_url, user.get('id'))
        tasks = get_url(task_url)

        task_dicts = [{"username": user.get("username"),
                       "task": t.get("title"),
                       "completed": t.get("completed")} for t in tasks]

        employees_tasks[user.get('id')] = task_dicts

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(employees_tasks, f)
