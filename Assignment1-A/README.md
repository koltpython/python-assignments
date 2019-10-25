# Assignment 1 - The Ultimatum Bargaining

**Due: 11:59 PM, Monday, November 4, 2019**

## Introduction

The assignments in KOLT Python Course are not going to be graded, but detailed feedback will be provided. This means that you don't have to ace the task; however, in order for you to get a certificate at the end of the program, we need to be convinced that you **did your best**.

Please don't see these assignments as regular class assignments. The main purpose of them is to get you practice what you have learned so far. Don't forget:

> **_You cannot learn coding if you don't get your hands dirty._**

## Instructions

You need to create a game for this assignment. This is a two-player game played in turns. One of the players is the **_Proposer_** and the other one is the **_Responder_**. The scenario is as follows:

- _Proposer_ is given \$10
- _Proposer_ decides how to split this amount between himself and the _Responder_
- _Responder_ is informed of the proposed allocation.
- Then, the responder can:
  - **Accept** the proposed allocation. In this case, each player gets their share of the proposed allocation.
  - **Reject** the allocation. In this case, neither the _Proposer_ nor the _Responder_ gets anything.

## Example Game

To see a working demo, visit [here](https://koltpython.github.io/assignments/demo/guacamole).

- _Proposer_ offers to split the money as follows: $7 for herself, $3 for the _Responder_.
- _Responder_ is informed of the proposed allocation.
- Based on the _Responder_'s decision:
  - _Responder_ **accepts** the offer. _Proposer_ gets $7 and _Responder_ gets $3 as payoff.
  - _Responder_ **rejects** the offer. Neither the _Proposer_ nor the _Responder_ gets anything.
