num = "123.45"

# 1. Convert string to float
num = float(num)

# 2. Convert float to integer (truncating the decimal part)
num = int(num)

# 3. Convert integer to string
num = str(num)

# (debug) Print the message if the conversion is successful
print('Reached End of the program without errors!, finally:', num, ' as ', type(num))
