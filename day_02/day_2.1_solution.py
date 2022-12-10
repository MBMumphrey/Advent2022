import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    selection_pts = {"X":1, "Y":2, "Z":3}
    win_pts = {"A X":3, "A Y":6, "A Z":0,
               "B X":0, "B Y":3, "B Z":6,
               "C X":6, "C Y":0, "C Z":3}

    score = 0
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            score += selection_pts[line[-1]]
            score += win_pts[line]
            
    print(score)