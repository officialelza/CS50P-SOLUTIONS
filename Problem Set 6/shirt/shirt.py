import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:

        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        form = [".jpg",".png","jpeg"]
        if input[1].lower() not in form or output[1].lower() not in form:
            sys.exit("Invalid output")
        elif input[1].lower() != output[1].lower() :
            sys.exit("Input and Output have different extensions")

        else:
            try:
                shirt = Image.open("shirt.png")
                with Image.open(sys.argv[1]) as a:
                    cropped = ImageOps.fit(a , shirt.size)
                    cropped.paste(shirt , mask = shirt)
                    cropped.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit("Input does not Exist")



if __name__ == "__main__":
    main()
