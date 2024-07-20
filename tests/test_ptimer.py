import unittest

from ptimer.ptimer import update_time, convert_time, print_time


class TestTimer(unittest.TestCase):
    def test_update_time(self):
        t = 2
        self.assertEqual(update_time(t), 1)

    def test_convert_time(self):
        seconds = 65
        self.assertEqual(convert_time(seconds), (1, 5))

    def test_print_time(self):
        mins = 2
        secs = 40
        self.assertEqual(print_time(mins, secs), "02:40")


if __name__ == "__main__":
    unittest.main(verbosity=2)
