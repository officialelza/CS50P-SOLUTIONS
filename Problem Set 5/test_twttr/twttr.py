def main():
    user_input = input("Input: ").strip()
    output = shorten(user_input)
    print(output)


def shorten(word):

    new_output=""
    Z = ['a','e','i','o','u','A','E','I','O','U']
    for i in word:
        if i not in Z:
            new_output+=i
    return new_output


if __name__ == "__main__" :
    main()
