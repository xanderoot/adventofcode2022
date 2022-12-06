'''











I failed this and copied it from https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/iz2dcw5/?utm_source=share&utm_medium=web2x&context=3













--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

'''

with open("day4part1input.txt") as file:
    lines = [i for i in file.read().splitlines()]

full_total = 0
partial_total = 0

for line in lines:
    section1, section2 = line.split(",")
    section1_begin, section1_end = section1.split("-")
    section2_begin, section2_end = section2.split("-")
    range_1 = [num for num in range(int(section1_begin), int(section1_end) + 1)]
    range_2 = [num for num in range(int(section2_begin), int(section2_end) + 1)]
    if all(x in range_1 for x in range_2) or all(x in range_2 for x in range_1):
        full_total += 1
    if any(x in range_1 for x in range_2):
        partial_total += 1

print(f"Complete Overlap {full_total}")
print(f"Partial Overlap {partial_total}")
