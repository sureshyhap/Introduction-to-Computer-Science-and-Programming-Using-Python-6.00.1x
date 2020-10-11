"""Calculates the minimum fixed payment amount to pay off a debt with
   interest in a year."""

num_months = 12

# balance = 4773
# annualInterestRate = .2
# Start monthly payment small, check to see if it pays off the debt, if not
# increment it by 10
minimum_monthly = 10

def calculate_balance(bal, inter, monthly):
    """Checks monthly to see if it will pay off the bal in a year at most."""
    for i in range(12):
        bal = (bal - monthly) * (1 + inter / num_months)
    # Balance has been paid off
    if bal <= 0:
        return True
    else:
        return False
    

while True:
    if calculate_balance(balance, annualInterestRate, minimum_monthly) == True:
        break
    else:
        minimum_monthly += 10

print("Lowest Payment:", str(minimum_monthly))
