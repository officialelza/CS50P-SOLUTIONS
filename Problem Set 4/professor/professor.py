import random

def main():
    lvl = get_level()
    sc = generate_integer(lvl)
    print("Score:",sc)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break

        except:
            pass

    return level


def generate_integer(l):
    level = int(l)
    count = 0
    for i in range(10):
        flag = 0
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)

        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)

        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
        for j in range(3):
            sum = int(input(f"{x} + {y} = "))
            if (sum == x+y):
                flag = 1
                count +=1
                break
            else:
                print("EEE")
        if flag == 0:
            print(f"{x} + {y} = {x + y}")

    return count


if __name__ == "__main__" :
    main()
