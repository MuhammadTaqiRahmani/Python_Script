



# def camel_to_snake(camel_case):
#     snake_case = ''
#     for char in camel_case:
#         if char.isupper():
#             snake_case = snake_case + '_' + char.lower()
#         else:
#             snake_case = snake_case + char
#     return snake_case.lstrip('_')

# # Test the function
# camel_case_input = input("Enter characters: ")
# snake_case_output = camel_to_snake(camel_case_input)
# print("Snake case:", snake_case_output)



# def kebab_case(camel_case):
#     kebabcase = ""
#     for i in camel_case:
#         if i.isupper():
#             kebabcase = kebabcase +"-"+ i.lower()
#         else:
#             kebabcase = kebabcase + i
#     return kebabcase
    
    
# text = input("Enter camel case characters: ")
# print(kebab_case(text))














# def kebab_to_snake(kebab):
#     snake_case = ""
#     for i in kebab:
#         if i == "-":
#             snake_case = snake_case + "_" 
#         else:
#             snake_case = snake_case + i
#     return snake_case
            
    
    
    
# kebab = input("Enter the kebab characters: ")
# print(kebab_to_snake(kebab))

# HelloWorld

def pascal_to_camel(pascal):
    camel_case = ""
    camel_case = pascal[0].lower()
    camel_store = camel_case
    for char in pascal[1:]:
        camel_store =  camel_store + char
    return camel_store 
        
    

pascal = input("Enter pascal characters: ")
print(pascal_to_camel(pascal))
        






# def pascal_to_camel(pascal):
#     camel_case = ""
#     for char in range(len(pascal)):
#         if pascal[char].isupper() and pascal[0].isupper():
#             camel_case = camel_case + pascal[0].lower()
#         else:
#             camel_case = camel_case + pascal[char]
#     return camel_case

# pascal = input("Enter pascal characters: ")
# print(pascal_to_camel(pascal))















