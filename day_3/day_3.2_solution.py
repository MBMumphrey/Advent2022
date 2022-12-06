import sys
from collections import Counter

if __name__ == "__main__":
    infile = sys.argv[1]
    score = 0
    with open(infile, 'r') as f:
        for line in f:
            elf1 = set(line.strip())
            elf2 = set(next(f).strip())
            elf3 = set(next(f).strip())
            common = list(elf1.intersection(elf2.intersection(elf3)))[0]
            if common.islower():
                score += ord(common) - 96
            else:
                score += ord(common) - 38
    
    print(score)

