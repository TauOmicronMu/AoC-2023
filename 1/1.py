import re
import itertools

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

portmanteaus = [(f'{x}{y[1:]}', f'{x}{y}') for (x, y) in itertools.product(digits.keys(), digits.keys()) if x[-1] == y[0]]

def get_calibration_values(lines): 
    return [int(f'{x}{x}') if len(x) == 1 else int(f'{x[0]}{x[-1]}') for x in lines]

def remove_portmanteau(line): 
    for p in portmanteaus:
        line = re.sub(p[0], p[1], line)
    return line

#  Part 1 
with open('1-input.txt', 'r') as f:
    lines = f.readlines(); 
    strp_lines = [re.sub('\D', '', line) for line in lines]
    calibration_vals = get_calibration_values(strp_lines)
    print(f'PART 1: {sum(calibration_vals)}')

#  Part 2
with open('1-input.txt', 'r') as f:
    lines = f.readlines(); 
    no_portmanteau_lines = [remove_portmanteau(line) for line in lines]
    lowercase_lines = [line.lower() for line in no_portmanteau_lines]
    for digit in digits.keys():
        lowercase_lines = [re.sub(digit, digits[digit], line) for line in lowercase_lines]
    strp_lines = [re.sub('\D', '', line) for line in lowercase_lines]
    calibration_vals = get_calibration_values(strp_lines) 
    print(f'PART 2: {sum(calibration_vals)}')
