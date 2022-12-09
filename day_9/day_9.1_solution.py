import sys

if __name__ == "__main__":
    infile = sys.argv[1]
    
    H = (0, 0)
    T = (0, 0)
    seen = [(0, 0)]

    with open(infile, 'r') as f:
        for line in f:
            line = line.strip().split()
            direction = line[0]
            steps = int(line[1])
            #If the tail moves, it will always end up in the previous head's position
            for step in range(steps):
                H_old = H
                if direction == "U":
                    H = (H[0], H[1] + 1)
                if direction == "D":
                    H = (H[0], H[1] - 1)
                if direction == "L":
                    H = (H[0] - 1, H[1])
                if direction == "R":
                    H = (H[0] + 1, H[1])
                #We can tell if the tail needs to move, because all positions that cause
                #A move have a euclidean distance of greater than sqrt(2)
                if ((H[0] - T[0])**2 + (H[1] - T[1])**2)**0.5 > 1.5:
                    T = H_old
                if T not in seen:
                    seen.append(T)

    print(len(seen))