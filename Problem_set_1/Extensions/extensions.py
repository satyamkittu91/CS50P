type = input("File name: ").lower().strip()

format = type.split(".")

if len(format) > 1:
    if format[-1] in ["gif", "jpg", "jpeg", "png"]:
        if format[-1] == "jpg":
            print("image/jpeg", end='')
        else:
            print(f"image/{format[-1]}", end='')
    elif format[-1] in ["pdf", "zip"]:
        print(f"application/{format[-1]}", end='')
    elif format[-1] == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")

else:
    print("application/octet-stream")
