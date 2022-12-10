import sys

if __name__ == "__main__":
    infile = sys.argv[1]
    with open(infile, 'r') as f:
        max = 0
        temp = 0
        for line in f:
            if line != "\n":
                temp += int(line)
            else:
                if temp > max:
                    max = temp
                temp = 0
        print(max)