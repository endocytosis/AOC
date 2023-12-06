def replace_words_with_numbers(s):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    result = ""
    i = 0

    while i < len(s):
        for word in number_map.keys():
            # If a word from the number map is found starting at the current position
            if s[i:].startswith(word):
                # Add the corresponding number to the result
                result += number_map[word]
                # Skip past the word in the string
                i += len(word) - 1
                break
        else:  # This else corresponds to the for-loop
            # If no word was found, add the current character to the result 
            # if it is an int, then move to the next character
            if s[i].isdigit():
                result += s[i]
            i += 1

    return result

# Read lines from the file
with open('day1.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file to get numbers_only array
numbers_only = [replace_words_with_numbers(line.strip()) for line in lines]

# Create a new array with only the first and last digit of each entry in numbers_only
first_last_digits = [int(str(num)[0] + str(num)[-1]) for num in numbers_only]

# Compute the sum of all ints in the new array
total_sum = sum(first_last_digits)

# Output the results
print("Numbers Only:", numbers_only)
print("First and Last Digits:", first_last_digits)
print("Total Sum:", total_sum)
