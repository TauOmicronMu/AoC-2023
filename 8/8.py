import re

graph = {} 

with open('8-input-graph.txt', 'r') as f:
    lines = f.readlines() 
    
    for line in lines:
        split_line = line.split('=')
        parsed_line = (split_line[0].strip(), split_line[1].strip().split(','))
        parsed_line = (parsed_line[0], [re.sub(r'[()]', '', l).strip() for l in parsed_line[1]]) 

        graph[parsed_line[0]] = parsed_line[1]

graph = dict(sorted(graph.items()))

print(graph)

current_node = 'AAA'
current_direction = 0 
steps_taken = 0
with open('8-input-directions.txt', 'r') as f:
    lines = f.readlines() 
    directions = [*lines[0].strip()]
      
    while current_node != 'ZZZ':
        direction = directions[current_direction]

        if direction == 'L':
            current_node = graph[current_node][0]
        else:
            current_node = graph[current_node][1] 
    
        current_direction += 1
        if current_direction == len(directions):
            current_direction = 0 

        steps_taken += 1 

print(f'PART ONE: {steps_taken}')
