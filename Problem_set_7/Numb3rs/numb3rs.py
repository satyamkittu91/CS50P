import sys

def main():
    if len(sys.argv) > 1:
        print(validate(sys.argv[1]))

    else:
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
            
        a1, a2, a3, a4 = ip.split(".")
        a1, a2, a3, a4 = int(a1), int(a2), int(a3), int(a4)

        if (0 <= a1 < 256) and (0 <= a2 < 256) and (0 <= a3 < 256) and (0 <= a4 < 256):
            return True
        else:
            return False
    
    except:
        return False
    


if __name__== "__main__":
    main()