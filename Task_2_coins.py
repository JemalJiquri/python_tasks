def main():
    inputAmount = input("Write down the desired amount :")
    exchange(int(inputAmount))


def exchange(amount):
    answer = 0
    coinsArr = [50, 20, 10, 5, 1]
    while (amount != 0):
        if amount - coinsArr[0] >= 0:
            answer += 1
            amount -= coinsArr[0]
        else:
            del coinsArr[0]

    print(answer)


# ამ კონკრეტულ შემთხვევაში რადგან მონეტების რაოდნეობა და
# ღიტებულება არის განსაზღვრული ოპტიმალური ვარიანტია ეს
# წინააღმდეგ შემთხვევაში სორტირებები დასჭირდებოდა

if __name__ == "__main__":
    main()
