def main():
    user_input=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    check(user_input)

def check(k):
    if k == "forty two" or k == "forty-two" or k == "42":
        print("Yes")
    else:
        print("No")

main()
