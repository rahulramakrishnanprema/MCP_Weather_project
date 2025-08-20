from calculator import calculate

if __name__ == "__main__":
    print("Simple Command-Line Calculator")
    print("Enter 'quit' to exit.")

    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'quit':
            break
        result = calculate(expression)
        print(f"Result: {result}")

