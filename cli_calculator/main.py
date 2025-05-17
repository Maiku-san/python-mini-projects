def calculate(expr):
    try:
        expr = expr.replace(" ", "")  # Strip spaces

        # Handle power first since it's two characters
        if "**" in expr:
            parts = expr.split("**")
            if len(parts) != 2:
                raise ValueError("Invalid power expression")
            a, b = float(parts[0]), float(parts[1])
            return a ** b

        # Try single-character operators
        for op in ['+', '-', '*', '/']:
            if op in expr:
                # Find the operator *after the first character* (to avoid splitting on negative sign)
                idx = expr.find(op, 1)
                if idx == -1:
                    continue

                left = float(expr[:idx])
                right = float(expr[idx+1:])

                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    if right == 0:
                        raise ZeroDivisionError
                    return left / right

        raise ValueError("No valid operator found")

    except ZeroDivisionError:
        return "❌ Cannot divide by zero."
    except ValueError as ve:
        return f"❌ {ve}"
    except Exception:
        return "❌ Invalid input."

def main():
    print("🧮 CLI Calculator (basic version)")
    print("Supported operations:\n+ (sum)\n- (subtraction)\n/ (division)\n* (multiplication)\n** (Exponentiation)")
    print("Type expressions like: 2 + 3, 5 / 2, or 3 ** 2")
    print("Type 'exit' or 'quit' to close the program\n")

    while True:
        expr = input(">> ")
        if expr.lower() in ("exit", "quit"):
            print("Goodbye! 👋")
            break

        result = calculate(expr)
        print("= ", result)

if __name__ == "__main__":
    main()