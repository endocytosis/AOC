def shift_dots_upwards(array):
    rows = len(array)
    cols = len(array[0])

    # Iterating through each element in the array
    for row in range(1, rows):  # Starting from the second row
        for col in range(cols):
            # If the current element is 'O', look above it
            if array[row][col] == 'O':
                current_row = row
                # While there is a dot above the 'O', shift it up
                while current_row > 0 and array[current_row - 1][col] == '.':
                    # Swap the 'O' and '.'
                    array[current_row][col], array[current_row - 1][col] = array[current_row - 1][col], array[current_row][col]
                    current_row -= 1
    return array

def parse_file_to_array(file_path):
    with open(file_path, 'r') as file:
        # Reading lines from the file
        lines = file.readlines()
        # Removing any leading/trailing whitespace including newlines
        lines = [line.strip() for line in lines]
        # Converting each line into a list of characters
        multi_dim_array = [list(line) for line in lines]
        return multi_dim_array

def calculate_total_load(array):
    total_load = 0
    rows = len(array)

    for row_index, row in enumerate(array):
        load_per_row = rows - row_index  # Load for each 'O' in this row
        total_load += row.count('O') * load_per_row

    return total_load

# Path to your file
file_path = 'day14.txt'

# Reading the array from the file
array_from_file = parse_file_to_array(file_path)

# Applying the transformation
transformed_array = shift_dots_upwards(array_from_file)

# Calculating the total load
total_load = calculate_total_load(transformed_array)

# Printing the transformed array, total load, and writing the transformed array back to the file
with open(file_path, 'w') as file:
    for row in transformed_array:
        line = "".join(row)
        print(line)
        file.write(line + "\n")

# Printing the total load
print("Total Load:", total_load)
