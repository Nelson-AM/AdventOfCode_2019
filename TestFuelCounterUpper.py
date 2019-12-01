import unittest

from FuelCounterUpper import calculate_fuel_given_mass, \
    load_file_as_list, calculate_total_fuel_requirements_modules_only, \
    calculate_total_fuel_for_module, calculate_total_fuel_requirements


class MyTestCase(unittest.TestCase):
    def test_load_file_as_list_returns_list_from_valid_filename(self):
        valid_filename = "Resources/input_day_1"
        self.assertTrue(isinstance(load_file_as_list(valid_filename), list))

    def test_load_file_as_list_fails_when_file_not_found(self):
        invalid_filename = "Resources/input_day_0"
        self.assertRaises(FileNotFoundError,
                          load_file_as_list, invalid_filename)

    def test_calculate_fuel_requirement_returns_correct_value(self):
        self.assertEqual(calculate_fuel_given_mass(12), 2)
        self.assertEqual(calculate_fuel_given_mass(14), 2)
        self.assertEqual(calculate_fuel_given_mass(1969), 654)
        self.assertEqual(calculate_fuel_given_mass(100756), 33583)

    def test_calculate_total_fuel_req_per_module(self):
        self.assertEqual(2, calculate_total_fuel_for_module(14))
        self.assertEqual(966, calculate_total_fuel_for_module(1969))
        self.assertEqual(50346, calculate_total_fuel_for_module(100756))

    def test_calculate_total_fuel_required_returns_correct_value(self):
        self.assertEqual(2, calculate_total_fuel_requirements([12]))
        self.assertEqual(2 + 2, calculate_total_fuel_requirements([12, 14]))
        self.assertEqual(2 + 2 + 966,
                         calculate_total_fuel_requirements([12, 14, 1969]))
        self.assertEqual(2 + 2 + 966 + 50346,
                         calculate_total_fuel_requirements(
                             [12, 14, 1969, 100756]))

    def test_calculate_total_fuel_req_mod_only_returns_correct_value(self):
        self.assertEqual(2, calculate_total_fuel_requirements_modules_only(
            [12]))
        self.assertEqual(2 + 2,
                         calculate_total_fuel_requirements_modules_only(
                             [12, 14]))
        self.assertEqual(2 + 2 + 654,
                         calculate_total_fuel_requirements_modules_only(
                             [12, 14, 1969]))
        self.assertEqual(2 + 2 + 654 + 33583,
                         calculate_total_fuel_requirements_modules_only(
                             [12, 14, 1969, 100756]))


if __name__ == '__main__':
    unittest.main()
