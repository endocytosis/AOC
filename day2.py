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

# Reading the file and processing the content
file_path = '/path/to/your/file.txt'  # Replace with your actual file path

with open(day2test.txt, 'r') as file:
    file_content = file.read()

result = process_file(file_content)
print(result)
