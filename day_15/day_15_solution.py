import sys
import re

def parse_line(line):
    coords = re.match(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line).groups()    

def main():
    infile = sys.argv[1]
    lines = open(infile, 'r').readlines()
    pairs = []
    pattern = r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)"
    for line in lines:
        coords = re.match(pattern, line).groups()
        pairs.append([[int(coords[0]), int(coords[1])],[int(coords[2]), int(coords[3])]])

    row = 2000000
    known = set()
    for sensor, beacon in pairs:
        b = sensor[1] - sensor[0]
        c = sensor[1] + sensor[0]
        test_x = beacon[0]
        if (beacon[0] < sensor[0] and beacon[1] < sensor[1]) or ((beacon[0] > sensor[0] and beacon[1] > sensor[1])):
            test_y = -test_x + c
        else:
            test_y = test_x + b
        o = abs(test_y - beacon[1])
        if row < sensor[1]:
            left = c - o - row
            right = row - b + o
        else:
            left = row - b - o
            right = c + o - row
        known.update([x for x in range(left, right + 1)])
    for sensor, beacon in pairs:
        if beacon[1] == row:
            known.discard(beacon[0])
    print(len(known))

if __name__ == "__main__":
    main()