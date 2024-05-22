import pytest
from bank import Greeting

def test_1():
    assert Greeting("hello") == 0
    assert Greeting("Hello") == 0
    assert Greeting("HELLO, brother") == 0
def test_2():
    assert Greeting("hey , how are you?") == 20
    assert Greeting("HEY!!!") == 20
    assert Greeting("How are you sir") == 20
    assert Greeting("Hoo") == 20

def test_3():
    assert Greeting("who are you?") == 100
    assert Greeting("WAO") == 100
    assert Greeting("BIngo , BangO") == 100
    
if __name__ == "__main__":
    pytest.main()









# import pytest
# from bank import Greeting

# def test_1():
#     assert Greeting("hello") == (0,"$")
#     assert Greeting("Hello") == (0,"$")
#     assert Greeting("HELLO, brother") == (0,"$")
# def test_2():
#     assert Greeting("hey , how are you?") == (20,"$")
#     assert Greeting("HEY!!!") == (20,"$")
#     assert Greeting("How are you sir") == (20,"$")
#     assert Greeting("Hoo") == (20,"$")

# def test_3():
#     assert Greeting("who are you?") == (100,"$")
#     assert Greeting("WAO") == (100,"$")
#     assert Greeting("BIngo , BangO") == (100,"$")
    
# if __name__ == "__main__":
#     pytest.main()


