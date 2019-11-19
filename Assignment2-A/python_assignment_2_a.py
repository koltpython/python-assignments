import random

# In your code don't directly use numbers, but use this variables
number_of_players = 4
number_of_rounds = 5
amount_received = 20
rate_of_return = 0.4
contributions = {}
payoffs = {}
# This line chooses random players from our class
all_possible_players = ['AHMET', 'CEREN', 'GUL SENA', 'HASAN CAN', 'ABDULLAH','AHMET','AHMET','AHMET','ALI','ALI','ALI','ALP','ARDA','ATA','AYSE','BERFIN','BERKER','BEYZA','BINNAZ','CANAN','CEMRE','DEMET','DENIZ','DENIZ','DENIZ','DILARA','DILARA','DORUK','DUYGU','EBRU','ECE','ECEM','EDA','EGEHAN','EKIN','EMIR','EMIRHAN','EZGI','EZGI','FATMANUR','FURKAN','GAMZE','GAMZE','GOKCE','GONCA','HALIS','ILAYDA','IREM','IREM','IRIS','KAMRAN','KEMAL','KUBRA','LACIN','MAHMUT','MAHSA','MARCO','MEHMET','MELIKE','MELIS','MERT','MEVA','MOHSEN','MUSTAFA','NARINSU','NAZ','PELIN','PIETRO','SELIN','SEYIT','SEYMA','SOZERI','SUNDUZ','TUBA','TUTKU','UMUT','YAGMUR','YAREN','YUSUF','ZEYNEP','ZEYNEP']
players = random.sample(all_possible_players, number_of_players)

# This method is already given to you to show the players in the game
def print_players_in_the_game():
  print(f'Players in the game: \n{", ".join(players)}')

# This method prints the player contributions and payoffs at each round
def print_player_contributions(round):
    print(f'Each player is given ${amount_received}')
    # Your code starts here
    for player, contribution in contributions.items():
        print(f'{player} contributes ${contribution[round]} to the water purification project.\n\t{player} receives ${amount_received-contribution[round]} payoff.')
    # Your code ends here
    print(f'The group receives a benefit of {calculate_benefit(round)} ')


# Implement a function that calculates the group benefit received each round
def calculate_benefit(round):
    sum_of_contributions = 0
    # Your code starts here
    for contribution in contributions.values():
        sum_of_contributions += contribution[round]#[len(contribution)-1]
    # Your code ends here
    return sum_of_contributions * rate_of_return

# For each round take the player contribution as an integer
# Make sure that the player enters a valid contribution (allowed range: 0 to amount_received)
#   Hint: You may want to protect your program against both ValueError and 
#         KeyError (when you put the initial contribution to the contributions dict)
def take_player_inputs():
  for round in range(number_of_rounds):
      # Your code starts here
      for player in players:
          contribution = int(input(f'Player {player} how much do you like to contribute to the project: '))
          try:
            contributions[player].append(contribution)
          except:
            contributions[player] = [contribution]
          print('\n'*20)
      # Your code ends here
      print_player_contributions(round)
  

# Write to a file named contributions.csv
# Make sure that there is a header line [Indicating the column names, eg. Player, Round] 
#   and the lines are ended properly [Hint: put a newline character at the end of each line]
#   and the you close the file
def save_to_file():
# Your code starts here
  with open('contributions.csv', 'w') as contributions_file:
      header = ','.join(['Player', 'Round', 'Amount Contributed', 'Group Return', 'Payoff'])
      contributions_file.write(header+'\n')
      for round in range(number_of_rounds):
        for player in players:
              str_items = [player, str(round+1), str(contributions[player][round]), str(calculate_benefit(round)), str(calculate_benefit(round)+amount_received-contributions[player][round]),]
              line_str = ','.join(str_items) + '\n'
              contributions_file.write(line_str)
      contributions_file.close()
  # Your code ends here

  
print_players_in_the_game()
take_player_inputs()
save_to_file()