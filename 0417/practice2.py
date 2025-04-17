s = "Python is simple and easy."

splitted = s.split()
ans = []

# 1
ans.append(splitted[2].capitalize())

# 2
ans.append(" " + splitted[0].lower() + " ")

# 3
ans.append((splitted[0][0] + splitted[3][0:] + splitted[3][0]).upper())

# 4
ans.append("-".join(splitted[4][:-1]))


# Print the result
print(ans)
