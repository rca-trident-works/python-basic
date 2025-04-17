a = "123"
b = 456
c = "3.14"
d = 2.718

# 1. Convert a to an integer
a_ = int(a)

# 2. Convert b to a string
b_ = str(b)

# 3. Convert c to a float
c_ = float(c)

# 4. Convert d to a string
d_ = str(d)

# (debug) Check the type of each variable
if (type(a_) == int and
    type(b_) == str and
    type(c_) == float and
    type(d_) == str):
    print("All conversions are correct.")
