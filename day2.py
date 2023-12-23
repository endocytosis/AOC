def parse_color_data(trial):
    """ Parse a trial string into a list of color counts [red, green, blue] """
    # Initialize color counts
    colors = {'red': 0, 'green': 0, 'blue': 0}

    # Split the trial into parts and parse each part
    parts = trial.split(',')
    for part in parts:
        part = part.strip()
        if part:
            number, color = part.split()
            colors[color] = int(number)

    return [colors['red'], colors['green'], colors['blue']]

def process_file(content):
    """ Process the file content and return the multi-dimensional array """
    lines = content.strip().split('\n')

    games_data = []
    for line in lines:
        # Remove the game number and colon
        game_data = line.split(': ')[1]
        # Split into trials
        game_trials = game_data.split(';')
        # Parse each trial
        parsed_trials = [parse_color_data(trial) for trial in game_trials]
        games_data.append(parsed_trials)

    return games_data

def find_feasible_games_adjusted(games_data):
    """ Find and return the numbers of games that are feasible with the given cube limits per trial """
    feasible_games = []
    for game_index, game in enumerate(games_data, start=1):
        # Check each trial in the game
        for trial in game:
            red, green, blue = trial
            # If any color in a trial exceeds the limits, break and move to the next game
            if red > 12 or green > 13 or blue > 14:
                break
        else:
            # If no trial exceeded the limits, add the game as feasible
            feasible_games.append(game_index)

    return feasible_games

#Fewest cubes 
#Loop through the array, temp variable for each color (RGB) initally set to zero, update if color at 
#next index is greater
#Store these values in a min_cubes array
#Power_set function: iterate through min_cubes array, calculate product for each trial, then sum

def find_fewest_cubes(games_data):
    #Fewest cubes array
    fewest_cubes = []
    for game_index, game in enumerate(games_data, start=1):
        #Increase the size of the array by 1 for each game, set intial value to zero
        fewest_cubes.append(0)
        temp_red = 0 
        temp_green = 0
        temp_blue = 0
        max_power = 0 
        for trial in game:
            red, green, blue = trial
            if red > temp_red:
                temp_red = red
            if green > temp_green:
                temp_green = green
            if blue > temp_blue:
                temp_blue = blue
            power = temp_blue * temp_red * temp_green
            #If current power greater than max power, update current game index with this power
            if power > max_power:
                max_power = power
                fewest_cubes[game_index - 1] = max_power
            print("The game index is", game_index)
            print("Max power is", max_power)
            print("The current max red is", temp_red)
            print("The current max green is", temp_green)
            print("The current max blue is", temp_blue)
    return fewest_cubes
# Reading the file and processing the content
file_path = 'day2.txt'  # The path to the uploaded file

with open(file_path, 'r') as file:
    file_content = file.read()

games_data = process_file(file_content)
adjusted_feasible_games = find_feasible_games_adjusted(games_data)
fewest_cubes = find_fewest_cubes(games_data)

# Print out the array of feasible game numbers and the resulting sum
print("Feasible Games:", adjusted_feasible_games)
print("Total Number of Feasible Games:", len(adjusted_feasible_games))
print("Sum of the Feasible Game Numbers:", sum(adjusted_feasible_games))
print("The fewest cubes are", fewest_cubes)
print("The sum of the fewest cubes is", sum(fewest_cubes))
print("This is a the final test output")