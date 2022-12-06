import sys

if __name__ == "__main__":
    infile = sys.argv[1]

    with open(infile, 'r') as f:
        line = next(f).strip()
        for i in range(13, len(line)):
            chunk = [x for x in line[(i - 13) : (i + 1)]]
            if len(set(chunk)) == 14:
                print(i + 1)
                break
