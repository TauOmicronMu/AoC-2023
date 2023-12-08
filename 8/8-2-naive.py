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

current_nodes = [node for node in graph.keys() if node[2] == 'A']
current_direction = 0 
steps_taken = 0
with open('8-input-directions.txt', 'r') as f:
    lines = f.readlines() 
    directions = [*lines[0].strip()]
      
    while not all([node[2] == 'Z' for node in current_nodes]):
        if any(node[2] == 'Z' for node in current_nodes):
            print(current_nodes)

        direction = directions[current_direction]

        if direction == 'L':
            current_nodes = [graph[node][0] for node in current_nodes]
        else:
            current_nodes = [graph[node][1] for node in current_nodes]
    
        current_direction += 1
        if current_direction == len(directions):
            current_direction = 0 

        steps_taken += len(current_nodes)
    
print(f'PART TWO: {steps_taken}')
