import random
# In your code don't directly use numbers, but use this variables
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']
payoffs = {}
players_guesses = {}
number_of_balls = 100
red_over_blue_ratio = 0.4
prize = 20


# This method creates and returns jar that contains number_of_balls balls and color ratio is color_ratio.
def create_jar():
    jar = ()
    for i in range(0, number_of_balls):
        if i < (number_of_balls * red_over_blue_ratio):
            jar += ('red',)
        else:
            jar += ('blue',)
    return jar

# This method gives given jar contains mostly blue or red.
def  jar_contains_mostly():
    if red_over_blue_ratio <= 0.5:
        return 'blue'
    else:
        return 'red'

# This method informs current player about previous players' choices.
def print_players_guesses():
    for player in players_guesses.keys():
        print(f"{player}'s choice is {players_guesses[player]}")
    print()


def take_player_inputs(jar):
    random.shuffle(players)
    print('\n' * 20)
    for player in players:
        print_players_guesses()
        ball = random.choice(jar)
        print(f'{player}, your random ball is {ball}')
        guess = input(f'{player} make a guess: ')
        while guess != 'red' and guess != 'blue':
            guess = input(f'{player} make a guess: ')
        players_guesses[player] = guess
        print('\n' * 20)
    players.sort()

def calculate_payoffs():
    for player in players:
        if players_guesses[player] == jar_contains_mostly():
            payoffs[player] = prize
        else:
            payoffs[player] = 0

#This method prints the players' payoffs at the end of program.
def print_payoffs():
    print(f'Since there were more {jar_contains_mostly()} balls,')
    for player in players:
        print(f'{player} earns ${payoffs[player]}.')

# Write to a file named payoffs.csv
# Make sure that there is a header line [Indicating the column names, eg. Player, Payoff] 
#   and the lines are ended properly [Hint: put a newline character at the end of each line]
#   and the you close the file.
def save_to_file():
# Your code starts here
  with open('payoffs.csv', 'w') as payoffs_file:
    header = ','.join(['Player', 'Payoff'])
    payoffs_file.write(header + '\n')
    for player in players:
        str_items = [player, str(payoffs[player])]
        line_str = ', '.join(str_items) + '\n'
        payoffs_file.write(line_str)
    payoffs_file.close()
  # Your code ends here

jar = create_jar()
take_player_inputs(jar)
calculate_payoffs()
print_payoffs()
save_to_file()
