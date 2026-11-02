print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

UNDER_WEIGHT = -1
NORMAL_WEIGHT = 0
OVER_WEIGHT = 1


def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight / (height * height)
    print("value of bmi is: ", bmi)

    if bmi < 18.5:
        print("BMI is underweight")
        return UNDER_WEIGHT
    elif bmi <= 25.0:
        print("BMI is normal weight")
        return NORMAL_WEIGHT
    else:
        print("BMI is overweight")
        return OVER_WEIGHT


def display_main_menu():
    print("display main menu")


def get_user_input():
    print("User Inputw")


def main():
    bmi_output = calculate_bmi(weight=57, height=1.73)
    print("Classification code: ", bmi_output)


if __name__ == "__main__":
    main()