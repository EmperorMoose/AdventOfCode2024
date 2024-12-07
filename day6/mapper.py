with open("map.txt", "r") as file:
    map = [list(line.strip()) for line in file]

guard = {"^", "<", ">", "V"}

distinct_count = 0


def printmap(map):
    for line in map:
        print(line)


def find_guard(map):
    position = None
    for r, row in enumerate(map):
        for c, char in enumerate(row):
            if char in guard:
                position = (r, c)
                return position


def check_collision(map, loc):
    if loc[0] < 0 or loc[0] >= len(map) or loc[1] < 0 or loc[1] >= len(map[loc[0]]):
        return False, True

    if map[loc[0]][loc[1]] == "#":
        return True, False

    if map[loc[0]][loc[1]] != "X":
        global distinct_count
        distinct_count += 1

    return False, False


def calculate_move(map, guardloc, direction):
    loc = list(guardloc)
    offmap = False
    match direction:
        case "^":
            collision, offmap = check_collision(map, [loc[0] - 1, loc[1]])
            if not collision and not offmap:
                map[loc[0]][loc[1]] = "X"
                map[loc[0] - 1][loc[1]] = "^"
                return (loc[0] - 1, loc[1]), offmap
            elif collision:
                return calculate_move(map, loc, ">")
            elif offmap:
                offmap = True
                return loc, offmap
        case ">":
            collision, offmap = check_collision(map, [loc[0], loc[1] + 1])
            if not collision and not offmap:
                map[loc[0]][loc[1]] = "X"
                map[loc[0]][loc[1] + 1] = ">"
                return (loc[0], loc[1] + 1), offmap
            elif collision:
                return calculate_move(map, loc, "V")
            elif offmap:
                offmap = True
                return loc, offmap
        case "V":
            collision, offmap = check_collision(map, [loc[0] + 1, loc[1]])
            if not collision and not offmap:
                map[loc[0]][loc[1]] = "X"
                map[loc[0] + 1][loc[1]] = "V"
                return (loc[0] + 1, loc[1]), offmap
            elif collision:
                return calculate_move(map, loc, "<")
            elif offmap:
                offmap = True
                return loc, offmap
        case "<":
            collision, offmap = check_collision(map, [loc[0], loc[1] - 1])
            if not collision and not offmap:
                map[loc[0]][loc[1]] = "X"
                map[loc[0]][loc[1] - 1] = "<"
                return (loc[0], loc[1] - 1), offmap
            elif collision:
                return calculate_move(map, loc, "^")
            elif offmap:
                offmap = True
                return loc, offmap
    return loc, True


printmap(map)
guardloc = find_guard(map)
if guardloc is None:
    exit()
print(f"Guard at {guardloc}")
over = False
while not over:
    guardloc, over = calculate_move(map, guardloc, map[guardloc[0]][guardloc[1]])
    printmap(map)
    print(
        "---------------------------------------------------------------------------------------------------"
    )

print(f"Distinct Count: {distinct_count+1}")
