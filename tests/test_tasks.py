import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import tasks


class TestTasks(unittest.TestCase):
    def test_add(self):
        data = []
        self.assertEqual(tasks.add(data, "a"), 1)
        self.assertEqual(tasks.add(data, "b"), 2)

    def test_done(self):
        data = []
        tasks.add(data, "a")
        self.assertTrue(tasks.mark_done(data, 1))
        self.assertTrue(data[0]["done"])
        self.assertFalse(tasks.mark_done(data, 99))

    def test_delete(self):
        data = []
        tasks.add(data, "a")
        self.assertTrue(tasks.delete(data, 1))
        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()
