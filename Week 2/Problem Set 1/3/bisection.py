"""Uses bisection search to efficiently calculate the monthly payment required
   to pay off a debt."""

num_months = 12

# balance = 999999
# annualInterestRate = .18

# Minimum monthly payment is if no interest
low = balance / num_months
# Maximum monthly payment is if you waited until the end of the
# year to pay off the debt
high = (balance * ((1 + annualInterestRate / num_months) ** num_months)) / num_months
epsilon = .005

def bisection_search_amount(low, high, bal, rate, epsilon):
    """Searches for the accurate monthly payment that will pay off a debt by
    splitting the problem in half each time."""
    b = bal
    while True:
        mid = (low + high) / 2
        for i in range(12):
            b = (b - mid) * (1 + rate / num_months)
        # Close to correct amount
        if abs(b) <= epsilon:
            return mid
        # Not enough
        elif b > 0:
            low = mid
        # Too much
        elif b < 0:
            high = mid
        b = bal


monthly = bisection_search_amount(low, high, balance, annualInterestRate, epsilon)
print("Lowest Payment:", str(round(monthly, 2)))
