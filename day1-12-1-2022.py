'''
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. 
As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. 
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
In the example above, this is 24000 (carried by the fourth Elf).

#########################################################################

separate all lines to a list
while loop that pushes each value to a list
when it encounters a blank line (likely a \n character) push that array to the list of elves.

'''

listOfElves = []
#will be two dimensional, [[1,1000,2000],[2,1000,2000]]

#this file open is copied from another project.
x = open("day1input.txt", 'rt') #read in text mode
input = x.readlines(0)  #'3402\n', '2044\n', '3407\n', '2833\n', '1007\n', '4695\n', '\n', '4894\n', '9624\n'
x.close()

elfLog = [] #temp value for each elf

while True: #separates the list of elves and their inventories
    if input == []:
        break
    elif input[0] == '\n': #<---- that took me ten minutes to figure out it was the wrong slash! 
        temp = elfLog.copy() #python lists are linked, this creates a non linked copy that can be appended freely
        listOfElves.append(temp)
        input.pop(0)
        elfLog.clear()
    else:
        elfLog.append(input[0])
        input.pop(0)

#print(listOfElves) #contains the two dimensional lists. , ['4894\n', '9624\n'], ['4894\n', '9624\n'], ['4894\n', '9624\n'], ['4894\n', '9624\n']]

#print(len(listOfElves)) #254


for x in range(len(listOfElves)): #this creates a list of all elves with their inventories as ints, with the values sorted high to low
    elfInLimbo = []
    copyOfElf = listOfElves[0]
    listOfElves.pop(0)
    for each in copyOfElf: 
        each = each.rstrip(each[-1])
        elfInLimbo.append(int(each))
    elfInLimbo.sort(reverse=True)
    listOfElves.append(elfInLimbo)

for x in range(len(listOfElves)): #sums each of the elves inventories.
    elfInLimbo = []
    copyOfElf = listOfElves[0]
    listOfElves.pop(0)
    sumOfInventory = sum(copyOfElf)
    listOfElves.append(sumOfInventory)

indexOfMax = 0
max = 0
x = 0
for each in listOfElves: #finds the max and logs the index of it
    if listOfElves[x] >= max:
        max = listOfElves[x]
        indexOfMax = x
    x += 1

print(listOfElves[indexOfMax])