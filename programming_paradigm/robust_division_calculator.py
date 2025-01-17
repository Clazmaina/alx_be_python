def safe_divide(numerator, denominator):
   try:
        # Convert arguments to floats for potential non-integer input
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Division by zero")
        return numerator / denominator
   except ZeroDivisionError as e:
        return f"Error: {e}"
   except ValueError as e:
        return f"Error: Invalid input. Please provide numeric values. {e}"