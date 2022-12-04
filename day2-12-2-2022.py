'''
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Rock = 1 point
Scissors = 2 points
Paper = 3 points
Losing = 0 points
Draw = 3 points
Win = 6 points

'''

#this file open is copied from another project.
x = open("day2input.txt", 'rt') #read in text mode
input = x.readlines(0)  #'3402\n', '2044\n', '3407\n', '2833\n', '1007\n', '4695\n', '\n', '4894\n', '9624\n'
x.close()

listOfMoves = []

for each in input: #creates a list of moves from the file ['A', 'X'], ['A', 'Z'], ['A', 'Z'], ['A', 'X'], ['B', 'Z']
    tempMove = []
    tempMove = each.split()
    listOfMoves.append(tempMove)

playerMoves = [['X',1],['Y',2],['Z',3]]
enemyMoves = [['A',1],['B',2],['C',3]]
outcomes = [['Loss',0],['Draw',3],['Win',6]]

playerScore = 0
enemyScore = 0
x = 0

while True:
    currentRound = listOfMoves[x]
    playerMove = currentRound[1]
    enemyMove = currentRound[0]
    
    if playerMove == 'X' and enemyMove == 'A': #draw
        playerScore += 4
        enemyScore += 4
    if playerMove == 'X' and enemyMove == 'B': #Loss
        playerScore += 1
        enemyScore += 8
    if playerMove == 'X' and enemyMove == 'C': #win
        playerScore += 7
        enemyScore += 1

    if playerMove == 'Y' and enemyMove == 'A': #win
        playerScore += 8
        enemyScore += 2
    if playerMove == 'Y' and enemyMove == 'B': #draw
        playerScore += 5
        enemyScore += 5
    if playerMove == 'Y' and enemyMove == 'C': #loss
        playerScore += 2
        enemyScore += 9

    if playerMove == 'Z' and enemyMove == 'A': #loss
        playerScore += 3
        enemyScore += 7
    if playerMove == 'Z' and enemyMove == 'B': #win
        playerScore += 9
        enemyScore += 3
    if playerMove == 'Z' and enemyMove == 'C': #draw
        playerScore += 6
        enemyScore += 6
    x += 1
    if x >= len(listOfMoves): 
        break

print(playerScore)
print(enemyScore)