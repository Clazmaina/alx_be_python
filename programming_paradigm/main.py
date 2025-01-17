import sys
from robust_division_calculator import safe_divide # type: ignore
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)  

    numerator = float(sys.argv[1])  
    denominator = float(sys.argv[2])  
    print("Numerator:", numerator)
    print("Denominator:", denominator)

    result = safe_divide(numerator, denominator)

    if result is not None: 
        print(result)
    else:
        print("Error occurred during division.")

if __name__ == "_main_":
    main()