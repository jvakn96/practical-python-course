# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 3684.11
total_paid = 0.0
months_required = 0.0

for i in range(12):
    principal = principal * (1+rate/12) - extra_payment
    total_paid = total_paid + extra_payment
    months_required = months_required + 1
    
while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months_required = months_required + 1

print('Total paid', round(total_paid,2), 'over ', months_required)
