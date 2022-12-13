import sys
import heapdict

def djikstra(start, stop, graph):
    distances = [9999999999999 for _ in graph.keys()]
    distances[start] = 0
    q = heapdict.heapdict()
    for node, distance in enumerate(distances):
        q[node] = distance
    while (stop in q):
        cur_node, cur_dist = q.popitem()
        for node in graph[cur_node]:
            if cur_dist + 1 < distances[node]:
                distances[node] = cur_dist + 1
                if node in q:
                    q[node] = cur_dist + 1

    return distances[stop]

def input_to_graph(infile):
    lines = [line.rstrip() for line in open(infile, 'r')]
    height = len(lines)
    width = len(lines[0])
    nodes = [x for x in range(height * width)]
    graph = {node:[] for node in nodes}
    start = []
    starts = []
    end = []
    for node in nodes:
        i = node // width
        j = node % width
        c = lines[i][j]
        if c == "S":
            start = node
            lines[i] = lines[i][:j] + "a" + lines[i][j + 1:]
        if c == "E":
            end = node
            lines[i] = lines[i][:j] + "z" + lines[i][j + 1:]
    for node in nodes:
        i = node // width
        j = node % width
        c = lines[i][j]
        if c == "a":
            starts.append(node)
        elevation = ord(c)
        #Check up
        if i > 0:
            if (ord(lines[i - 1][j]) - elevation) <= 1:
                graph[node].append(node - width)
        #Check down
        if i < height - 1:
            if (ord(lines[i + 1][j]) - elevation) <= 1:
                graph[node].append(node + width)
        #Check left:
        if j > 0:
            if (ord(lines[i][j - 1]) - elevation) <= 1:
                graph[node].append(node - 1)
        #Check right:
        if j < width - 1:
            if (ord(lines[i][j + 1]) - elevation) <= 1:
                graph[node].append(node + 1)

    return graph, start, end, starts

def main():
    infile = sys.argv[1]
    graph, start, end, starts = input_to_graph(infile)
    print(f"Part 1: {djikstra(start, end, graph)}")
    min_dist = 999999999999
    for s in starts:
        temp_dist = djikstra(s, end, graph)
        if temp_dist < min_dist:
            min_dist = temp_dist
    print(f"Part 2: {min_dist}")

if __name__ == "__main__":
    main()