def does_number_have_decreasing_digits(number_to_test):
    str_number = str(number_to_test)
    for a, b in zip(str_number[:-1], str_number[1:]):
        if a > b:
            return True
    return False


def does_number_have_same_adjacent_digits(number_to_test):
    str_number = str(number_to_test)
    for a, b in zip(str_number[:-1], str_number[1:]):
        if a == b:
            return True
    return False


def generate_possible_passwords(min_val, max_val):
    passwords = []
    for i in range(min_val, max_val + 1):
        if does_number_have_same_adjacent_digits(i) \
                and not does_number_have_decreasing_digits(i):
            passwords.append(i)
    return passwords


if __name__ == "__main__":
    min_value = 138241
    max_value = 674034
    print("Generating potential passwords in range: {}, {}.".format(min_value,
                                                                    max_value))

    list_of_passwords = generate_possible_passwords(min_value, max_value)
    print("Number of potential passwords: {}.".format(len(list_of_passwords)))
