import sys

class Monkey:
    def __init__(self, lines, key):
        self.n = int(lines[0][-3])
        self.items = [key + i for i in range(len(lines[1].split(":")[1].split(", ")))]
        self.operation = "+" if lines[2].find("+") != -1 else "*"
        self.operation_target = lines[2].strip().split(" ")[-1]
        self.test_val = int(lines[3].split( )[-1])
        self.true_throw = int(lines[4].split()[-1])
        self.false_throw = int(lines[5].split()[-1])
        self.inspected = 0

    def catch(self, item):
        self.items.append(item)

    def throw(self, items_mod, mods):
        self.inspected += 1
        item = self.items.pop(0)
        #Update each items worry mod each monkey
        for i, worry in enumerate(items_mod[item]):
            op_tar = worry if self.operation_target == "old" else int(self.operation_target)
            if self.operation == "+":
                items_mod[item][i] = (worry + op_tar) % mods[i]
            else:
                items_mod[item][i] = (worry * (op_tar % mods[i])) % mods[i]
        
        return [items_mod, item, self.true_throw if items_mod[item][self.n] == 0 else self.false_throw]

if __name__ == "__main__":
    infile = sys.argv[1]

    lines = open(infile, 'r').readlines()
    monkeys = []
    items = {}
    mods = []
    key = 0
    #Store items as keys in each monkey
    for i in range(0, len(lines), 7):
        monkeys.append(Monkey(lines[i:i+6], key))
        for j, item in enumerate(lines[i+1].split(":")[1].split(", ")):
            items[key + j] = int(item)
        mods.append(int(lines[i + 3].split(" ")[-1]))
        key += len(monkeys[-1].items)

    #Keep a dict which tracks each item's worry separately modulo
    #each monkey's test value
    items_mod = {k:[] for k in items.keys()}
    for k, v in items.items():
        for monkey in monkeys:
            items_mod[k].append(v % monkey.test_val)

    for _ in range(10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                items_mod, item, target = monkey.throw(items_mod, mods)
                monkeys[target].catch(item)

    activity = sorted([monkey.inspected for monkey in monkeys])
    print(activity[-1] * activity[-2])