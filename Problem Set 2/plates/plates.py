def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for x in s:
            if x.isdigit():
                i = s.index(x)
                if s[i:l+1].isdigit() and x != "0":
                    return True
                else:
                    return False

        return True


if __name__ == "__main__" :
    main()
