from collections import defaultdict

rules = defaultdict(list)
updates = []

with open("ordering-rules.txt", "r") as file:
    for line in file:
        parts = list(map(int, line.strip().split("|")))
        key = parts[0]
        values = parts[1:]
        rules[key].extend(values)

with open("update.txt", "r") as file:
    for line in file:
        input = list(map(int, line.split(",")))
        updates.append(input)


def is_valid(update):
    print(f"UPDATE: {update}")
    for y, page in enumerate(update):
        page_rules = set(rules[page])
        print(f"RULES:{page}|| {page_rules}")
        # nothing left of page in update should be contained within page_rules
        if any(rule in update[:y] for rule in page_rules):
            return False
    return True


def sort_rule(update):
    print(f"SORTING UPDATE: {update}")
    for y, page in enumerate(update):
        page_rules = set(rules[page])
        print(f"RULES:{page}||{page_rules}")
        violations = [rule for rule in page_rules if rule in update[:y]]
        if violations:
            earliest_violation = min(update.index(rule) for rule in violations)
            print(f"CONFLICT:{page} conflicts with {update[earliest_violation]}")

            update.pop(y)
            update.insert(earliest_violation, page)
    if is_valid(update):
        return update
    else:
        print(
            "RESORTING------------------------------------------------------------------------------------------>"
        )
        return sort_rule(update)


valid_rules = []
invalid_rules = []

for update in updates:
    unsorted = update[:]
    if is_valid(update):
        valid_rules.append(update[len(update) // 2])
    else:
        sortedrule = sort_rule(update)
        print(f"****SORTED {unsorted} to {update}||**********")
        if is_valid(sortedrule):
            invalid_rules.append(sortedrule[len(sortedrule) // 2])
        else:
            print(f"INVALID UPDATE: {unsorted} sorted to {sortedrule}")


print(f"Sum: {sum(valid_rules)}")
print(f"Invalid Sums: {sum(invalid_rules)}")
