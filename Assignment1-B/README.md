# Assignment 1 - First Price Auction Game

**Due: 11:59 PM, Monday, November 4, 2019**

## Introduction

The assignments in KOLT Python Course are not going to be graded, but detailed feedback will be provided. This means that you don't have to ace the task; however, in order for you to get a certificate at the end of the program, we need to be convinced that you **did your best**.

Please don't see these assignments as regular class assignments. The main purpose of them is to get you practice what you have learned so far. Don't forget:

> **_You cannot learn coding if you don't get your hands dirty._**

## Instructions

You need to create a game for this assignment. There is a specific item that will be sold by auction. There are two bidders in the game, we call them Player A and Player B. The highest bidder wins the auction. The winner gets his valuation minus his bid as payoff. The loser does not get a payoff. You create the game as follows:

You need to create a game for this assignment. There is a specific item that will be sold by auction. There are <ins>**two bidders**</ins> in the game, we call them **_Player A_** and **_Player B_**. The highest bidder wins the auction. The winner gets his valuation minus his bid as payoff. The loser does not get a payoff. You create the game as follows:

- Each player (_Players A_ and _B_) is privately assigned a random "valuation" for the item between 1 and 10. This is how much they value the item.
- Players are informed about what their valuation is. They do not know the other bidder's valuation.
- Players then submit their bids for the item.
- The player who submitted the highest bid wins the item. He gets his valuation minus his bid as payoff.
- The player who submitted the lower bid gets a payoff of zero.
- The winner is announced and also each player's payoff is calculated and printed.

## Example Game

To see a working demo, visit [here](https://koltpython.github.io/assignments/demo/mayonnaise).

- _Player A_ is assigned a random valuation of 5, and _Player B_ is assigned a random valuation of 6 for the auctioned item.
- Their randomly assigned values are told to the players (privately).
- Players submit their bids for the item. For example, _Player A_ has a prize value of 5, so he can bid 0, 1, 2, 3, 4, 5. Likewise, _Player B_ can bid 0, 1, 2, 3, 4, 5, 6.
- Suppose _Player A_ bids 4 and _Player B_ bids 2. _Player A_ wins.
- _Player A_ pays 4 for an item that has a prize value of 5. Therefore, _Player A_'s final payoff is 5-4=1. _Player B_'s final payoff is 0.
