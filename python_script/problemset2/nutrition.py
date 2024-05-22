def calories(fruit):
    cals = {
        "apple":130,
        "avacado":50,
        "banana":110,
        "grapes":90,
        "lemon":15,
        "lime":20,
        "kiwifruit":90,
        "cantaloupe":50,
        "honeydew melon":50,
        "grapefruit":60,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweetcherries":100,
        "tangerine":50,
        "watermelon":100,

    }
    for cal in cals:
        if fruit in cal:
            return cals[fruit]
        else:
            return "Unknown fruit"
        
    
def main():
    fruit = input("Enter fruit name: ").strip().lower()
    print("Calories: ",calories(fruit))

main()