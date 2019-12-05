import unittest

from Day3.CrossingWires import find_closest_intersection, \
    find_coordinates_of_changes, parse_string_to_csv_list


class MyTestCase(unittest.TestCase):
    def test_string_is_parsed_to_csv_list(self):
        self.assertEqual(["R8", "U5", "L5", "D3"],
                         parse_string_to_csv_list("R8,U5,L5,D3"))
        self.assertEqual(["U7", "R6", "D4", "L4"],
                         parse_string_to_csv_list("U7,R6,D4,L4"))

    def test_coordinates_of_bends_are_found(self):
        self.assertEqual([[0, 0], [8, 0], [8, 5], [3, 5], [3, 2]],
                         find_coordinates_of_changes("R8,U5,L5,D3"))
        self.assertEqual([[0, 0], [0, 7], [6, 7], [6, 3], [2, 3]],
                         find_coordinates_of_changes("U7,R6,D4,L4"))

    def test_closest_intersection_is_found(self):
        # Crosses at [3, 3] and [6, 5]
        self.assertEqual(6,
                         find_closest_intersection(["R8,U5,L5,D3"],
                                                   ["U7,R6,D4,L4"]))
        self.assertEqual(159,
                         find_closest_intersection(
                             ["R75,D30,R83,U83,L12,D49,R71,U7,L72"],
                             ["U62,R66,U55,R34,D71,R55,D58,R83"]))
        self.assertEqual(135,
                         find_closest_intersection(
                             ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"],
                             ["U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]))


if __name__ == '__main__':
    unittest.main()
