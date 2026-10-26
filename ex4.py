def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    # 1. Read the text the user types
    user_text = input()

    # 2. Split the string into a list of strings at each comma
    text_list = user_text.split(",")

    # 3. Convert each string to a float
    float_list = []
    for item in text_list:
        float_list.append(float(item))

    # 4. Return the list of floats
    return float_list


def calc_average_temperature(temperatures):
    total = sum(temperatures)
    count = len(temperatures)
    average = total / count
    return average


def calc_min_max_temperature(temperatures):
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return [min_temp, max_temp]


def sort_temperature(temperatures):
    print("sort_temperature")


def calc_median_temperature(temperatures):
    print("calc_median_temperature")


# Temporary test calls
display_main_menu()
temperatures = get_user_input()
print("Temperatures:", temperatures)
print("Average:", calc_average_temperature(temperatures))
print("Min and max:", calc_min_max_temperature(temperatures))