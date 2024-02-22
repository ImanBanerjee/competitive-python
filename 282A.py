x = 0

operation = input()

for i in range(int(operation)):
    operation = input()
    if operation[1] == '+':
        x += 1
    else:
        x -= 1

print(x)