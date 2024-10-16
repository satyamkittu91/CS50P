import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r'"https?://(www\.)?youtube.com/embed/([a-zA-Z0-9_-]+)"', s):
        return("https://youtu.be/"+link.group(2))
    

if __name__== "__main__":
    main()