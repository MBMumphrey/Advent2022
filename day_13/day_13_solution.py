import sys
from functools import cmp_to_key

def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return -1
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        for x, y in zip(left, right):
            res = check_order(x, y)
            if res != 0:
                return res
        if len(left) == len(right):
            return 0
        elif len(left) < len(right):
            return -1
        else:
            return 1
    else:
        if isinstance(left, int):
            return check_order([left], right)
        elif isinstance(right, int):
            return check_order(left, [right])

def main():
    lines = open(sys.argv[1], 'r').readlines()
    pairs = [[eval(lines[i]), eval(lines[i + 1])] for i in range(0, len(lines), 3)]
    total = 0
    for i, pair in enumerate(pairs):
        if check_order(pair[0], pair[1]) == -1:
            total += i + 1
    print(f"Part 1: {total}")

    packets = [eval(line) for line in lines if line != "\n"] + [[[2]], [[6]]]
    packets_ordered = sorted(packets, key = cmp_to_key(check_order))
    print(f"Part 2: {(packets_ordered.index([[2]]) + 1) * (packets_ordered.index([[6]]) + 1)}")

if __name__ == "__main__":
    main()