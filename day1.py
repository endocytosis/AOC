#Open text file and store each row as an array entry
with open('day1.txt', 'r') as file:
    document = [line.strip() for line in file]

#List comprehension creates two lists
#One containing the first digit [char for char in line if char.isdigit()][:1] 
#The other containing the last digit [char for char in line if char.isdigit()][-1:]
#Lists are concatenated and joined into a string, string conveted to int 
#Result is 1D array where each entry is the first and last digit of each line

first_two_digits = [
    int(''.join([char for char in line if char.isdigit()][:1] + [char for char in line if char.isdigit()][-1:]))
    for line in document
]
print(first_two_digits)
#List comprehension to collapse 2D array into 1D array
total_sum = sum(first_two_digits)
print(total_sum)

