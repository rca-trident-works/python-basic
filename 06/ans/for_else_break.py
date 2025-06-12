print("start")
j=0
for i in range(10):
    print(f"{i=}, {j=}")
    if i > 5:
        print("break-1")
        break
    else:
        print("else-1")

    for j in range(10):
        print(f"{i=}, {j=}")
        if j > 5:
            print("break-2")
            break
        else:
            print("else-2")
    else:
        print("else-3")
else:
    print("else-4")
print("done")
