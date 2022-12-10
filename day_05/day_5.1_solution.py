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
            for move in range(int(command[1])):
                columns[int(command[5]) - 1].append(columns[int(command[3]) - 1].pop())
        print("".join([col[-1] for col in columns]))