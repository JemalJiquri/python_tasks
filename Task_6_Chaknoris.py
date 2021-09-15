import requests
import json


def main():
    startJoke()


def startJoke():
    jokeArr = []
    openJokes(jokeArr)
    while True:
        command = input("A new joke: 1 \nSaved joke: 2\nExit: 0 \nYour choice: ")
        try:
            if int(command) == float(command) and 0 <= int(command) < 3:
                command = int(command)
            else:
                continue
        except ValueError:
            continue

        if command == 1:
            tellMeARandomJoke(jokeArr)
        elif command == 2:
            tellMeAOldJoke(jokeArr)
        elif command == 0:
            saveJokes(jokeArr)
            break


def tellMeARandomJoke(jokes):
    f = r"http://api.icndb.com/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)
    if tt["value"]["joke"] not in jokes:
        jokes.append(tt["value"]["joke"])
    print(tt["value"]["joke"])
    return tt["value"]["joke"]


def tellMeAOldJoke(jokes):
    for i in jokes:
        print(i + "\n")


def saveJokes(jokes):
    f = open("jokesAboutChaknoris.txt", "+w")
    f.write(json.dumps(jokes))
    f.close()


def openJokes(jokes):
    try:
        f = open("jokesAboutChaknoris.txt", "r")
        for x in json.loads(f.read()):
            jokes.append(x)
        f.close()
    except FileNotFoundError:
        f = open("jokesAboutChaknoris.txt", "w")
        f.write(json.dumps([]))
        f.close()
    except json.decoder.JSONDecodeError:
        return


if __name__ == '__main__':
    main()
