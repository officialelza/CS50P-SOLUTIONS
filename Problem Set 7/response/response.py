from validator_collection import checkers

def main():
    print(validation(input("What's your email address? ")))

def validation(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()
