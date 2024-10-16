Amount_due = 50
total_paid = 0


while Amount_due > 0:
    print(f"Amount Due: {Amount_due}")
    pay = int(input("Insert Coin: "))
    if pay in [25, 10, 5]:
        Amount_due = Amount_due - pay
        total_paid = total_paid + pay

if total_paid >= Amount_due:
    print(f"change owed: {total_paid - 50}")