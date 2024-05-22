# import random
# coin = random.choice(["heads","tails"])

# print(coin)


# from random import choice
# name = input("Whos the imposter? ")
# imposter = choice(["Rashid","Taqi","Arqum","Hamza","Ibad","Umer"])
# if name==imposter:
#     print("YOu won, "+name+" is the imposter")
# else:
#     print("you loose "+imposter+" is the imposter")
    


import random
cards=["jack","queen","king","joker","dimond","heart"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)