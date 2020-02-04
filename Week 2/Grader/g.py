import math

def polysum(n, s):
    """Sums the area and square of the perimeter of an
    n-sided regular polygon with side length s."""
    def area(n, s):
        """Calculates the area of an n-sided regular polygon
        with side length s."""
        numerator = .25 * n * (s ** 2)
        denominator = math.tan(math.pi / n)
        return numerator / denominator
    def perimeter(n, s):
        """Calculates the perimeter of an n-sided regular polygon
        with side length s."""
        return n * s
    return round(area(n, s) + (perimeter(n, s) ** 2), 4)
