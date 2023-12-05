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
            # if it is an int, then move to the next characater
            if s[i].isdigit():
                result += s[i]
            i += 1

    return result

# Test data
test_data = [
    "two1nine",
    "eightwothree",
    "threeightone",
    "three348two"
]

# Process each line in the test data
numbers_only = [replace_words_with_numbers(line) for line in test_data]

# Expected output
print(numbers_only)
