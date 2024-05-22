def grocery(groceryList,item):
    try:
        if isinstance(item,str) and item.isalpha():
            groceryList.append(item)
            return groceryList
        else:
            raise ValueError("Invalid Input: Only Strings are allowed.")
    except ValueError as ve:
        print(ve)
        # return groceryList
    
    
def main():
    groceryList = []
    control = True
    while control:
        try:
            item = input("Item: ")
            if item == "d":
                for i in obj:
                    print(i)
                exit()
            else:
                obj = grocery(groceryList,item)
                
                # print(obj)
                
        except ValueError as e:
            print(e)
    

        
    
if __name__ == "__main__":
    main()





# def grocery(groceryList, item):
#     if isinstance(item, str) and item.isalpha():
#         groceryList.append(item)
#     else:
#         raise ValueError("Invalid input. Only pure strings are allowed.")
#     return groceryList

# def main():
#     groceryList = []
#     control = True
#     while control:
#         try:
#             item = input("Item: ")
#             if item == "d":
#                 exit()
#             else:
#                 obj = grocery(groceryList, item)
#                 print(obj)
#         except ValueError as e:
#             print(e)

# if __name__ == "__main__":
#     main()
