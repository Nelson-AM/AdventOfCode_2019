from Day1.FuelCounterUpper import load_file_as_list


def parse_string_to_csv_list(input_string):
    return input_string.split(",")


def find_full_path_of_wire(wire_instructions):
    wire_path_list = parse_string_to_csv_list(wire_instructions)

    full_path = [[0, 0]]

    for instruction in wire_path_list:
        for i in range(int(instruction[1:])):
            full_path = update_path(full_path, instruction[0])
    return full_path[1:]


def update_path(full_path, direction):
    new_path = []
    coordinate = full_path[-1]
    if direction == "R":
        new_path = full_path + [[coordinate[0] + 1, coordinate[1]]]
    elif direction == "L":
        new_path = full_path + [[coordinate[0] - 1, coordinate[1]]]
    elif direction == "U":
        new_path = full_path + [[coordinate[0], coordinate[1] + 1]]
    elif direction == "D":
        new_path = full_path + [[coordinate[0], coordinate[1] - 1]]
    else:
        print("This state should not be reachable.")
    return new_path


def find_intersections(path_one, path_two):
    return [value for value in path_one if value in path_two]


def calculate_manhattan_distances(intersections):
    return [abs(value[0]) + abs(value[1]) for value in intersections]


def find_closest_intersection(wire_one, wire_two):
    path_one = find_full_path_of_wire(wire_one)
    path_two = find_full_path_of_wire(wire_two)

    intersections = find_intersections(path_one, path_two)
    # print(intersections)
    manhattan_distances = calculate_manhattan_distances(intersections)
    return min(manhattan_distances)


if __name__ == "__main__":
    filename = "Resources/input_day_3.txt"
    list_from_file = load_file_as_list(filename, to_int=False)
    closest_intersection = find_closest_intersection(list_from_file[0],
                                                     list_from_file[1])
    print("Closest intersection: ", closest_intersection)
