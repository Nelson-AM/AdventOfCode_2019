
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


def manipulate_values(input_array, op_code=None):
    if not op_code:
        op_code = input_array[0]
    index_to_change = input_array[-1]
    if op_code == 1:
        new_value = input_array[1] + input_array[2]
    else:
        new_value = input_array[1] * input_array[2]
    input_array[index_to_change] = new_value
    return input_array


def run_opcodes(input_array):
    for i in range(0, len(input_array), 4):
        op_code = input_array[i]
        if op_code == 99:
            return input_array
        else:
            index_to_change = input_array[i + 3]

            if op_code == 1:
                input_array[index_to_change] = input_array[
                                                   input_array[i + 1]] + \
                                               input_array[input_array[i + 2]]
            elif op_code == 2:
                input_array[index_to_change] = input_array[
                                                   input_array[i + 1]] * \
                                               input_array[input_array[i + 2]]
    return input_array


def initialize_to_1202_state(input_array):
    input_array[1] = 12
    input_array[2] = 2
    return input_array


if __name__ == "__main__":
    input_file = "Resources/input_day_2"
    list_from_file = load_one_line_csv_file_as_list(input_file, to_int=True)
    initialized_list = initialize_to_1202_state(list_from_file)
    op_codes = run_opcodes(initialized_list)
    print("Initial op_code is: ", op_codes[0])
