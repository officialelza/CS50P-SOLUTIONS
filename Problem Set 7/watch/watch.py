import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)"', s)
    if match:
        return ("https://youtu.be/"+ match.group(1))
    else:
        return None

if __name__ == "__main__":
    main()

#match = re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(.+)"', s)
"""After embed/(.+) if you give without a question mark what happens is that
the link will be captured but... it will capture till the last double qoutes
which is reallly unnecessary. so to cure that we put ? after +"""
