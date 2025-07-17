import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(tabulate(table,headers,tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("Not a CSV file")

    else:
        pass

if __name__ == "__main__" :
    main()

