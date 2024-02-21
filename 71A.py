while True:
    try:
        word = input("Enter a word (or type 'exit' to close the program): ")

        if word.lower() == 'exit':
            break

        if word.isalpha():
            if len(word) > 10:
                print(word[0] + str(len(word) - 2) + word[-1])
            else:
                print(word)
        else:
            print("Please enter a valid word (only alphabetic characters allowed).")
    except EOFError:
        print("Error: EOF (End of File) encountered. Exiting the program.")
        break
    except Exception as e:
        print("An error occurred:", e)
