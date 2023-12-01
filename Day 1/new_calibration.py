import re

def calibration(line):
    nums = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    digit_1 = nums[0]
    try:
        digit_1 = int(digit_1)
    except:
        if digit_1 == "one":
            digit_1 = 1
        elif digit_1 == "two":
            digit_1 = 2
        elif digit_1 == "three":
            digit_1 = 3
        elif digit_1 == "four":
            digit_1 = 4
        elif digit_1 == "five":
            digit_1 = 5
        elif digit_1 == "six":
            digit_1 = 6
        elif digit_1 == "seven":
            digit_1 = 7
        elif digit_1 == "eight":
            digit_1 = 8
        elif digit_1 == "nine":
            digit_1 = 9
    digit_1 = digit_1*10
    digit_2 = nums[-1]
    try:
        digit_2 = int(digit_2)
    except:
        if digit_2 == "one":
            digit_2 = 1
        elif digit_2 == "two":
            digit_2 = 2
        elif digit_2 == "three":
            digit_2 = 3
        elif digit_2 == "four":
            digit_2 = 4
        elif digit_2 == "five":
            digit_2 = 5
        elif digit_2 == "six":
            digit_2 = 6
        elif digit_2 == "seven":
            digit_2 = 7
        elif digit_2 == "eight":
            digit_2 = 8
        elif digit_2 == "nine":
            digit_2 = 9
    return digit_1 + digit_2