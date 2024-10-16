import unittest
import json
import os
import io
import sys
from datetime import datetime
from app import (
    TASKS_FILE,
    load_tasks,
    save_tasks,
    get_next_id,
    add_task,
    update_task,
    delete_task,
    mark_task,
    list_tasks,
)

class TestTaskCLI(unittest.TestCase):
    def setUp(self):
        self.test_tasks = [
            {
                "id": 1,
                "description": "Test task 1",
                "status": "todo",
                "createdAt": "2023-04-01T10:00:00",
                "updatedAt": "2023-04-01T10:00:00"
            },
            {
                "id": 2,
                "description": "Test task 2",
                "status": "in-progress",
                "createdAt": "2023-04-01T11:00:00",
                "updatedAt": "2023-04-01T11:00:00"
            }
        ]
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.test_tasks, f)

    def tearDown(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def test_load_tasks(self):
        tasks = load_tasks()
        self.assertEqual(tasks, self.test_tasks)

    def test_save_tasks(self):
        new_tasks = [{"id": 3, "description": "New task", "status": "todo"}]
        save_tasks(new_tasks)
        with open(TASKS_FILE, 'r') as f:
            saved_tasks = json.load(f)
        self.assertEqual(saved_tasks, new_tasks)

    def test_get_next_id(self):
        next_id = get_next_id(self.test_tasks)
        self.assertEqual(next_id, 3)

    def test_add_task(self):
        add_task("New test task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[-1]["description"], "New test task")
        self.assertEqual(tasks[-1]["status"], "todo")

    def test_update_task(self):
        update_task(1, "Updated test task")
        tasks = load_tasks()
        updated_task = next(task for task in tasks if task["id"] == 1)
        self.assertEqual(updated_task["description"], "Updated test task")

    def test_delete_task(self):
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertFalse(any(task["id"] == 1 for task in tasks))

    def test_mark_task(self):
        mark_task(1, "done")
        tasks = load_tasks()
        marked_task = next(task for task in tasks if task["id"] == 1)
        self.assertEqual(marked_task["status"], "done")

    def test_list_tasks(self):
        # This test is a bit tricky as list_tasks prints to console
        # We'll just check if it runs without errors
        try:
            list_tasks()
            list_tasks("todo")
        except Exception as e:
            self.fail(f"list_tasks raised {type(e).__name__} unexpectedly!")

    def test_task_not_found(self):
        # Test the "Task with ID {task_id} not found" print statement
        non_existent_id = 999
        with io.StringIO() as fake_stdout:
            sys.stdout = fake_stdout
            update_task(non_existent_id, "This task doesn't exist")
            sys.stdout = sys.__stdout__
            self.assertEqual(fake_stdout.getvalue().strip(), f"Task with ID {non_existent_id} not found")
   

if __name__ == '__main__':
    unittest.main()
