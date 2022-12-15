import sys
import re

def parse_line(line):
    coords = re.match(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line).groups()    

def check_gaps(ranges, boundary):
    start, stop = ranges[0]
    if start > 0:
        return 0
    for r in ranges[1:]:
        if r[0] <= stop + 1:
            if r[1] > stop:
                stop = r[1]
                if stop > boundary:
                    return None
        else:
            return stop + 1
    return None

def main():
    infile = sys.argv[1]
    lines = open(infile, 'r').readlines()
    pairs = []
    pattern = r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)"
    for line in lines:
        coords = re.match(pattern, line).groups()
        pairs.append([[int(coords[0]), int(coords[1])],[int(coords[2]), int(coords[3])]])
    bound = 4000000
    sensor_vars = []
    for sensor, beacon in pairs:
        b = sensor[1] - sensor[0]
        c = sensor[1] + sensor[0]
        test_x = beacon[0]
        if (beacon[0] < sensor[0] and beacon[1] < sensor[1]) or ((beacon[0] > sensor[0] and beacon[1] > sensor[1])):
            test_y = -test_x + c
        else:
            test_y = test_x + b
        o = abs(test_y - beacon[1])
        sensor_vars.append([sensor[1], b, c, o])
    for row in range(bound + 1):
        ranges = []
        for y, b, c, o in sensor_vars:
            if row < y:
                left = c - o - row
                right = row - b + o
            else:
                left = row - b - o
                right = c + o - row
            if left < right:
                ranges.append([left, right])
        gap = check_gaps(sorted(ranges), bound)
        if gap != None:
            print(gap * 4000000 + row)
            break

if __name__ == "__main__":
    main()