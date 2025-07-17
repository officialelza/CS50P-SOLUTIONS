def main():
    user_input=input("Greeting: ").lower()
    output = is_hello(user_input)
    print(f"${output}")

def is_hello(n):
    if n == "hello" or n.startswith('hello'):
        return 0
    elif n.startswith('h'):
        return 20
    else:
        return 100
    
if __name__ == "__main__" :
    main()
