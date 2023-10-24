def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def calc_average(numbers):
    average = sum(numbers) / len(numbers)
    print("The average is " + str(average))


def get_user_input():
    a = input()
    y = a.split(", ")
    numbers = list(map(float, y))  # converting str to float
    return numbers


def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    print("Minimum number is " + str(minimum))
    print("Maximum number is " + str(maximum))


def sort_temperature():
    print("sort_temperature")


def calc_median_temperature():
    print("calc_median_temperature")


if __name__ == "__main__":
    display_main_menu()
    number = get_user_input()
    calc_average(number)
    find_min_max(number)
