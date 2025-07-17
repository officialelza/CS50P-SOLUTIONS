def convert(inp):
    con=inp.replace(":)","🙂").replace(":(","🙁")
    return(con)
def main():
    n=input()
    print(convert(n))
main()
