def main():
    time=input('What time is it? ').strip()
    x= convert(time)
    if 7 <= x <= 8:
        print('Breakfast time')
    elif 12 <= x <=13:
        print('Lunch time')
    elif 18 <= x <= 19:
        print('Dinner time')
    else:
        pass

def convert(t):
    hours,minutes=t.split(':')
    t=float(hours)+(float(minutes)/60)
    return t

if __name__ == "__main__":
    main()
