import emoji
def main():
    a = input("Input: ")
    print("Output: ",sep="" , end="")
    print(emoji.emojize(a , language = "alias"))

main()
