import unittest
import xmlrunner
import calculator  # Assuming you've saved your calculator code in a file named "calculator.py"

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(0, 0), 0)

    # Similarly, write test methods for other functions...

if __name__ == '__main__':
    unittest.main()
