def main():
    user_input=input("file name: ").lower().strip()
    print(check(user_input))
def check(innp):
    if innp.endswith(".gif"):
        return('image/gif')
    elif innp.endswith('.jpeg') or innp.endswith('.jpg'):
        return('image/jpeg')
    elif innp.endswith('.png'):
        return('image/png')
    elif innp.endswith('.pdf'):
        return('application/pdf')
    elif innp.endswith('.txt'):
        return('text/plain')
    elif innp.endswith('.zip'):
        return('application/zip')
    else:
        return('application/octet-stream')

main()

