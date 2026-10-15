
import os
import tempfile
import unittest
import task_manager as tm


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.old_dir = os.getcwd()
        os.chdir(self.temp.name)
        tm.CSV_FILE = "tasks.csv"
        tm.initialize_csv()

    def tearDown(self):
        os.chdir(self.old_dir)
        self.temp.cleanup()

    def test_add_and_list(self):
        task = tm.add_task("Finish lab", "high")
        self.assertEqual(task["task_id"], "1")
        self.assertEqual(len(tm.list_tasks()), 1)

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            tm.add_task("Finish lab", "urgent")

    def test_update_status(self):
        tm.add_task("Finish lab", "high")
        task = tm.update_status(1, "completed")
        self.assertEqual(task["status"], "completed")

    def test_missing_task(self):
        with self.assertRaises(ValueError):
            tm.update_status(999, "completed")

    def test_summary(self):
        tm.add_task("Task A", "high")
        tm.add_task("Task B", "low")
        tm.update_status(2, "completed")
        self.assertEqual(
            tm.summarize_tasks(),
            {"pending": 1, "completed": 1},
        )


if __name__ == "__main__":
    unittest.main()
