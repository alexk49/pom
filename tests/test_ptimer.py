import unittest

from ptimer.ptimer import updateTime, convertTime, printTime


class TestTimer(unittest.TestCase):
    def test_updateTime(self):
        t = 2
        self.assertEqual(updateTime(t), 1)

    def test_convertTime(self):
        seconds = 65
        self.assertEqual(convertTime(seconds), (1, 5))

    def test_printTime(self):
        mins = 2
        secs = 40
        self.assertEqual(printTime(mins, secs), "02:40")


if __name__ == "__main__":
    unittest.main(verbosity=2)
