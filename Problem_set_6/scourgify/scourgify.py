import sys
import csv

def main():
    check_cl_argument()
    list1 = []
    try:
        #reading the csv file
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                list1.append({'first': first.lstrip(), "last":last, "house":row['house']})
        

        
    except FileNotFoundError:
        sys.exit(f"file {sys.argv[1]} does not exist")

    #creating and writing in new formatted csv file
    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        #writer.writerow({"first": "first", "last": "last", "house":"house"})
        writer.writeheader()
        for row in list1:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})











def check_cl_argument():
    # check for the number of sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many commnad-line arguments")
    #check if the command is a csv file
    if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
        



if __name__ == "__main__":
    main()