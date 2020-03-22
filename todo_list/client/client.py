import json

import requests


def get_tasks():
    objects = requests.get('http://127.0.0.1:5000/todo/api/tasks')
    return objects.json()['tasks']


def get_task(task_id):
    task = requests.get('http://127.0.0.1:5000/todo/api/tasks/{}'.format(task_id))
    return task.json()['task']


def add_task(title, description=''):
    obj = {'title': title, 'description': description}
    resp = requests.post('http://127.0.0.1:5000/todo/api/tasks', json=obj)
    print(resp.text)


def modify_task(task_id, title=None, description=None, done=False):
    obj = {'done': done}
    if title:
        obj['title'] = title
    if description:
        obj['description'] = description
    headers = {'content-type': 'application/json'}
    resp = requests.put('http://127.0.0.1:5000/todo/api/tasks/{}'.format(task_id), data=json.dumps(obj),
                        headers=headers)
    print(resp.text)


def delete_task(task_id):
    resp = requests.delete('http://127.0.0.1:5000/todo/api/tasks/{}'.format(task_id))
    print(resp.text)

pass