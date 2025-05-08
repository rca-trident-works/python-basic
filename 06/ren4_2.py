data = [10, 1, 0, 30, 1, 20, 0, 5, 0, 60]

# Exclude 0 from the list
excluded = [i for i in data if i != 0]

print(excluded)
