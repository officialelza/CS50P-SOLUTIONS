def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove $ and convert it to float
    d=float(d.lstrip('$'))
    return d


def percent_to_float(p):
    #remove % and convert it to float
    p=float(p.rstrip('%'))/100
    return p

main()
