"""
 * Problem Statement                                            *
 * Have the function BasicRomanNumerals(str) read str which     *
 * will be a string of Roman numerals. The numerals being used  *
 * are: I for 1, V for 5, X for 10, L for 50, C for 100, D for  *
 * 500 and M for 1000. In Roman numerals, to create a number    *
 * like 11 you simply add a 1 after the 10, so you get XI. But  *
 * to create a number like 19, you use the subtraction notation *
 * which is to add an I before an X or V (or add an X before    *
 * an L or C). So 19 in Roman numerals is XIX.                  *
 *                                                              *
 * The goal of your program is to return the decimal equivalent *
 * of the Roman numeral given. For example: if str is "XXIV"    *
 * your program should return 24                                *
"""

def roman_to_int(roman):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    count = 0
    prev_value = 0  
    for char in roman:
        current_value = a[char]     
        if current_value > prev_value:
            count += current_value - 2 * prev_value
        else:
            count += current_value
        prev_value = current_value
    return count

print(roman_to_int("IV"))  # Output: 4
print(roman_to_int("XIV")) # Output: 14
print(roman_to_int("MX"))  # Output: 1010
