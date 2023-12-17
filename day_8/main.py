import itertools

print('--- Day 8: Haunted Wasteland ---')

with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

directions = list(lines[0])
lines.pop(0)
lines.pop(0)

# Parse node data
node_data = {}
for line in lines:
    node, next_node = line.strip().split(' = ')
    left, right = next_node[1:-1].split(', ')
    node_data[node] = {'left': left, 'right': right}

def navigate(node_data, start_node, directions):
    current_node = start_node
    visited_nodes = 0
    cyclic_directions = itertools.cycle(directions)
    for direction in cyclic_directions:
        next_node = node_data[current_node]['left'] if direction == 'L' else node_data[current_node]['right']
        visited_nodes += 1
        current_node = next_node
        if current_node == 'ZZZ':
            break
    return visited_nodes

answer = navigate(node_data, 'AAA', directions)
print(f'Answer: {answer}')
