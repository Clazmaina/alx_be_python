def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        return None
    except ValueError:
        return None
    else:
        return result