def main():
    month = ["January","February","March","April","May",
    "June","July","August","September","October","November","December"]

    while True:
        try:
            user_input = input("Date: ").strip().title()
            if "/" in user_input:
                L = []
                l = user_input.split("/")
                for i in l:
                    L.append(int(i))
                if L[0] <= 12 and L[1] <= 31:
                    print(f"{L[2]}-{L[0]:02}-{L[1]:02}")
                    break
                else:
                    continue
            elif "," in user_input:
                user_input = user_input.replace(",","")
                months, day, year = user_input.split()
                months = month.index(months)+1
                if int(day)<=31:
                    print(f"{int(year)}-{months:02}-{int(day):02}")
                    break
                else:
                    continue
        except ValueError:
            continue

main()
