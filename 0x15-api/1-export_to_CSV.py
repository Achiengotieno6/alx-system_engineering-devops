#!/usr/bin/python3
"""returns information using REST API and exports data in CSV format"""
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
    # Get user ID from command ine argument
    user_id = sys.argv[1]

    # base URL for API
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, user_id)
    user = get_url(user_url)

    task_url = "{}/users/{}/todos".format(base_url, user_id)
    tasks = get_url(task_url)
    # define CSV filename based on user ID
    filename = "{}.csv".format(user_id)
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            line = '"{}","{}","{}","{}"\n'.format(user_id,
                                                  user.get('username'),
                                                  task.get('completed'),
                                                  task.get('title'))
            f.write(line)
