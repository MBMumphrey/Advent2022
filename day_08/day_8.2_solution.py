import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    with open(infile, 'r') as f:
        lines = f.read().splitlines()

    width = len(lines[0])
    height = len(lines)
    max_scenic = -1
    for i in range(height):
        for j in range(width):
            if i in [0, height - 1] or j in [0, width - 1]:
                continue
            tree = int(lines[i][j])
            try:
                up = [int(lines[x][j]) >= tree for x in range(i)][::-1].index(True) + 1
            except:
                up = i
            try:
                down = [int(lines[x][j]) >= tree for x in range(i+1, height)].index(True) + 1
            except:
                down = height - i - 1
            try:
                left = [int(lines[i][y]) >= tree for y in range(j)][::-1].index(True) + 1
            except:
                left = j
            try:
                right = [int(lines[i][y]) >= tree for y in range(j+1, width)].index(True) + 1
            except:
                right = width - j - 1
            scenic = up * down * left * right
            if scenic > max_scenic:
                max_scenic = scenic

    print(max_scenic)