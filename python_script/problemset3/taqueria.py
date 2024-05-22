
def price(item_name,prc):
    try:
        PRICES = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
        
        for i in PRICES:
            if i in PRICES:
                prc = prc + PRICES[item_name]
                return prc
        else:
            raise ValueError("Invalid Item: Please Enter valid item.")
    except ValueError as ve:
        print(ve)

    
    
    
def item():
    control = True
    while control:
        try:
            itemf = input("ITEM: ").strip().title()
            if itemf.replace(" ", "").isalpha():  
                return itemf
            else:
                raise TypeError("Invalid Input: Please try again, avoid numbers or special characters.")
        except TypeError as te:
            print(te)

    
    
def main():
    control = True
    item_price = 0 
    while control:
        item_name = item()
        try:
            item_price = price(item_name,item_price)
            
            if item_price != None:
                print("PRICE: $",item_price)
            else:
                print()
        except ValueError:
            print("Invalid Input: Please try again")
        
    

main()



# def price(item_name, prc):
#     PRICES = {
#         "Baja Taco": 4.25,
#         "Burrito": 7.50,
#         "Bowl": 8.50,
#         "Nachos": 11.00,
#         "Quesadilla": 8.50,
#         "Super Burrito": 8.50,
#         "Super Quesadilla": 9.50,
#         "Taco": 3.00,
#         "Tortilla Salad": 8.00
#     }

#     if item_name in PRICES:
#         prc += PRICES[item_name]  # Increment prc with the price of the current item
#         return prc
#     else:
#         raise ValueError("Invalid Item: Please enter a valid item.")


# def item():
#     while True:
#         try:
#             itemf = input("ITEM: ").strip().title()
#             if itemf.isalpha():
#                 return itemf
#             else:
#                 raise TypeError("Invalid Input: Please try again, avoid numbers or special characters.")
#         except TypeError as te:
#             print(te)


# def main():
#     control = True
#     item_price = 0
#     while control:
#         item_name = item()
#         try:
#             item_price = price(item_name, item_price)
#             print("PRICE: $", item_price)
#         except ValueError as ve:
#             print(ve)


# main()

