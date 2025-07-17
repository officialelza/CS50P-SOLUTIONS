import inflect

p = inflect.engine()

def main():

    L = []

    while True:

        try:
            user_input = input("Name: ").title().strip()
            L.append(user_input)

        except EOFError:
            New_list = p.join(L)
            print("\nAdieu, adieu, to",New_list)
            break



if __name__ == "__main__":
    main()