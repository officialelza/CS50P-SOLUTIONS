def main():
    amount_due = 50
    while True:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            amount_due -= coin
            if amount_due <= 0:
                print("Change Owed:",abs(amount_due))
                break

main()
