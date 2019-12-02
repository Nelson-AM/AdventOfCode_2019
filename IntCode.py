
def load_one_line_csv_file_as_list(filename, to_int=None):
    with open(filename) as file:
        for line in file:
            current_line = line.split(",")

        if to_int:
            int_list = []
            for i in current_line:
                int_list.append(int(i))
            current_line = int_list
    return current_line


def manipulate_values(input_list, op_code=None):
    if not op_code:
        op_code = input_list[0]
    index_to_change = input_list[-1]
    if op_code == 1:
        new_value = input_list[1] + input_list[2]
    else:
        new_value = input_list[1] * input_list[2]
    input_list[index_to_change] = new_value
    return input_list


def run_opcodes(input_list):
    for i in range(0, len(input_list), 4):
        op_code = input_list[i]
        if op_code == 99:
            return input_list
        else:
            index_to_change = input_list[i + 3]

            if op_code == 1:
                input_list[index_to_change] = input_list[
                                                   input_list[i + 1]] + \
                                              input_list[input_list[i + 2]]
            elif op_code == 2:
                input_list[index_to_change] = input_list[
                                                   input_list[i + 1]] * \
                                              input_list[input_list[i + 2]]
    return input_list


def initialize_to_state(input_list, noun, verb):
    input_list[1] = noun
    input_list[2] = verb
    return input_list


def calculate_puzzle_output(noun, verb):
    return 100 * noun + verb


def find_output_for_target_value(values_to_check, target):
    for output_values in values_to_check:
        if output_values[0] == target:
            return calculate_puzzle_output(output_values[1], output_values[2])


def cycle_through_instruction_values(filename, target):
    output_to_check = []
    for i in range(0, 99):
        for j in range(0, 99):
            list_from_file = load_one_line_csv_file_as_list(filename,
                                                            to_int=True)
            initialized = initialize_to_state(list_from_file, i, j)
            output_list = run_opcodes(initialized)
            output_to_check.append([output_list[0], i, j])
    return find_output_for_target_value(output_to_check, target)


if __name__ == "__main__":
    input_file = "Resources/input_day_2"
    target_value = 19690720

    puzzle_output = cycle_through_instruction_values(input_file, target_value)

    print("Puzzle output: ", puzzle_output)
