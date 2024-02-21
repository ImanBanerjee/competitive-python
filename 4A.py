def can_divide_watermelon(w):
    for i in range(1, w):
        if i % 2 == 0 and (w - i) % 2 == 0:
            return "YES"
    return "NO"

# Reading input
w = int(input())

# Checking if the watermelon can be divided
result = can_divide_watermelon(w)
print(result)

