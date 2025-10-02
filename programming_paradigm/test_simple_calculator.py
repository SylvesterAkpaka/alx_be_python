import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # integers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

        # floats
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3, places=7)

        # large numbers
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    def test_subtraction(self):
        # integers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # floats
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=7)

        # identity-like checks
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_multiplication(self):
        # integers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

        # zero
        self.assertEqual(self.calc.multiply(12345, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

        # floats
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0, places=7)

        # commutativity
        self.assertEqual(self.calc.multiply(7, 8), self.calc.multiply(8, 7))

    def test_division(self):
        # normal divisions
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

        # floats
        self.assertAlmostEqual(self.calc.divide(2.5, 0.5), 5.0)

        # negative values
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

        # dividing by 1 and identity checks
        self.assertEqual(self.calc.divide(5, 1), 5.0)

    def test_divide_by_zero(self):
        # According to the provided implementation, divide returns None on division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_type_handling(self):
        # Ensure behaviour with floats and ints mixed
        self.assertAlmostEqual(self.calc.add(1, 2.5), 3.5)
        self.assertAlmostEqual(self.calc.subtract(1, 2.5), -1.5)
        self.assertAlmostEqual(self.calc.multiply(1, 2.5), 2.5)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

if __name__ == "__main__":
    unittest.main()
