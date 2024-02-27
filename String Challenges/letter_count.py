"""/****************************************************************
 *             CODERBYTE LETTER COUNT ONE CHALLENGE             *
 *                                                              *
 * Problem Statement                                            *
 * Have the function LetterCountI(str) take the str parameter   *
 * being passed and return the first word with the greatest     *
 * number of repeated letters.                                  *
 * For example: "Today, is the greatest day ever!"              *
 * should return greatest because it has 2 e's (and 2 t's) & it *
 * comes before ever which also has 2 e's. If there are no      *
 * words with repeating letters return -1. Words will be        *
 * separated by spaces.                                         *
 *                                                              *
 * Examples                                                     *
 * Input 1: Hello apple pie                                     *
 * Output 1: Hello                                              *
 *                                                              *
 * Input 2: No words                                            *
 * Output 2: -1                                                 *"""

def LetterCountI(s):
    words = s.split()
    max_repeated_count = 0
    result_word = -1

    for word in words:
        repeated_count = sum(word.count(char) > 1 for char in set(word))
        if repeated_count > max_repeated_count:
            max_repeated_count = repeated_count
            result_word = word

    return result_word

# Example usage:
input_str = "Hello apple pie"
result = LetterCountI(input_str)
print(result)
