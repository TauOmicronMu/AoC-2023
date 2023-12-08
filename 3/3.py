adj_coords = [(x,y) for x in [-1, 0, 1] for y in [-1, 0, 1]]

def is_symbol(char):
    return char != '.' and not char.isdigit()

def is_adjacent(grid, row, col, check):
    is_adj = False 
    for coord in adj_coords: 
        try: 
            is_adj = is_adj or check(grid[row + coord[0]][col + coord[1]])
        except:
            continue 
    return is_adj

def coords_to_num(grid, coords):
    num_str = "" 
    for coord in coords:
        num_str += grid[coord[0]][coord[1]]
    return int(num_str)
    
def get_number_from_row(row, row_i, start):
    number = [] 
    i = start

    while i < len(row) and row[i].isdigit():
        number.append((row_i, i))
        i += 1
 
    return number 

def get_numbers_from_row(row, row_i): 
    numbers = []

    for i in range(len(row)):
        char = row[i] 
        if not char.isdigit():
            continue 
        if i == 0:
            numbers.append(get_number_from_row(row, row_i, i))
            continue 
        if i == len(row) - 1 and not row[i - 1].isdigit():
            numbers.append([(row_i, i)]) 
            continue 
        if not row[i-1].isdigit():
            numbers.append(get_number_from_row(row, row_i, i))

    return numbers 

def get_gears_from_row(grid, row, row_i, part_number_coords): 
    gears = [] 
    for i in range(len(row)): 
        char = row[i]
        if not char == '*':
            continue 
        adjacents = [(row_i + row, i + col) for (row, col) in adj_coords] 
        adj_part_coords = [number for number in part_number_coords if any([adj_coord in number for adj_coord in adjacents])]
        if len(adj_part_coords) == 2: 
            adj_part_numbers = [coords_to_num(grid, coord) for coord in adj_part_coords]
            ratio = adj_part_numbers[0] * adj_part_numbers[1]
            gears.append((row_i, i, ratio))
    return gears 


with open('3-input.txt', 'r') as f:
    lines = f.readlines() 
    split_lines = [[*line.strip()] for line in lines]
    numbers = []
    for row in split_lines:
        numbers += get_numbers_from_row(row, split_lines.index(row))

    part_number_coords = [number for number in numbers if any([is_adjacent(split_lines, row, col, is_symbol) for (row, col) in number])]
    part_numbers = [coords_to_num(split_lines, coords) for coords in part_number_coords] 
    print(part_numbers)
    print(f'PART 1: {sum(part_numbers)}')
    
    gears = []
    for row in split_lines: 
        gears += get_gears_from_row(split_lines, row, split_lines.index(row), part_number_coords)

    print(f'PART 2: {sum([ratio for (row, col, ratio) in gears])}')

