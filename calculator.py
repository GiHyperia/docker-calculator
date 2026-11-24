"""Simple calculator configured through environment variables.

Environment variables:
    APP_NAME        Name shown in the output banner
    APP_AUTHOR      Author shown in the output banner
    CALC_OPERATION  add | sub | mul | div | pow
    CALC_NUM1       First operand (number)
    CALC_NUM2       Second operand (number)
"""
import os
import sys

OPERATIONS = {
    "add": ("+", lambda a, b: a + b),
    "sub": ("-", lambda a, b: a - b),
    "mul": ("*", lambda a, b: a * b),
    "div": ("/", lambda a, b: a / b),
    "pow": ("^", lambda a, b: a ** b),
}


def read_number(var_name):
    raw = os.getenv(var_name)
    if raw is None:
        sys.exit(f"[ERROR] Environment variable {var_name} is not set.")
    try:
        return float(raw)
    except ValueError:
        sys.exit(f"[ERROR] {var_name}='{raw}' is not a valid number.")


def main():
    app_name = os.getenv("APP_NAME", "Docker Calculator")
    author = os.getenv("APP_AUTHOR", "unknown")
    operation = os.getenv("CALC_OPERATION", "add").strip().lower()

    print("=" * 45)
    print(f" {app_name}  (author: {author})")
    print("=" * 45)

    if operation not in OPERATIONS:
        valid = ", ".join(OPERATIONS)
        sys.exit(f"[ERROR] Unknown operation '{operation}'. Valid: {valid}")

    num1 = read_number("CALC_NUM1")
    num2 = read_number("CALC_NUM2")
    symbol, func = OPERATIONS[operation]

    if operation == "div" and num2 == 0:
        sys.exit("[ERROR] Division by zero is not allowed.")

    result = func(num1, num2)
    print(f" Operation : {operation}")
    print(f" Result    : {num1:g} {symbol} {num2:g} = {result:g}")
    print("=" * 45)


if __name__ == "__main__":
    main()
