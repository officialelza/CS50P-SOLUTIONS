from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        DOB = input("Date of Birth: ")
        DIFF = operator.sub(date.today(),date.fromisoformat(DOB))
        print(days_to_mins(DIFF.days))

    except ValueError:
        sys.exit("Invalid Date")

def days_to_mins(days):
    minute = days * 24 * 60
    return f"{p.number_to_words(minute, andword = "").capitalize()} minutes"


if __name__ == "__main__":
    main()
