import re
def main():
    p = convert(input("Hours: "))
    print(p)

def convert(s):
    # 9:00 AM to 5:00 PM --> 09:00 to 17:00
    # 9 AM to 5 PM
    # 10:30 PM to 8 AM

    INPUT_TIME = re.search( r'^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$' , s)
    if INPUT_TIME:
        Start_hour = int(INPUT_TIME.group(1))
        Start_min = INPUT_TIME.group(2)
        Start_phase = INPUT_TIME.group(3)

        End_hour = int(INPUT_TIME.group(4))
        End_min = INPUT_TIME.group(5)
        End_phase = INPUT_TIME.group(6)

        start = time_converter( Start_hour , Start_min , Start_phase )
        end = time_converter( End_hour , End_min , End_phase )

        return f"{start} to {end}"

    else:
        raise ValueError

def time_converter( hour, min, ph ):
    # HOUR CONVERSION
    if hour == 12:
        if ph == "AM":
            HOUR = "00"
        else:
            HOUR = '12'

    else:
        if ph == "AM":
            HOUR = f"{hour:02}"
        else:
            HOUR = f"{hour+12:02}"

    # MINUTE CONVERSION
    if min == None:
        MIN = "00"
    else:
        MIN = f"{min:02}"

    return f"{HOUR}:{MIN}"



if __name__ == "__main__":


    main()
