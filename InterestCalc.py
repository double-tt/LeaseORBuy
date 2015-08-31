__author__ = 'piyushverma'
#References
#http://www.hughcalc.org/formula_deriv.php
#https://www.youtube.com/watch?v=FtAZD4R-Wh0

defaultCarPrice = 25000
carPrice = raw_input('\n Enter car price in $: ') or defaultCarPrice
print ('Car price is: $' + str(carPrice))
carPrice = float(carPrice)

defaultSalesTax = 10
salesTax = raw_input('\n Enter sales tax in %: ') or defaultSalesTax
print ('Sales tax is: ' + str(salesTax) + '%')
salesTax = float(salesTax)

defaultLoan = 22500
loanAmount = raw_input('\n Enter Loan Amount in $ (Rest is down payment): ') or defaultLoan
print ('Loan is: $' + str(loanAmount))
loanAmount = float(loanAmount)

defaultLoanPeriod = 3
loanPeriod = raw_input('\n Enter Loan payments in years: ') or defaultLoanPeriod
print ('Loan period is: ' + str(loanPeriod) + ' years')
loanPeriod = float(loanPeriod) * 12

defaultInterest = 3
interest = raw_input('\n Annual interest rate: ') or defaultInterest
print ('Annual interest rate is: ' + str(interest) + ' %')
interest = float(interest)/100/12

monthlyPayments = loanAmount * (interest * (1 + interest) ** loanPeriod) / ((1 + interest) ** loanPeriod - 1)

print ('\n Calculated monthly payment is: $' + str(round(monthlyPayments)))

defaultDiscountRate = 6
discountRate = raw_input('\n Expected annual rate of return otherwise: ') or defaultDiscountRate
print ('Annual discount rate is: ' + str(discountRate) + '%')
discountRate = float(discountRate)/100/12

presentValue = ( carPrice * (1 + salesTax / 100) - loanAmount ) + monthlyPayments * ((1 + discountRate) ** loanPeriod - 1) / (discountRate * (1 + discountRate) ** loanPeriod)

print ('\n Calculated present value of all payments is: $' + str(round(presentValue)))

defaultCarLife = 5
carLife = raw_input('\n Expected life of car before resale in years: ') or defaultCarLife
print ('Car will be sold after ' + str(carLife) + ' years')
carLife = float(carLife) * 12

defaultResalePrice = 0.5 * carPrice
resalePrice = raw_input('\n Expected resale price in $: ') or defaultResalePrice
print ('Car will be resold for $' + str(resalePrice))
resalePrice = float(resalePrice)

netPresentValue = presentValue - resalePrice * (1 / (1 + discountRate) ** carLife)

print ('\n Net present value of all payments including car resale is: $' + str(round(netPresentValue)))

defaultLeasePayment = 200
leasePayment = raw_input('\n Enter monthly lease payment in $ (w/o taxes): ') or defaultLeasePayment
print ('Monthly lease payment is: $' + str(leasePayment))
leasePayment = float(leasePayment)

defaultLeasePeriod = 3
leasePeriod = raw_input('\n Enter lease period in years: ') or defaultLeasePeriod
print ('Lease period is: ' + str(leasePeriod) + ' years')
leasePeriod = float(leasePeriod) * 12

leasePresentValue = leasePayment * (1 + salesTax / 100 ) * ((1 + discountRate) ** leasePeriod - 1) / (discountRate * (1 + discountRate) ** leasePeriod)

defaultDownPayment = 2500
downPayment = raw_input('\n Enter down payment for lease term in $: ') or defaultDownPayment
print ('Down payment is: $' + str(downPayment))
downPayment = float(downPayment)

defaultDispositionFee = 350
dispositionFee = raw_input('\n Enter disposition fee due at lease end in $: ') or defaultDispositionFee
print ('Disposition fee is: $' + str(dispositionFee))
dispositionFee = float(dispositionFee)

netLeasePresentValue = downPayment * (1 + salesTax / 100) + leasePresentValue + (dispositionFee * (1 / (1 + discountRate) ** leasePeriod))

print ('\n Calculated present value of all lease payments is: $' + str(round(netLeasePresentValue)))

print ('\n ################################################################################### \n')
print ('Own the car for ' + str(carLife/12) + ' years for $' + str(round(netPresentValue)) + ' or lease the car for ' + str(leasePeriod/12) + ' years for $' + str(round(netLeasePresentValue)) + '!' )
print ('\n ################################################################################### \n')


