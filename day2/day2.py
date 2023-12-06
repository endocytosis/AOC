def parse_color_data(trial):
    """ Parse a trial string into a list of color counts [red, green, blue] """
    # Initialize color counts
    colors = {'red': 0, 'green': 0, 'blue': 0}

    # Split the trial into parts and parse each part
    parts = trial.split(',')
    for part in parts:
   w     part = part.strip()
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

# Reading the file and processing the content
file_path = 'day2.txt'  # The path to the uploaded file

with open(file_path, 'r') as file:
    file_content = file.read()

games_data = process_file(file_content)
adjusted_feasible_games = find_feasible_games_adjusted(games_data)

# Print out the array of feasible game numbers and the resulting sum
print("Feasible Games:", adjusted_feasible_games)
print("Total Number of Feasible Games:", len(adjusted_feasible_games))
print("Sum of the Feasible Game Numbers:", sum(adjusted_feasible_games))