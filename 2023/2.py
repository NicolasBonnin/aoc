import re

input_file = open('resources/input.txt', 'r')

calibration_values = input_file.readlines()

pattern = r'/|1|2|3|4|5|6|7|8|9|one|eno|two|owt|three|eerht|four|ruof|five|evif|six|xis|seven|neves|eight|thgie|nine|enin|/g'


def find_number(string):
    match = re.search(pattern, string)
    if match is None:
        return None
    else:
        return match.group()

def find_second_number(string):
    number = find_number(string)
    ## there is no None check here because we know there is a number in the string
    print(number)
    if not number.isdigit():
        return number[::-1]
    return number

def resolve_calibration_value(calib):
    print(calib)
    first_number = find_number(calib)
    if first_number is None or not first_number:
        return 0
    else:
        return convert_to_number(first_number) + convert_to_number(find_second_number(calib[::-1]))

def convert_to_number(string):
    if string.isdigit():
        return string
    else:
        return {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }[string]

total = 0
for calibration in calibration_values:
    total += int(resolve_calibration_value(calibration.strip()))

print(total)
