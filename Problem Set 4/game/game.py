import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            r = random.randint(1,level)
            while True:
                guess = int(input("Guess: "))

                if guess < r:
                    print("Too small!")

                elif guess > r:
                    print("Too large!")

                else:
                    print("Just right!")
                    raise EOFError

        except ValueError:
            continue
        except EOFError:
            break


if __name__ == "__main__":
    p= main()
    print(p)



