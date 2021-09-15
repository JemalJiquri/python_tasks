def main():
    inputWord = input("Please enter a palindrome :")
    palindrom(inputWord)


def palindrom(word):
    wordLengthHalf =  int(len(word) / 2)

    for i in range(0, wordLengthHalf):
        if (word[i] != word[-(i + 1)]):
            print('False')
            return False

    print("True")
    return True


if __name__ == "__main__":
    main()
