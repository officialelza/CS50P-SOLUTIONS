import csv
import sys
def main():
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too Few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else :
        if sys.argv[1].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    with open(sys.argv[2],'w') as new_file:
                        writer = csv.DictWriter(new_file, fieldnames = ["first","last","house"])
                        writer.writeheader()
                        for student in reader:
                            last , first = student["name"].split(",")
                            house = student["house"]
                            writer.writerow({"first": first.strip(), "last": last.strip(),  "house" : house})

            except FileNotFoundError:
                sys.exit(f"could not read {sys.argv[1]}")
        else:
            sys.exit("Not a CSV file")
if __name__ == "__main__":
    main()
