import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    selection_pts = {"X":1, "Y":2, "Z":3}
    decision = {"A X":["Z", 0], "A Y":["X", 3], "A Z":["Y", 6],
                "B X":["X", 0], "B Y":["Y", 3], "B Z":["Z", 6],
                "C X":["Y", 0], "C Y":["Z", 3], "C Z":["X", 6]}

    score = 0
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            score += selection_pts[decision[line][0]]
            score += decision[line][1]
            
    print(score)