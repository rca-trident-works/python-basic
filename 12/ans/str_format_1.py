# format method
print('x={} , y={}'.format(10, 20))
print('x={0} , y={0} , z={1}'.format(10, 20))

s = 'a = {0} , b = {1} , c = {2}'.format(100, 200, 300)
print(s)

# f-string python3.6以降で利用可
x = 10
y = 20
print(f'x={x} , y={y}')
print(f'x={x} , y={x} , z={y}')

s = f'a = {100} , b = {200} , c = {300}'
print(s)
