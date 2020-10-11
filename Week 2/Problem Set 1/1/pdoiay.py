"""Calculating balance after one year of paying only the minimum."""

# balance = 5000
# annualInterestRate = .18
# monthlyPaymentRate = .02

num_months = 12

for i in range(num_months):
    monthly_payment = balance * monthlyPaymentRate
    balance = (balance - monthly_payment) * \
    (1 + annualInterestRate / num_months)

print("Remaining balance: " + str(round(balance, 2)))
