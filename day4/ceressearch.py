grid = []
search_terms = ["XMAS", "SAMX"]
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

count = 0

for search_term in search_terms:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == search_term[0]:
                if x + len(search_term) - 1 < len(row):
                    target = "".join(row[x : x + len(search_term)])
                    if target == search_term:
                        count += 1
                if y + len(search_term) - 1 < len(grid):
                    target = "".join(
                        grid[y + delta][x] for delta in range(len(search_term))
                    )
                    if target == search_term:
                        count += 1
                if x + len(search_term) - 1 < len(row) and y + len(
                    search_term
                ) - 1 < len(grid):
                    target = "".join(
                        grid[y + delta][x + delta] for delta in range(len(search_term))
                    )
                    if target == search_term:
                        count += 1
                if (
                    x + len(search_term) - 1 < len(row)
                    and y - len(search_term) + 1 >= 0
                ):
                    target = "".join(
                        grid[y - delta][x + delta] for delta in range(len(search_term))
                    )
                    if target == search_term:
                        count += 1

# since the pattern has been flattened, order of verification is very important
# M.S
# .A.
# M.S
patterns = ["MSAMS", "SMASM", "MMASS", "SSAMM"]
# set of relative delts for matching the pattern
deltas = [[0, 0], [2, 0], [1, 1], [0, 2], [2, 2]]

pattern_count = 0

for pattern in patterns:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == pattern[0]:
                target = ""
                if x + 2 >= len(row) or y + 2 >= len(
                    grid
                ):  # check if theres room for the box patterb
                    continue
                for delta in deltas:
                    target += grid[y + delta[1]][x + delta[0]]
                if target == pattern:
                    pattern_count += 1

print(f"XMAS Count: {count}")
print(f"X-MAS Count: {pattern_count}")
