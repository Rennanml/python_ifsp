x = int(input())
y = int(input())
z = int(input())
while x < 10:
    x = x + 3
    y = y + (x % 2)
flag = True
while flag and y < 10:
    y = y + 2
    x = x - 1
    if x <= y:
        flag = False
i = 0
while i < z:
    y = y + i
    i = i + 1
print(x, y, z)