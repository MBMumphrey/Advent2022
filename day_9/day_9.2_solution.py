import sys

if __name__ == "__main__":
    infile = sys.argv[1]
    
    nodes = [(0, 0)]*10
    seen = [(0, 0)]

    with open(infile, 'r') as f:
        for line in f:
            line = line.strip().split()
            direction = line[0]
            steps = int(line[1])
            #If the tail moves, it will always end up in the previous head's position
            for step in range(steps):
                #nodes_old = tuple(nodes)
                if direction == "U":
                    nodes[0] = (nodes[0][0], nodes[0][1] + 1)
                if direction == "D":
                    nodes[0] = (nodes[0][0], nodes[0][1] - 1)
                if direction == "L":
                    nodes[0] = (nodes[0][0] - 1, nodes[0][1])
                if direction == "R":
                    nodes[0] = (nodes[0][0] + 1, nodes[0][1])
                for i in range(len(nodes) - 1):
                    #We can tell if the tail needs to move, because all positions that cause
                    #A move have a euclidean distance of greater than sqrt(2)
                    if ((nodes[i][0] - nodes[i + 1][0])**2 + (nodes[i][1] - nodes[i + 1][1])**2)**0.5 > 1.5:
                        #Unlike part 1, we can't assume each node will take the original position of the leading node
                        #because mid-rope nodes can make diagonal moves
                        new_x = (nodes[i + 1][0] + (nodes[i + 1][0] < nodes[i][0]) - (nodes[i + 1][0] > nodes[i][0]))
                        new_y = (nodes[i + 1][1] + (nodes[i + 1][1] < nodes[i][1]) - (nodes[i + 1][1] > nodes[i][1]))
                        nodes[i + 1] = (new_x, new_y)
                if nodes[-1] not in seen:
                    seen.append(nodes[-1])

    print(len(seen))