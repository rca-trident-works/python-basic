# x=5 , y=20とする。  
# x<10 かつ y>10 のとき、xとyを出力する。  
# ループごとに xは1増加、yは2減少する。

x = 5
y = 20
while x < 10 and y > 10:
    # print(f"x={x},y={y}")
    print(f"{x=},{y=}")
    x += 1
    y -= 2
