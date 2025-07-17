def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    result = gauge(perc)
    print(result)

def convert(fraction):
    while True:
        x , y = fraction.split("/")
        try:
            x , y = int(x) , int(y)
            if x <= y:
                percentage = (x / y)*100
                return round(percentage)
            else:
                fraction = input("Fraction: ")
                continue
        except (ZeroDivisionError , ValueError):
            continue

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage) + "%")

if __name__ == "__main__" :
    main()
