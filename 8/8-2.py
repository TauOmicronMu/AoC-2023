import re
import math

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

def steps_for_ghost(node):
    current_node = node
    current_direction = 0 
    steps_taken = 0
    with open('8-input-directions.txt', 'r') as f:
        lines = f.readlines() 
        directions = [*lines[0].strip()]
      
        while current_node[2] != 'Z':
            direction = directions[current_direction]

            if direction == 'L':
                current_node = graph[current_node][0]
            else:
                current_node = graph[current_node][1] 
    
            current_direction += 1
            if current_direction == len(directions):
                current_direction = 0 

            steps_taken += 1 

    return steps_taken

starting_nodes = [node for node in graph.keys() if node[2] == 'A']
print(f'STARTING NODES {starting_nodes}')

steps = [steps_for_ghost(node) for node in starting_nodes]
print(f'STEPS: {steps}')

print(f'PART TWO: {math.lcm(*steps)}')
