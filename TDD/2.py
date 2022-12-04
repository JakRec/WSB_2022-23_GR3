import unittest

class Dodawanie(unittest.TestCase):
    def test_main(self):
        result = addition(3,6)
        assert result == 9

def addition(*args):
    total = 0
    for i in args:
        total = total + i
    return total

if __name__ == "__main__":
    unittest.main()