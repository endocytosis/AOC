#Open text file and store each row as an array entry
with open('day1test.txt', 'r') as file:
    document = [line.strip() for line in file]

print(document)

#List comprehension creates two lists
#One containing the first digit [char for char in line if char.isdigit()][:1] 
#The other containing the last digit [char for char in line if char.isdigit()][-1:]
#Lists are concatenated and joined into a string, string converted to int 
#Result is 1D array where each entry is the first and last digit of each line

#Part II: Your calculation isn't quite right. It looks like some of the digits 
#are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
#also count as valid "digits".

#Parse each line and search for words, convert to int
#Then proceed as before

#Dictionary
def replace_spelled_numbers(text):
    # Dictionary mapping spelled numbers to their numeric values
    number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # Replace each spelled number with its numeric value
    for spelled, number in number_dict.items():
        text = text.replace(spelled, number)
    
    return text

#Replace spelled number for list function
def replace_spelled_numbers_in_list(strings):
    # Reuse the previously defined function for each string in the list
    return [replace_spelled_numbers(string) for string in strings]

text_as_int = replace_spelled_numbers_in_list(document)
print(text_as_int)


first_last_digits = [
    int(''.join([char for char in line if char.isdigit()][:1] + [char for char in line if char.isdigit()][-1:]))
    for line in text_as_int
]
print(first_last_digits)
#List comprehension to collapse 2D array into 1D array
print(sum(first_last_digits))


