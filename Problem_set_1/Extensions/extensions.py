type = input("File name: ").lower().strip()

name, format = type.split(".")

if format in ["gif", "jpg", "jped", "png"]:
    print(f"image/{format}")
elif format in ["pdf", "zip"]:
    print(f"application/{format}")
elif format == "txt":
    print("text/plain")

else:
    print("application/octet-stream")