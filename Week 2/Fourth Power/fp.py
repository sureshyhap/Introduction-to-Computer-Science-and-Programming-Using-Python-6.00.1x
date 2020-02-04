def fourth_power(x):
    """Raises x to the 4th power."""
    def square(x):
        """Squares the input."""
        return x**2
    return square(square(x))
