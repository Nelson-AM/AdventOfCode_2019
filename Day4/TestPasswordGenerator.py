import unittest

from Day4.PasswordGenerator import generate_possible_passwords, \
    does_number_have_double_same_digits, does_number_have_decreasing_digits, \
    count_digits_in_number


class MyTestCase(unittest.TestCase):

    def test_count_digits_in_number(self):
        self.assertEqual(1, count_digits_in_number(4, 1234))
        self.assertEqual(2, count_digits_in_number(4, 12344))

    def test_number_contains_no_decreasing_digits(self):
        self.assertFalse(does_number_have_decreasing_digits(123456))
        self.assertTrue(does_number_have_decreasing_digits(123454))

    def test_number_contains_double_same_digits(self):
        self.assertFalse(does_number_have_double_same_digits(123456))
        self.assertTrue(does_number_have_double_same_digits(123455))
        # self.assertTrue(does_number_have_double_same_digits(111111))

    def test_valid_number_within_range_generated(self):
        self.assertEqual([123455],
                         generate_possible_passwords(123454, 123456))
        self.assertEqual([123455, 123466],
                         generate_possible_passwords(123454, 123467))


if __name__ == '__main__':
    unittest.main()
