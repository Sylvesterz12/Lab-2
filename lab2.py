print("ET0735 (DevOps fpr AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = " , height)
    print("Weight = " , weight)

    bmi = weight / (height * height)
    print ("value of bmi is: ", bmi)

    if bmi < 18.5:
            print("BMI is underweight")
    elif bmi >= 18.5 and bmi <24.9:
            print("BMI is normal weight")
    else:
        print("BMI is overweight")

    
    return bmi

def display_main_menu():
    print("display main menu")


def get_user_input():
     print("User Inputw")


bmi_output = calculate_bmi(weight=57, height=1.73)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()