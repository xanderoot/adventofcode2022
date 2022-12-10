"""--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


crates = [
          ['B','Q','C'], # 1
          ['R','Q','W','Z'], # 2
          ['B','M','R','L','V'], # 3
          ['C','Z','H','V','T','W'], # 4
          ['D','Z','H','B','N','V','G'], #5
          ['H','N','P','C','J','F','V','Q'], # 6
          ['D','G','T','R','W','Z','S'], # 7
          ['C','G','M','N','B','W','Z','P'], # 8
          ['N','J','B','M','W','Q','F','P'] # 9
          ]

with open('Python/adventofcode2022/day5part1input.txt','r') as x:
    rawData = x.readlines()


rawData = [each[:-1] for each in rawData] # remove \n from each string
# no idea why the above worked, its not one string, its a list of strings


tempCrate = []

for x in range(len(rawData)): # creates a list on string ints
    rawData[x] = rawData[x].split(' ')
    rawData[x].pop(0)
    rawData[x].pop(1)
    rawData[x].pop(2)

for x in range(len(rawData)):

    y = rawData[x]
    numberToMove = int(y[0])
    originPile = int(y[1]) - 1
    destinationPile = int(y[2]) - 1
    for x in range(numberToMove):
        box = crates[originPile].pop(-1)
        crates[destinationPile].append(box)

for each in crates:
    print(each[-1])