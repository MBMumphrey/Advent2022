import sys

def tick(cycle):
    rows[int((cycle-1)/40)] += "#" if ((cycle - 1) % 40) in [x - 1, x, x + 1] else "."
    cycle += 1
    return cycle

if __name__ == "__main__":
    infile = sys.argv[1]

    rows = ["", "", "", "", "", ""]
    x, cycle = 1, 1
    for line in open(infile, 'r').readlines():
        cycle = tick(cycle) #You always noop once
        if line.startswith("addx"): #Then addx gets its own extra add cycle
            cycle = tick(cycle)
            x += int(line.split(" ")[1])

    for row in rows: print(row)