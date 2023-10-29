#!/usr/bin/python3
"""Exports task data of an employee to a JSON file"""
import json
import requests
import sys


def get_url(url):
    """Returns the json response of a call to the API.

    Args:
        url: the url to request.
    """
    res = requests.get(url)
    return res.json()


if __name__ == "__main__":
    user_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, user_id)
    user = get_url(user_url)

    task_url = "{}/users/{}/todos".format(base_url, user_id)
    tasks = get_url(task_url)

    task_dicts = [{"task": t.get("title"), "completed": t.get("completed"),
                   "username": user.get("username")} for t in tasks]
    response = {user_id: task_dicts}

    filename = "{}.json".format(user_id)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(response, f)
