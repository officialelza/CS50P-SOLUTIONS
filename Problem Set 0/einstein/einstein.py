def main():
    m=int(input("m: "))
    print(einstein(m))

def einstein(mass):
    c=300000000
    E=mass*(c*c)
    return E

main()
