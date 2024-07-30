import os
import unittest

from pom.timers import Timer


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = Timer()

    def test_init(self):
        # defaults
        self.assertFalse(self.timer.pause)
        self.assertFalse(self.timer.sound_on_finish)
        self.assertEqual(self.timer.time_string, "00:00")
        self.assertEqual(self.timer.time, 0)

    def test_convert_input_time(self):
        test_val = "01:05"
        expected_res = 65
        self.assertEqual(self.timer.convert_input_time(test_val), expected_res)

    def test_start_countdown(self):
        """Sets single second timer
        which should increment down to -1
        """
        self.timer.time = 1
        self.timer.start_countdown()
        self.assertEqual(self.timer.time, -1)

    def test_check_for_sound_does_nothing(self):
        self.timer.sound_on_finish = False
        self.timer.check_for_sound()
        self.assertFalse(self.timer.sound_on_finish)

    def test_convert_time(self):
        self.timer.time = 65
        mins, secs = self.timer.convert_time()
        self.assertEqual(mins, 1)
        self.assertEqual(secs, 5)

    def test_update_time_string(self):
        self.timer.update_time_string(0, 20)
        self.assertEqual(self.timer.time_string, "00:20")

    def test_update_time(self):
        self.timer.time = 20
        self.timer.update_time()
        self.assertEqual(self.timer.time, 19)


if __name__ == "__main__":
    unittest.main()
