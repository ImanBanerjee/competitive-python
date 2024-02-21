while True:
    word = input("Enter a word (or type 'exit' to close the program): ")

    if word.lower() == 'exit':
        break

    if word.isalpha():
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)