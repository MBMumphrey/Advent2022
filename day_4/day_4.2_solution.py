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