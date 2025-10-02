def safe_divide(numerator, denominator):
    """
    Perform division, handling potential errors like division by zero and non-numeric inputs.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return "The result of the division is " + str(numerator / denominator)
    except ValueError:
        return "Error: Please enter numeric values only."