word = int(input())

all = []

for i in range(word):
    word = input()
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    all.append(word)

for i in all:
    print(i)

