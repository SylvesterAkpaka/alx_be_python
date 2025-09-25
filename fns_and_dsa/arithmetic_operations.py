# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float | str: The result of the operation, or an error message for invalid input / division by zero
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
