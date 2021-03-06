def find_unique_digits(number):
    return set(str(number))


def count_digits_in_number(digit, number):
    list_of_digits = [x for x in str(number) if x == str(digit)]
    return len(list_of_digits)


def does_number_have_decreasing_digits(number_to_test):
    digits = [int(x) for x in str(number_to_test)]
    if sorted(digits) == digits:
        return False
    return True


def does_number_have_double_same_digits(number):
    unique_digits = find_unique_digits(number)
    digit_counts = []
    for i in unique_digits:
        digit_counts.append(count_digits_in_number(i, number))
    if 2 in digit_counts:
        return True
    return False
    # return True if 2 in digit_counts else False
    # print(digit_counts)
    # return True


def generate_possible_passwords(min_val, max_val):
    passwords = []
    for i in range(min_val, max_val + 1):
        if does_number_have_double_same_digits(i) \
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
