def main():
    stepsNumber = int(input("input number of steps :"))
    stepCounter(stepsNumber)
    print("========================")
    print(recursFun(0, 0, stepsNumber))


def stepCounter(stepsNumber):
    steps = 0
    # მათემატიკური შესაძლო ვარიანტების გამომთვლელი ფორმულა
    c = lambda m, n: factorial(n) / (factorial(m) * (factorial(n - m)))
    for i in range(1, int(stepsNumber / 2) + 1):
        steps += c(i, stepsNumber - i)
    print(steps + 1)


def factorial(num):
    ansver = 1
    for i in range(1, num + 1):
        ansver *= i
    return ansver


# ეს ფუნქცია არის რეკურსიული იგივეს აკეთებს უბრალოდ რეკურსიულად
# და აშკარად უფრო სწრაფად წინა ვარიანტი დაწერილი მქონდა ასერომ ორივე დავტოვე :D


def recursFun(curent, stepSize, maxStep):
    if curent + stepSize > maxStep:
        return 0
    if curent + stepSize == maxStep:
        return 1
    return recursFun(curent + stepSize, 1, maxStep) + recursFun(
        curent + stepSize, 2, maxStep)


if __name__ == "__main__":
    main()
