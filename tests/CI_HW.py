import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# UNit test that will Pass
class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 2), -4)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)


if __name__ == "__main__":
    print("Addition of 2 and 3 is:", add(2, 3))
    print("Subtraction of 5 from 10 is:", subtract(10, 5))
    print("Multiplication of 4 and 5 is:", multiply(4, 5))
    print("Division of 10 by 2 is:", divide(10, 2))
