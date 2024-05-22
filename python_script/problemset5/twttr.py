def omitVowels(tweet):
    vowelOmittxt = ""
    for var in tweet:
        if var in ["a","e","i","o","u","A","E","I","O","U"]:
            continue
        else:
            vowelOmittxt = vowelOmittxt + var
    return vowelOmittxt
    
    
def main():
    tweet = input().strip()
    print("Text without Vowels: ", omitVowels(tweet))
    
if __name__ == "__main__":
    main()