"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""
import sys

def elf_range(line):
    line = line.split("-")
    return set(range(int(line[0]), int(line[1]) + 1))

if __name__ == "__main__":
    infile = sys.argv[1]

    contained = 0
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip().split(",")
            elf1 = set(range(int(line[0].split("-")[0]), int(line[0].split("-")[1]) + 1))
            elf2 = set(range(int(line[1].split("-")[0]), int(line[1].split("-")[1]) + 1))
            #If the length of the union is less than the total size of both sets, there is overlap
            if len(elf1) + len(elf2) != len(elf1.union(elf2)):
                contained += 1

    print(contained)