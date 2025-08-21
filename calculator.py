import re

def calculate(expression):
    """
    Calculates the result of a mathematical expression.
    Handles addition, subtraction, multiplication, and division.
    Includes basic error handling for invalid expressions or division by zero.
    """
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', expression)

    if not match:
        return "Error: Invalid expression format. Please use 'number operator number' (e.g., '5 + 3')."

    num1, operator_symbol, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)

    try:
        if operator_symbol == '/' and num2 == 0:
            return "Error: Division by zero is not allowed."
        result = operators[operator_symbol](num1, num2)
        return round(result, 2)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except KeyError:
        return "Error: Invalid operator. Supported operators are +, -, *, /."
    except Exception:
        return "Error: An unexpected error occurred."

