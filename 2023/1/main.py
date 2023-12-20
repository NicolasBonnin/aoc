input_file = open('input.txt', 'r')

calibration_values = input_file.readlines()

def find_first_number(string):
    for char in string:
        if char.isdigit():
            return char
    return ""

def resolve_calibration_value(calib):
    numbers_amount = numbers_in_string(calib)
    if numbers_amount == 0:
        return 0
    elif numbers_amount == 1:
        number = find_first_number(calib)
        return number + number
    else:
        return find_first_number(calib) + find_first_number(calib[::-1])

def numbers_in_string(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

total = 0
for calibration in calibration_values:
    total += int(resolve_calibration_value(calibration))
print(total)

