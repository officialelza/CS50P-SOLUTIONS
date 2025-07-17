def main():
    d = {}
    while True:
        try:
            items = input().lower().strip()
            if items not in d:
                d.update({items:1})
            else:
                d[items] += 1
        except EOFError:
            sd=sorted(d)
            for i in range(len(sd)):
                print(d[sd[i]],sd[i].upper())
            break
main()
