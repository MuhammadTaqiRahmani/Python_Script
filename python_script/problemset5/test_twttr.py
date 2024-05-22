import pytest
from twttr import omitVowels

def test_shorten_with_vowels():
    assert omitVowels("Hello World") == "Hll Wrld"
    assert omitVowels("AEIOU") == ""
    assert omitVowels("This is a test") == "Ths s  tst"
    
def test_shorten_without_vowels():
    assert omitVowels("Hll Wrld") == "Hll Wrld"
    assert omitVowels("Ths s  tst") == "Ths s  tst"

if __name__ == "__main__":
    pytest.main()
