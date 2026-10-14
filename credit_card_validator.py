def has_valid_length(card_number):
    return 13 <= len(card_number) <= 16


def contains_only_digits(card_number):
    return card_number.isdigit()


def get_card_type(card_number):
    if not contains_only_digits(card_number) or not has_valid_length(card_number):
        return "Unknown"
    if card_number.startswith("4"):
        return "Visa"
    if card_number.startswith("5"):
        return "MasterCard"
    if card_number.startswith("37"):
        return "American Express"
    if card_number.startswith("6"):
        return "Discover"
    return "Unknown"


def make_single_digit(number):
    if number < 10:
        return number


def sum_of_doubled_digits(card_number):
    total = 0
    for index in range(len(card_number) - 2, -1, -2):
        digit = int(card_number[index])
        total = total + make_single_digit(digit * 2)
    return total


def sum_of_odd_place_digits(card_number):
    total = 0
    for index in range(len(card_number) - 1, -1, -2):
        digit = int(card_number[index])
        total = total + digit
    return total


def is_valid(card_number):
    if get_card_type(card_number) == "Unknown":
        return False
    total = sum_of_doubled_digits(card_number) + sum_of_odd_place_digits(card_number)
    return total % 10 == 0


def main():
    card_number = input("Hello, kindly enter card number to validate: ").strip()

    print("**Credit Card Type: " + get_card_type(card_number))
    print("**Credit Card Number: " + card_number)
    if is_valid(card_number):
        print("**Credit Card Validity Status: Valid")
    else:
        print("**Credit Card Validity Status: Invalid")

