import random

# In your code don't directly use numbers, but use this variables.
payoffs = {}
players_guesses = {}
number_of_balls = 100
number_of_players = 5
red_ratio = random.uniform(0, 1)
prize = 20

# This line chooses random players from our class
all_possible_players = ['AHMET', 'CEREN', 'GUL SENA', 'HASAN CAN', 'ABDULLAH','AHMET','AHMET','AHMET','ALI','ALI','ALI','ALP','ARDA','ATA','AYSE','BERFIN','BERKER','BEYZA','BINNAZ','CANAN','CEMRE','DEMET','DENIZ','DENIZ','DENIZ','DILARA','DILARA','DORUK','DUYGU','EBRU','ECE','ECEM','EDA','EGEHAN','EKIN','EMIR','EMIRHAN','EZGI','EZGI','FATMANUR','FURKAN','GAMZE','GAMZE','GOKCE','GONCA','HALIS','ILAYDA','IREM','IREM','IRIS','KAMRAN','KEMAL','KUBRA','LACIN','MAHMUT','MAHSA','MARCO','MEHMET','MELIKE','MELIS','MERT','MEVA','MOHSEN','MUSTAFA','NARINSU','NAZ','PELIN','PIETRO','SELIN','SEYIT','SEYMA','SOZERI','SUNDUZ','TUBA','TUTKU','UMUT','YAGMUR','YAREN','YUSUF','ZEYNEP','ZEYNEP']
players = random.sample(all_possible_players, number_of_players)

# This method is already given to you to show the definiton of game and players in the game.
def print_game():
    print('This is a five-player game played in turns where the players try to \n\
guess if a jar containing blue and red balls has mostly blue or mostly\n\
red balls. If a player’s guess is correct, the player gets 20$. If it \n\
is false, the player gets 0$. ')
    print(f'\nPlayers in the game: \n{", ".join(players)}\nOrder of players has determined randomly. ')

# This method creates and returns jar that contains number_of_balls balls and color ratio is color_ratio.
def create_jar():
    jar = ()
    for i in range(0, number_of_balls):
        if i < (number_of_balls * red_ratio):
            jar += ('red',)
        else:
            jar += ('blue',)
    return jar

# This method gives given jar contains mostly blue or red.
def  jar_contains_mostly():
    if red_ratio <= 0.5:
        return 'blue'
    else:
        return 'red'

# This method informs current player about previous players' choices.
def print_players_guesses():
    for player in players_guesses.keys():
        print(f"{player}'s choice is {players_guesses[player]}")
    print()

#For each player take the player guess as a string
#Make sure that the player enters a valid contribution (allowed inputs just red or blue)
#Inform current player about previous players' choices.
def take_player_inputs(jar):
    print('\n')
    for player in players:
        print_players_guesses()
        ball = random.choice(jar)
        print(f'{player}, your random ball is {ball}')
        guess = input(f'{player} make a guess: ')
        while guess != 'red' and guess != 'blue':
            guess = input(f'{player} make a guess: ')
        players_guesses[player] = guess
        print('\n' * 20)

#This method calculates payoff of each player, keeps it in a dictionary.
def calculate_payoffs():
    for player in players:
        if players_guesses[player] == jar_contains_mostly():
            payoffs[player] = prize
        else:
            payoffs[player] = 0

#This method prints the players' payoffs at the end of program.
def print_payoffs():
    print(f'Since there were more {jar_contains_mostly()} balls, ')
    for player in players:
        print(f'{player} earns ${payoffs[player]}. ')


# Write to a file named payoffs.csv
# Make sure that there is a header line [Indicating the column names, eg. Player, Payoff] 
#   and the lines are ended properly [Hint: put a newline character at the end of each line]
#   and the you close the file.
def save_to_file():
  with open('payoffs.csv', 'w') as payoffs_file:
    header = ','.join(['Player', 'Payoff'])
    payoffs_file.write(header + '\n')
    for player in players:
        str_items = [player, str(payoffs[player])]
        line_str = ', '.join(str_items) + '\n'
        payoffs_file.write(line_str)
    payoffs_file.close()

print_game()
jar = create_jar()
take_player_inputs(jar)
calculate_payoffs()
print_payoffs()
save_to_file()
