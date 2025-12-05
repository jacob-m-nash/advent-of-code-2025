with open("Day4/input.txt") as f:
    matrix = [list(line.strip()) for line in f]

rows = len(matrix)
cols = len(matrix[0])
pad = 1
padded_matrix = [["."] * (cols + 2)]
for row in matrix:
    padded_matrix.append(["."] + row + ["."])
padded_matrix.append(["."] * (cols + 2))

counter = 0
for r in range(rows):
    for c in range(cols):
        pr = r + pad
        pc = c + pad

        window = [row[pc - 1:pc + 2] for row in padded_matrix[pr - 1:pr + 2]]
        if(window[1][1] != "@"): continue

        dot_count = 0
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if (window[i][j] == "."):
                    dot_count += 1

        if (dot_count > 4):
            matrix[r][c] = "x"
            counter += 1

print(counter)