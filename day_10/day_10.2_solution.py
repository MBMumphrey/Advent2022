import sys

def tick(x, cycle, rows):
    if ((cycle - 1) % 40) in [x - 1, x, x + 1]:
        rows[int((cycle-1)/40)].append("#")
    else:
        rows[int((cycle-1)/40)].append(".")
    cycle += 1
    return x, cycle, rows

if __name__ == "__main__":
    infile = sys.argv[1]

    rows = [[], [], [], [], [], []]
    x = 1
    cycle = 1
    with open(infile, 'r') as f:
        for line in f:
            if line.startswith("noop"):
                x, cycle, rows = tick(x, cycle, rows)
            else:
                x, cycle, rows = tick(x, cycle, rows)
                x, cycle, rows = tick(x, cycle, rows)
                x += int(line.split(" ")[1])

    for row in rows:
        print("".join(row))
