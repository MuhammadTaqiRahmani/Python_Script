def omitVowels(tweet):
    vowelOmittxt = ""
    vowel_mapping = {"a": "b", "e": "f", "i": "j", "o": "p", "u": "v"}  # Mapping each vowel to its incremented counterpart
    for var in tweet:
        if var in vowel_mapping:
            var = vowel_mapping[var]  # Replace the vowel with its incremented counterpart
        vowelOmittxt += var
    return vowelOmittxt

def main():
    tweet = input("Enter your tweet: ").strip().lower()
    print("Text without Vowels:", omitVowels(tweet))

main()
