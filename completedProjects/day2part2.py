'''
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
'''

x = open("day2input.txt", 'rt') #read in text mode
input = x.readlines(0)  #'3402\n', '2044\n', '3407\n', '2833\n', '1007\n', '4695\n', '\n', '4894\n', '9624\n'
x.close()

listOfMoves = []

for each in input: #creates a list of moves from the file ['A', 'X'], ['A', 'Z'], ['A', 'Z'], ['A', 'X'], ['B', 'Z']
    tempMove = []
    tempMove = each.split()
    listOfMoves.append(tempMove)

playerScore = 0
enemyScore = 0
x = 0

while True:
    currentRound = listOfMoves[x]
    expectedOutcome = currentRound[1]
    enemyMove = currentRound[0]

    if enemyMove == 'A' and expectedOutcome == 'X': #need to lose
        playerScore += 3
        enemyScore += 7
    if enemyMove == 'A' and expectedOutcome == 'Y': #need to draw
        playerScore += 4
        enemyScore += 4
    if enemyMove == 'A' and expectedOutcome == 'Z': #need to win
        playerScore += 8
        enemyScore += 1

    if enemyMove == 'B' and expectedOutcome == 'X': #need to lose
        playerScore += 1
        enemyScore += 8
    if enemyMove == 'B' and expectedOutcome == 'Y': #need to draw
        playerScore += 5
        enemyScore += 5
    if enemyMove == 'B' and expectedOutcome == 'Z': #need to win
        playerScore += 9
        enemyScore += 2

    if enemyMove == 'C' and expectedOutcome == 'X': #need to lose
        playerScore += 2
        enemyScore += 9
    if enemyMove == 'C' and expectedOutcome == 'Y': #need to draw
        playerScore += 6
        enemyScore += 6
    if enemyMove == 'C' and expectedOutcome == 'Z': #need to win
        playerScore += 7
        enemyScore += 3

    x += 1
    if x >= len(listOfMoves): 
        break

print(playerScore)
print(enemyScore)