import unittest


def ex1(string):                                              #Reverse a string
    return (string[::-1])


def ex2(nr):                                                  #Check if a number is even or odd
    if nr % 2 == 0:
        return ("Number is even")
    else: return ("Number is odd")


def ex3(lst):                                                 #Find the largest number in a list
    if not lst:
        return None
    largest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


def ex4(lst):                                                 #Find the smallest number in a list
    if not lst:
        return None
    smallest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest


def ex5(firstNumber,secondNumber):                            #Check if a number is divisible by another number
    if firstNumber % secondNumber == 0:
        return ("The first number is divisible by the second number")
    else:
        return ("The first number is not divisible by the second number")


#Unit tests


class TestEx1(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(ex1("hello"), "olleh")
        self.assertEqual(ex1("racecar"), "racecar")
        self.assertEqual(ex1("12345"), "54321")
        self.assertEqual(ex1(""), "")


class TestEx2(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(ex2(0), "Number is even")
        self.assertEqual(ex2(2), "Number is even")
        self.assertEqual(ex2(-4), "Number is even")

    def test_is_odd(self):
        self.assertEqual(ex2(1), "Number is odd")
        self.assertEqual(ex2(-3), "Number is odd")


class TestEx3(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(ex3([]))

    def test_single_item_list(self):
        self.assertEqual(ex3([5]), 5)

    def test_list_with_duplicates(self):
        self.assertEqual(ex3([1, 2, 3, 4, 4]), 4)

    def test_list_in_descending_order(self):
        self.assertEqual(ex3([9, 7, 4, 2]), 9)

    def test_list_in_random_order(self):
        self.assertEqual(ex3([2, 7, 1, 8, 4]), 8)


class TestEx4(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(ex4([]))

    def test_single_item_list(self):
        self.assertEqual(ex4([5]), 5)

    def test_list_with_duplicates(self):
        self.assertEqual(ex4([1, 2, 3, 4, 4]), 1)

    def test_list_in_ascending_order(self):
        self.assertEqual(ex4([2, 4, 7, 9]), 2)

    def test_list_in_random_order(self):
        self.assertEqual(ex4([2, 7, 1, 8, 4]), 1)


class TestEx5(unittest.TestCase):

    def test_divisible(self):
        self.assertEqual(ex5(10, 2), "The first number is divisible by the second number")
        self.assertEqual(ex5(100, 10), "The first number is divisible by the second number")
        self.assertEqual(ex5(49, 7), "The first number is divisible by the second number")

    def test_not_divisible(self):
        self.assertEqual(ex5(7, 3), "The first number is not divisible by the second number")
        self.assertEqual(ex5(11, 5), "The first number is not divisible by the second number")
        self.assertEqual(ex5(20, 7), "The first number is not divisible by the second number")

    def test_zero_divisor(self):
        self.assertRaises(ZeroDivisionError, ex5, 10, 0)


if __name__ == '__main__':
    unittest.main()