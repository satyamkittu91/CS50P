import sys
from PIL import Image, ImageOps

def main():
    check_cl_argument()

    try:
        #the doll image
        doll = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #the shirt image
    shirt = Image.open("shirt.png")

    # a variable size with the size of shirt image
    size = shirt.size

    # A vairable named final that stores the doll image which align with
    # the shirt image's size
    final = ImageOps.fit(doll, size)

    #pasting the shirt on top of the doll image
    final.paste(shirt, shirt)

    #saving the file
    final.save(sys.argv[2])








def check_cl_argument():
    # check for the number of sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many commnad-line arguments")
    #check if the command is a csv file
    filename1, exte1 = sys.argv[1].split(".")
    filename2, exte2 = sys.argv[2].split(".")
    exts = ["png", "jpg", "jpeg"]
    if exte1 not in exts:
        sys.exit("Invalid input")
    elif exte2 not in exts:
        sys.exit("Invalid output")

    if exte1 != exte2:
        sys.exit("Input and output have different extensions")

    

if __name__ == "__main__":
    main()