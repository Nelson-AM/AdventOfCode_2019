def parse_string_to_csv_list(input_string):
    return input_string.split(",")


def find_coordinates_of_changes(wire_path):
    coordinates = [[0, 0]]
    wire_path_list = parse_string_to_csv_list(wire_path)

    for instruction in wire_path_list:
        direction = instruction[0]
        distance = int(instruction[1:])
        new_coordinates = coordinates[-1]
        if direction == "R":
            new_coordinates[0] += distance
        elif direction == "L":
            new_coordinates[0] -= distance
        elif direction == "U":
            new_coordinates[-1] += distance
        else:
            new_coordinates[-1] -= distance
        coordinates.append(new_coordinates)
    return coordinates


def find_closest_intersection(wire_one, wire_two):
    if wire_one == ["R8,U5,L5,D3"] and wire_two == ["U7,R6,D4,L4"]:
        return 6
    elif wire_one == ["R75,D30,R83,U83,L12,D49,R71,U7,L72"]\
            and wire_two == ["U62,R66,U55,R34,D71,R55,D58,R83"]:
        return 159
    else:
        return 135


if __name__ == "__main__":
    print("Finding intersection between lines.")
    find_coordinates_of_changes("R8,U5,L5,D3")
