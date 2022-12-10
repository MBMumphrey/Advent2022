import sys

def tick(cycle):
    if ((cycle - 1) % 40) in [x - 1, x, x + 1]:
        rows[int((cycle-1)/40)].append("#")
    else:
        rows[int((cycle-1)/40)].append(".")
    cycle += 1
    return cycle

if __name__ == "__main__":
    infile = sys.argv[1]

    rows = [[], [], [], [], [], []]
    x = 1
    cycle = 1
    with open(infile, 'r') as f:
        for line in f:
            if line.startswith("noop"):
                cycle = tick(cycle)
            else:
                cycle = tick(cycle)
                cycle = tick(cycle)
                x += int(line.split(" ")[1])

    for row in rows:
        print("".join(row))
