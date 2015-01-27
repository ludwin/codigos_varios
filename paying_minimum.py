total_paid=0
for i in range(12):
	minimum_payment=balance*monthlyPaymentRate
	unpaid_balance=balance-minimum_payment
	interest=annualInterestRate/12.0*unpaid_balance
	balance=unpaid_balance+interest
	total_paid=total_paid+minimum_payment
	i=i+1
	print "Mont: ",i
	print " Minimum monthly payment",round(minimum_payment,2)
	print" Remaining Balance ",round(balance,2)
print" Total paid",round(total_paid,2)
print "Remaining balance:", round(balance,2)
