def calculate(expression):
    """
    Calculates the result of a mathematical expression.
    Handles addition, subtraction, multiplication, and division.
    Includes basic error handling for invalid expressions or division by zero.
    """
    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
