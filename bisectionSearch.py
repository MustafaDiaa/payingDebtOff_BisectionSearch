import time
start_time = time.clock()	#begining of calculating seconds till end of calculating
balance = 99999999		#original credit card Balance
annualInterestRate = 0.18	#fixed annualInterestRate
upperBound = balance / 12.0	#highest guess for the monthlyPayment
lowerBound = (balance * (1 + annualInterestRate/12)**12)/12	#lowest guess for the monthlyPayment

while True:		#looping until  -0.01 < remainingBalance < 0.01
    remainingBalance = balance		#assign remainingBalance to balance
    monthlyPayment = (lowerBound+upperBound) / 2.0   #calculating the average of lower,upper Bound (Bisection Search)
   
    for count in range(0, 12):   #Calculating remaining balance after 12 months
        remainingBalance -= monthlyPayment	#discount monthlyPayment from remainingBalance
        remainingBalance = remainingBalance + (annualInterestRate/12 * remainingBalance)	#calculate remainingBalance + monthly Interests

    if remainingBalance < 0.01 and remainingBalance > -0.01:
        break			#break with the new monthlyPayment value
    if remainingBalance > 0:
        upperBound = monthlyPayment		#assign the highest guess for monthlyPayment to upperBound
    else:
        lowerBound = monthlyPayment		#assign the lowest guess for monthlyPayment to lowerBound

print 'Lowest Payment: ' + str(round(monthlyPayment,2))
print time.clock() - start_time, "seconds"	#find the time taken to calculate the monthlyPayment
