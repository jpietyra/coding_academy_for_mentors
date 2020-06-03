# Card number validity can be checked using Luhn algorithm.
# https://en.wikipedia.org/wiki/Luhn_algorithm
#
# Your task is to implement this algorithm.
#
# Write function to validate credit card numbers:
#   def solution(card_number):
#
# Variable card_number will be provided as string (no spaces inside).
# Function should return True for valid card number, and False for invalid.
#
# Sample data:
# Valid card numbers
# 4111111111111111
# 5500000000000004
#
# Invalid card numbers
# 4198786787558765
# 9875787643456354


def solution(card_number):
    sum = 0
    for idx, char in enumerate(card_number[::-1]):
        digit = (idx % 2 + 1) * int(char)
        if digit > 9:
            digit -= 9
        sum += digit
    return sum % 10 == 0
