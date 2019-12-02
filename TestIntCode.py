import unittest

from IntCode import manipulate_values, run_opcodes


class MyTestCase(unittest.TestCase):
    def test_add_values_to_second_position(self):
        self.assertEqual([1, 1, 2, 3], manipulate_values([1, 1, 2, 3]))
        self.assertEqual([5, 2, 3, 0], manipulate_values([1, 2, 3, 0]))

    def test_multiply_values_to_second_position(self):
        self.assertEqual([2, 1, 2, 2], manipulate_values([2, 1, 2, 3]))
        self.assertEqual([20, 4, 5, 0], manipulate_values([2, 4, 5, 0]))

    def test_small_program_runs_correctly(self):
        self.assertEqual([2, 0, 0, 0, 99], run_opcodes([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], run_opcodes([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801],
                         run_opcodes([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         run_opcodes([1, 1, 1, 4, 99, 5, 6, 0, 99]))


if __name__ == '__main__':
    unittest.main()
