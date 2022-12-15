import sys

def print_grid(grid):
    for row in grid:
        print("".join(row))

def parse_rocks(lines):
    rocks = []
    for line in lines:
        points = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in line.strip().split(" -> ")]
        for i in range(len(points) - 1):
            start = points[i]
            end = points[i + 1]
            if start[0] == end[0]:
                new_rocks = [[start[0], j] for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1)]
                rocks += new_rocks
            else:
                new_rocks = [[j, start[1]] for j in range(min(start[0], end[0]), max(start[0], end[0]) + 1)]
                rocks += new_rocks
    xmin = min([x[0] for x in rocks])
    xmax = max([x[0] for x in rocks])
    ymin = 0
    ymax = max([x[1] for x in rocks])
    grid = [["." for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]
    for x, y in rocks:
        grid[y - ymin][x - xmin] = "#"
    return [grid, xmin]

def drop_sand(start, grid):
    if start[1] + 1 > len(grid) - 1:
        return None
    elif grid[start[1] + 1][start[0]] == ".":
        return drop_sand([start[0], start[1] + 1], grid)
    elif start[0] - 1 < 0:
        return None
    elif grid[start[1] + 1][start[0] - 1] == ".":
        return drop_sand([start[0] - 1, start[1] + 1], grid)
    elif start[0] + 1 > len(grid[0]) - 1:
        return None
    elif grid[start[1] + 1][start[0] + 1] == ".":
        return drop_sand([start[0] + 1, start[1] + 1], grid)
    else:
        return start
    
def main():
    infile = sys.argv[1]
    lines = open(infile, 'r').readlines()

    grid, offset = parse_rocks(lines)
    sand = []
    i = 0
    while sand != None:
        sand = drop_sand([500 - offset, 0], grid)
        if sand == None:
            break
        grid[sand[1]][sand[0]] = "O"
        #print_grid(grid)
        #print("".join(["~" for _ in range(len(grid[0]))]))
        i += 1
    print_grid(grid)
    print(i)

if __name__ == "__main__":
    main()