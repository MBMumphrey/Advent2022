import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    #Parse disk, taking into account dirs of the same name
    #can occur in different places
    global_disk = {}
    dir_stack = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip().split()
            if line[1] == "cd":
                if line[2] == "..":
                    dir_stack.pop()
                else:
                    dir_stack.append("".join(dir_stack) + "/" + line[2])
            if line[0].isnumeric():
                for d in dir_stack:
                    if d in global_disk:
                        global_disk[d] += int(line[0])
                    else:
                        global_disk[d] = int(line[0])
    #Solution 1
    print(sum([x for x in global_disk.values() if x <= 100000]))

    #Solution 2
    free = 70000000 - global_disk["/"]
    needed = 30000000 - free
    best = 0
    best_diff = 1000000000000
    for x in global_disk.values():
        diff = x - needed
        if diff > 0 and diff < best_diff:
            best = x
            best_diff = diff
    print(best)