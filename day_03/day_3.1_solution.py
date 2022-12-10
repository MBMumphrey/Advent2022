import sys
from collections import Counter

if __name__ == "__main__":
    infile = sys.argv[1]
    score = 0
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            sack1 = set(line[:int(len(line)/2)])
            sack2 = set(line[int(len(line)/2):])
            common = list(sack1.intersection(sack2))[0]
            if common.islower():
                score += ord(common) - 96
            else:
                score += ord(common) - 38
    
    print(score)

