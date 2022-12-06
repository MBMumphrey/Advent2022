import sys

if __name__ == "__main__":
    infile = sys.argv[1]
    with open(infile, 'r') as f:
        elves = []
        temp = 0
        for line in f:
            if line != "\n":
                temp += int(line)
            else:
                elves.append(temp)
                temp = 0
        print(sum(sorted(elves)[-3:]))