import unittest

from pt.pt import update_time, convert_time, print_time, convert_input_time


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

    def test_convert_input_time_with_number(self):
        self.assertEqual(convert_input_time("50"), 50)

    def test_convert_input_time(self):
        t = "01:30"
        t_in_secs = 90
        self.assertEqual(convert_input_time(t), t_in_secs)



if __name__ == "__main__":
    unittest.main(verbosity=2)
