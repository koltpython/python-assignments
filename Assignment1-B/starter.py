import random

print('Welcome to first price auction game!')
print('There are two bidders in this game.')
print('Each bidder (Player A and Player B) is privately assigned a random "valuation" for the item between 1 and 10.')
print('Their randomly assigned values are told to the players (privately).')
print('Players then privately submit their bids for the item.)')
print('Players can bid values in range [0, item\'s valuation] (inclusive).')
print('The winner is announced and also each player\'s payoff is calculated and printed.')

valuation_a = random.randint(1, 10)
valuation_b = random.randint(1, 10)

# Inform valuation for Player A and take her bid

# You need to make sure she entered a valid bid, a value in range [0, valuation_a]
# Continue to ask for new bid until she enters a valid bid


# Clear the console screen after Player A enters her bid.
# There is no easy way of clearing the console on Python
# You can print 20 empty lines to hide Player A's turn

# Inform valuation for Player B and take her bid

# You need to make sure she entered a valid bid, a value in range [0, valuation_b]
# Continue to ask for new bid until she enters a valid bid

# Announce the winner and final payoffs
