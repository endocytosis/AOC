import ast

instructions_text = 'LRRRLRRLRLRRRLRLLLLRRRLRLRRLRLRLRRLRRRLRRLRRRLRLLLRRLRRLRRLRRLRRLLLLLRLRLRRRLRLLRRLRLRRRLRRLRRRLLLRRLRRLRRLRRRLRLRLRRLLRRRLRRLRRRLRRRLRRRLRLRRLRRLRRLRRRLRLRRLRRLLRRRLRRLRRLRRRLRLRLRRLLRRRLLRRLRRRLRRRLRLRRLLRRRLRLRRLLRRLRLRRRLRLRRRLRRLRRLRRLRRRLRRRLRLLRRLRRLLRRLRRRLRRLRLRLRRRLLLRRLRLRRLRRLRLRLLRLRRLRLRLRRRR'
#Parse instructions_text as a list, instructions
instructions = []
for i in range(len(instructions_text)):
    instructions.append(instructions_text[i])

# Initialize an empty dictionary
network_data = {}

# Open the file and read its contents
with open('day8test.txt', 'r') as file:
    for line in file:
        # Split the line into key and value parts
        key, value = line.split('=')
        # Remove whitespace and parentheses from key and value
        key = key.strip()
        value = value.strip().strip('()')
        # Split the value part into individual elements
        values = value.split(',')
        # Add the processed key and value to the dictionary
        network_data[key] = [v.strip() for v in values]

def steps_to_end(start_key, instructions, data):
    current_key = start_key
    steps = 0
    i = 0  # Instruction index

    while current_key != 'ZZZ':
        # Determine next key based on current instruction
        next_key = data[current_key][0 if instructions[i] == 'L' else 1]
        
        # Update the current key and steps
        current_key = next_key
        steps += 1
        print(steps)

        # Move to the next instruction, wrap around if necessary
        i = (i + 1) % len(instructions)

    return steps

start = 'AAA'

print(instructions)
print(network_data)
print(steps_to_end(start, instructions, network_data))