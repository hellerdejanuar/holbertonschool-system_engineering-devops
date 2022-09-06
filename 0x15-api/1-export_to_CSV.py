#!/usr/bin/python3
"""
    API requests module
    this module fetches data from API
"""


import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    n_tasks_total = 0
    n_tasks_done = 0

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_name = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()['name']

    for task in user_tasks:
        n_tasks_total += 1
        if task['completed'] is True:
            n_tasks_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, n_tasks_done, n_tasks_total))

    for task in user_tasks:
        if task['completed'] is True:
            print("\t {}".format(task['title']))

    # Write data in csv format
    f = open('path/to/csv_file', 'w')
    writer = csv.writer(f)

