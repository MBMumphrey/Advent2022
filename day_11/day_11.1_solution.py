import sys

class Monkey:
    def __init__(self, lines):
        self.items = [int(x) for x in lines[0].split(":")[1].strip().split(", ")]
        self.operation = "+" if lines[1].find("+") != -1 else "*"
        self.operation_target = lines[1].strip().split(" ")[-1]
        self.test_val = int(lines[2].split( )[-1])
        self.true_throw = int(lines[3].split()[-1])
        self.false_throw = int(lines[4].split()[-1])
        self.inspected = 0

    def catch(self, item):
        self.items.append(item)

    def throw(self):
        self.inspected += 1
        worry = self.items.pop(0)
        target = worry if self.operation_target == "old" else int(self.operation_target)
        worry = int((worry + target if self.operation == "+" else worry * target)/3)
        return [worry, self.true_throw if worry % self.test_val == 0 else self.false_throw]

if __name__ == "__main__":
    infile = sys.argv[1]

    lines = open(infile, 'r').readlines()
    monkeys = []
    for i in range(1, len(lines), 7):
        monkeys.append(Monkey(lines[i:i+5]))

    for _ in range(20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                worry, target = monkey.throw()
                monkeys[target].catch(worry)
    
    activity = sorted([monkey.inspected for monkey in monkeys])
    print(activity[-1] * activity[-2])