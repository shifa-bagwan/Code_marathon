strs = ["act", "pots", "tops", "cat", "stop", "hat"]

groups = {}

for word in strs:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))