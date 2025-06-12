a = [1, 2, 3]
b = [1, 2, 3]

if a == b:
    print("同じ")
else:
    print("異なる")

if a is b:
    print("同じ")
else:
    print("異なる")
    
c = a
if a == c:
    print("同じ")
else:
    print("異なる")

if a is c:
    print("同じ")
else:
    print("異なる")
