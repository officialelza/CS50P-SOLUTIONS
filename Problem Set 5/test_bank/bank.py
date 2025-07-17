
def main():
    user_input=input("Greeting: ").lower()
    output = is_hello(user_input)
    print(f"${output}")

def value(greeting):
    greeting = greeting.lower()
    if greeting == "hello" or greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100
if __name__ == "__main__" :
    main()
