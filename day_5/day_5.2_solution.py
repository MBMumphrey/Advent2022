"""
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

import sys

def parse_columns(col_lines, col_n):
    cols = [[] for n in range(col_n)]
    for line in col_lines[::-1]:
        for i in range(col_n):
            c = line[i*4 + 1]
            if c != " ":
                cols[i].append(c)
    return cols

if __name__ == "__main__":
    infile = sys.argv[1]

    with open(infile, 'r') as f:
        column_lines = []
        column_index = ""
        command_lines = []
        for line in f:
            if line.startswith("["):
                column_lines.append(line)
            elif line.startswith(" "):
                column_index = line.strip()
            elif line.startswith("\n"):
                continue
            elif line.startswith("move"):
                command_lines.append(line.strip().split())
        columns = parse_columns(column_lines, len(column_index.split()))
        for command in command_lines:
            temp = []
            for move in range(int(command[1])):
                temp.append(columns[int(command[3]) - 1].pop())
            columns[int(command[5]) - 1] += temp[::-1]
        print("".join([col[-1] for col in columns]))