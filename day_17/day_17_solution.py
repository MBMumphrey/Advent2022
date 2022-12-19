import sys
import copy
"""
Rock types
0:  ####    1:  .#.     2:  ..#     3:  #   4:  ##
                ###         ..#         #       ##
                .#.         ###         #
                                        #
"""
def to_tuple(l):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in l)

class Rock():
    height_dict = {0:1, 1:3, 2:3, 3:4, 4:2}
    width_dict = {0:4, 1:3, 2:3, 3:1, 4:2}
    offset_dict = {0:[(0, 0), (1, 0), (2, 0), (3, 0)],
                   1:[(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
                   2:[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                   3:[(0, 0), (0, 1), (0, 2), (0, 3)],
                   4:[(0, 0), (1, 0), (0, 1), (1, 1)]}
    def __init__(self, t, pos):
        self.type = t
        self.pos = pos
        self.height = self.height_dict[self.type]
        self.width = self.width_dict[self.type]
        self.offsets = self.offset_dict[self.type]

    def stopped_bottom(self, chamber, bottom_offset):
        x, y = self.pos
        for x_o, y_o in self.offsets:
            if y + y_o - 1 < 0:
                return True
            elif chamber[y + y_o - 1 - bottom_offset][x + x_o] != ".":
                return True
        return False
    
    def stopped_left(self, chamber, bottom_offset):
        x, y = self.pos
        for x_o, y_o in self.offsets:
            if x + x_o - 1 < 0:
                return True
            elif chamber[y + y_o - bottom_offset][x + x_o - 1] != ".":
                return True
        return False
    
    def stopped_right(self, chamber, bottom_offset):
        x, y = self.pos
        for x_o, y_o in self.offsets:
            if x + x_o + 1 >= 7:
                return True
            elif chamber[y + y_o - bottom_offset][x + x_o + 1] != ".":
                return True
        return False
        return False

class Chamber():
    bottom_offset = 0
    def __init__(self, jets):
        self.chamber = [["." for _ in range(7)]]
        self.top = 0
        self.jets = jets
        self.jet_pos = 0
        self.next_rock = 0
        self.rocks = []
        self.spawn_rock()
        self.bottom_offset = 0
        self.hashes = {}
        self.cycle = -1
        self.cycle_rock = -1
        self.cycle_floor_height = -1
        self.cycle_gap_height = -1

    def __str__(self):
        print_copy = copy.deepcopy(self.chamber)
        if len(self.rocks) > 0:
            falling_rock = self.rocks[-1]
            x, y = falling_rock.pos
            for x_o, y_o in falling_rock.offsets:
                print_copy[y + y_o][x + x_o] = "@"
        rows = ["".join(row) for row in print_copy]
        return "\n".join([row for row in rows][::-1] + ["~~~~~~~~~~~~~~~"])

    def spawn_rock(self):
        rock_type = self.next_rock
        self.next_rock = (self.next_rock + 1) % 5
        rock_loc = [2, self.top + 3]
        self.rocks.append(Rock(rock_type, rock_loc))
        new_height = 3 + self.rocks[-1].height - (len(self.chamber) + self.bottom_offset - self.top - 1)
        self.chamber = self.chamber + [["." for _ in range(7)] for __ in range(new_height)]
        if len(self.chamber) > 100:
            self.bottom_offset += len(self.chamber) - 100
            self.chamber = self.chamber[-100:]
            if self.cycle == -1:
                h = hash(to_tuple(self.chamber))
                if h in self.hashes:
                    self.cycle = len(self.rocks)
                    self.cycle_rock = self.hashes[h][0]
                    self.cycle_floor_height = self.hashes[h][1]
                    self.cycle_gap_height = self.top - self.cycle_floor_height
                else:
                    self.hashes[h] = [len(self.rocks), self.top]

    def tick(self):
        if self.jets[self.jet_pos] == "<":
            if not self.rocks[-1].stopped_left(self.chamber, self.bottom_offset):
                self.rocks[-1].pos[0] -= 1
        else:
            if not self.rocks[-1].stopped_right(self.chamber, self.bottom_offset):
                self.rocks[-1].pos[0] += 1
        self.jet_pos = (self.jet_pos + 1) % len(self.jets)
        if self.rocks[-1].stopped_bottom(self.chamber, self.bottom_offset):
            x, y = self.rocks[-1].pos
            for x_o, y_o in self.rocks[-1].offsets:
                self.chamber[y + y_o - self.bottom_offset][x + x_o] = "#"
            self.top = max(self.top, self.rocks[-1].pos[1] + self.rocks[-1].height)
            self.spawn_rock()
        else:
            self.rocks[-1].pos[1] -= 1

def main():
    infile = sys.argv[1]
    jets = open(infile, 'r').readlines()[0].strip()
    chamber = Chamber(jets)
    while chamber.cycle == -1:
        chamber.tick()
    print(f"Cycle starts at rock {chamber.cycle_rock} with length {chamber.cycle - chamber.cycle_rock}")
    print(f"\tHeight at {chamber.cycle_rock}: {chamber.cycle_floor_height}")
    print(f"\tCycle height: {chamber.cycle_floor_height + chamber.cycle_gap_height}")
    targets = [2023 , 1000000000000]
    for target in targets:
        print(f"Target: {target}")
        full_cycles = (target - chamber.cycle_rock) // (chamber.cycle - chamber.cycle_rock)
        remainder = target - (full_cycles * (chamber.cycle - chamber.cycle_rock)) - chamber.cycle_rock
        print(f"\tTarget contains first {chamber.cycle_rock} rocks, {full_cycles} full cycles, and {remainder} remainder")
        temp_chamber = Chamber(jets)
        while len(temp_chamber.rocks) != chamber.cycle_rock + remainder + 1:
            temp_chamber.tick()
        remainder_height = temp_chamber.top - chamber.cycle_floor_height
        print(f"\tTarget height:{chamber.cycle_floor_height + (chamber.cycle_gap_height * full_cycles) + remainder_height}")

if __name__ == "__main__":
    main()