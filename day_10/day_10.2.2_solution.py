import sys

def tick():
    rows[int((cycle[0]-1)/40)] += "#" if ((cycle[0] - 1) % 40) in [x - 1, x, x + 1] else "."
    cycle[0] += 1

if __name__ == "__main__":
    infile = sys.argv[1]

    rows = ["", "", "", "", "", ""]
    cycle = [1]
    x = 1
    for line in open(infile, 'r').readlines():
        tick() #You always noop once
        if line.startswith("addx"): #Then addx gets its own extra add cycle
            tick()
            x += int(line.split(" ")[1])

    for row in rows: print(row)