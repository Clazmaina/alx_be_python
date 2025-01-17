import sys
from robust_division_calculator import safe_divide # type: ignore
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)  # Exit with an error code

    numerator = float(sys.argv[1])  # Convert to float for potential non-integer input
    denominator = float(sys.argv[2])  # Convert to float for potential non-integer input

    result = safe_divide(numerator, denominator)

    if result is not None:  # Check if result is not an error message
        print(result)
    else:
        print("Error occurred during division.")

if __name__ == "_main_":
    main()