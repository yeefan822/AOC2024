def read_file(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    lines = file_content.strip().splitlines()
    rules = []
    updates = []

    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return rules, updates

def is_correctly_ordered(update, rules):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False
    return True
    
def fix_updates_order(update, rules):
    fixed = False
    while is_correctly_ordered(update, rules) == False:
        for a, b in rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    index_a = update.index(a)
                    index_b = update.index(b)
                    update[index_a], update[index_b] = update[index_b], update[index_a]
                    fixed = True
    return update
    
def find_middle_number(update):
    return update[len(update) // 2]

def solve_manual_ordering_sum_mediums(file_path):
    fixed_incorrect_updates = []
    rules, updates = read_file(file_path)
    for update in updates:
        if is_correctly_ordered(update, rules) == False:
            fixed_update = fix_updates_order(update, rules)
            fixed_incorrect_updates.append(fixed_update)
    middle_numbers = [find_middle_number(update) for update in fixed_incorrect_updates]
    
    print(middle_numbers)
    return sum(middle_numbers)


file_path = "Data.txt"
sum_value = solve_manual_ordering_sum_mediums(file_path)
print("Sum of mediums of fixed updates:", sum_value)


