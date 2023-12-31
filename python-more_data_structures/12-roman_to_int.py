#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    result = 0
    for i, c in enumerate(roman_string):
        if i > 0 and roman_dict[c] > roman_dict[roman_string[i - 1]]:
            result += roman_dict[c] - 2 * roman_dict[roman_string[i - 1]]
        else:
            result += roman_dict[c]
    return result
