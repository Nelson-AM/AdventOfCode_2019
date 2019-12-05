# Reused from 2018
def load_file_as_list(filename, to_int=None):
    list_from_file = []
    with open(filename) as file:
        for line in file:
            if to_int:
                list_from_file.append(int(line))
            else:
                list_from_file.append(line)
    return list_from_file


def calculate_total_fuel_requirements_modules_only(total_mass):
    total_fuel = 0
    for i in total_mass:
        total_fuel += calculate_fuel_given_mass(i)
    return total_fuel


def calculate_total_fuel_requirements(total_mass):
    total_fuel = 0
    for i in total_mass:
        total_fuel += calculate_total_fuel_for_module(i)
    return total_fuel


def calculate_total_fuel_for_module(module_mass):
    total_fuel_list = [calculate_fuel_given_mass(module_mass)]
    while calculate_fuel_given_mass(total_fuel_list[-1]) > 0:
        total_fuel_list.append(calculate_fuel_given_mass(total_fuel_list[-1]))
    return sum(total_fuel_list)


def calculate_fuel_given_mass(mass):
    return (int(mass / 3)) - 2


if __name__ == "__main__":
    input_file = "Resources/input_day_1"
    input_masses = load_file_as_list(input_file, to_int=True)

    print("Total fuel required: ",
          calculate_total_fuel_requirements(input_masses))
