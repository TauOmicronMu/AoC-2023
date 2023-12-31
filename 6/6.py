import re
from functools import reduce

def parse_line(line): 
    return [int(x) for x in line.split(":")[1].strip().split()]

def parse_line_smushed(line): 
    return int(''.join(line.split(":")[1].strip().split()))

def get_times(race): 
    return [ (race[0] - i) * i for i in range(race[0])]

with open('6-input.txt', 'r') as f: 
    lines = f.readlines() 
    times = parse_line(lines[0]) 
    distances = parse_line(lines[1])
    races = zip(times, distances)
    times = [(get_times(race), race[1]) for race in races]
   
    margins = [sum([1 for x in time[0] if x > time[1]]) for time in times]
    product = reduce(lambda x, y: x * y, margins) 
    print(f'PART 1: {product}') 

with open('6-input.txt', 'r') as f:
    lines = f.readlines()
    time = parse_line_smushed(lines[0])
    distance = parse_line_smushed(lines[1])
    race = (time, distance)
    times = get_times(race)
    
    margin = sum([1 for time in times if time > distance])
    print(f'PART 2: {margin}') 
