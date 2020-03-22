import unittest
import rest_api.todo_list.client.client as client

INITIAL_TASKS = [
    {'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False, 'id': 1, 'title': 'Buy groceries'},
    {'description': 'Need to find a good Python tutorial on the web', 'done': False, 'id': 2, 'title': 'Learn Python'}]

NEW_TASK = {'description': 'Opis nowego zadania', 'done': False, 'id': 3, 'title': 'nowe zadanie'}
MODIFIED_TASK = {'description': 'Zmodyfikowany opis nowego zadania', 'done': True,
                 'title': 'zmodyfikowane nowe zadanie'}


class TestTodoApi(unittest.TestCase):

    def test_get_tasks(self):
        tasks = client.get_tasks()
        self.assertEqual(len(tasks), len(INITIAL_TASKS), 'Verify count of tasks on startup')
        self.assertEqual(tasks[0], INITIAL_TASKS[0], 'Verify first initial task')
        self.assertEqual(tasks[1], INITIAL_TASKS[1], 'Verify second initial task')

    def test_get_task(self):
        self.assertEqual(client.get_task(1), INITIAL_TASKS[0], 'Verify first initial task')
        self.assertEqual(client.get_task(2), INITIAL_TASKS[1], 'Verify second initial task')

    def test_add_task(self):
        client.add_task(title=NEW_TASK['title'], description=NEW_TASK['description'])
        tasks = client.get_tasks()
        self.assertEqual(len(tasks), len(INITIAL_TASKS + [NEW_TASK]), 'Verify count of tasks after adding new task')
        self.assertEqual(tasks, INITIAL_TASKS + [NEW_TASK], 'Verify tasks after adding new task')

    def test_modify_task(self):
        client.modify_task(task_id=3, title=MODIFIED_TASK['title'], description=MODIFIED_TASK['description'],
                           done=MODIFIED_TASK['done'])
        tasks = client.get_tasks()
        self.assertEqual(len(tasks), len(INITIAL_TASKS + [MODIFIED_TASK]), 'Verify count of tasks after modifying task')
        self.assertEqual(tasks, INITIAL_TASKS + [MODIFIED_TASK], 'Verify tasks after modifying task')

    def test_delete_task(self):
        client.delete_task(3)
        tasks = client.get_tasks()
        self.assertEqual(len(tasks), len(INITIAL_TASKS), 'Verify count of tasks after removing task')
        self.assertEqual(tasks, INITIAL_TASKS, 'Verify tasks after removing task')


if __name__ == '__main__':
    unittest.main()
