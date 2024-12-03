import re

with open("input.txt", "r") as file:
    content = file.read()


do_dont_regex = r"(do\(\)|don't\(\))"

mul_regex = r"mul\((\d+),(\d+)\)"

ctrl_statements = re.split(do_dont_regex, content)
ctrl = True

commands = []

for part in ctrl_statements:
    if part == "do()":
        ctrl = True
    if part == "don't()":
        ctrl = False
    else:
        if ctrl:
            matches = re.findall(mul_regex, part)
            commands.extend(matches)

numbers = [(int(x), int(y)) for x, y in commands]

multiplication_results = []

for set in numbers:
    multiplication_results.append(set[0] * set[1])

results = sum(multiplication_results)

print(results)
