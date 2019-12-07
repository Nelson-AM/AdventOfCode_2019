import unittest

from Day4.PasswordGenerator import generate_possible_passwords, \
    does_number_have_same_adjacent_digits, does_number_have_decreasing_digits


class MyTestCase(unittest.TestCase):
    def test_number_contains_no_decreasing_digits(self):
        self.assertFalse(does_number_have_decreasing_digits(123456))
        self.assertTrue(does_number_have_decreasing_digits(123454))

    def test_number_contains_same_adjacent_digits(self):
        self.assertFalse(does_number_have_same_adjacent_digits(123456))
        self.assertTrue(does_number_have_same_adjacent_digits(123455))
        self.assertTrue(does_number_have_same_adjacent_digits(111111))

    def test_valid_number_within_range_generated(self):
        self.assertEqual([123455],
                         generate_possible_passwords(123454, 123456))
        self.assertEqual([123455, 123466],
                         generate_possible_passwords(123454, 123467))


if __name__ == '__main__':
    unittest.main()
