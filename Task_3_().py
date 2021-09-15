def main():
    inputTxt = input("input yours string :")
    exchange(inputTxt)


def exchange(text):
    countNum = 0
    for i in text:
        if i == "(":
            countNum += 1
        elif i == ")":
            countNum -= 1
        else:
            continue

        if countNum < 0:
            print("It's not correct")
            return False
    if countNum != 0:
        print("It's not correct")
        return False

    print("it is correct")
    return True


if __name__ == "__main__":
    main()
