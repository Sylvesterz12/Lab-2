def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():

    user_text = input()
    text_list = user_text.split(",")

    float_list = []
    for item in text_list:
        float_list.append(float(item))

    return float_list


def calc_average(temperatures):
    total = sum(temperatures)
    average = total / len(temperatures)
    return average


def find_min_max(temperatures):
    minimum = min(temperatures)
    maximum = max(temperatures)
    return minimum, maximum


def sort_temperature(temperatures):
    sorted_list = sorted(temperatures)
    return sorted_list


def calc_median_temperature(temperatures):
    sorted_list = sort_temperature(temperatures)
    n = len(sorted_list)
    middle = n // 2

    if n % 2 == 1:
        # Odd count: middle value
        return sorted_list[middle]
    else:
        # Even count: average of the two middle values
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2


def main():
    display_main_menu()
    temperatures = get_user_input()
    print(temperatures)
    print("Average:", calc_average(temperatures))
    print("Min/Max:", find_min_max(temperatures))
    print("Median:", calc_median_temperature(temperatures))


if __name__ == "__main__":
    main()