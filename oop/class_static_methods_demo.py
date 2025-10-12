# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
