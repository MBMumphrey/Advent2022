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
            #If the set of both elves is equal in size to the size of the largest set, then one contains the other
            if max(len(elf1), len(elf2)) == len(elf1.union(elf2)):
                contained += 1

    print(contained)