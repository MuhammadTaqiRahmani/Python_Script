def cent(amount_due,insert_amount):
    control = True
    while control:
        amount_due = amount_due - insert_amount
        print("Amount Due: " , amount_due)
        if amount_due == 0:
            break
        insert_amount = int(input("Insert Coin: "))

            
def main():
    amount_due = 50
    print("Amount Due: ", amount_due)
    insert_amount = int(input("Insert Coin: "))
    cent(amount_due,insert_amount)


main()
    