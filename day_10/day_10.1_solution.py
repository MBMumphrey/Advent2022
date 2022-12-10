import sys

def tick(x, cycle, total):
    if (cycle - 20) % 40 == 0:
        total += x*cycle
    cycle += 1
    return x, cycle, total

if __name__ == "__main__":
    infile = sys.argv[1]

    total = 0
    x = 1
    cycle = 1
    with open(infile, 'r') as f:
        for line in f:
            if line.startswith("noop"):
                x, cycle, total = tick(x, cycle, total)
            else:
                x, cycle, total = tick(x, cycle, total)
                x, cycle, total = tick(x, cycle, total)
                x += int(line.split(" ")[1])

    print(total)
