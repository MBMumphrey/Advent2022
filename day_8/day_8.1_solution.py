import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    with open(infile, 'r') as f:
        lines = f.read().splitlines()

    width = len(lines[0])
    height = len(lines)
    visible = 0
    for i in range(height):
        for j in range(width):
            if i in [0, height - 1] or j in [0, width - 1]:
                visible += 1
                continue
            tree = int(lines[i][j])
            up = max([int(lines[x][j]) for x in range(i)])
            down = max([int(lines[x][j]) for x in range(i+1, height)])
            left = max([int(lines[i][y]) for y in range(j)])
            right = max([int(lines[i][y]) for y in range(j+1, width)])
            if tree > up or tree > down or tree > left or tree > right:
                visible += 1

    print(visible)