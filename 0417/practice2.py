s = "Python is simple and easy."

# Make array ['Simple', ' python ', 'PANDA', 'e-a-s-y']

splitted = s.split()

ans = []

# 1
ans.append(splitted[2].capitalize())

# 2
ans.append(" " + splitted[0].lower() + " ")

# 3 (Pick target char from string)
ans.append(splitted[0][0].upper() + splitted[3][0:].upper() + splitted[3][0].upper())


print(ans)
