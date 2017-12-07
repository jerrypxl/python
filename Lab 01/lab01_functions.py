def pay(hourlyWage,nHours):
    if nHours<=40:
        return hourlyWage*nHours

    elif 40<nHours<60:
        return hourlyWage*40+1.5*(nHours-40)*(hourlyWage)

    else:
        return hourlyWage*40+1.5*20*(hourlyWage)+(nHours-60)*hourlyWage*2
    
print(pay(10, 35))
print(pay(10, 45))
print(pay(10, 61))





def statement(LTransactions):
    totalWithdrawals = []
    totalDeposits = []
    for i in range (0, len(LTransactions)):
        if LTransactions[i] < 0:
            totalWithdrawals.append(LTransactions[i])
        elif LTransactions[i] > 0:
            totalDeposits.append(LTransactions[i])
    return [sum(totalWithdrawals), sum(totalDeposits)]

print (statement([30.95, -15.67, 45.56, -55.00, 43.78]))
print (statement([10, 20, 100]))






import math
def isPrime(M):
    sqrtM = math.floor(math.sqrt(M))
    for i in range(2, sqrtM + 1):
        if M%i == 0:
            return False
    return True

def countPrimes(N):
    y = []
    for i in range (2, N+1):
        if isPrime(i) == True:
            y.append(i)

    return len(y)

print (countPrimes(6))
print (countPrimes(13))






import math
def isPrime(M):
    sqrtM = math.floor(math.sqrt(M))
    for i in range(2, sqrtM + 1):
        if M%i == 0:
            return False
    return True

def sumInversePrimes(N):
    y = []
    x = []
    for i in range (2, N+1):
        if isPrime(i) == True:
            y.append(i)
    for i in range (0, len(y)):
        x.append(1/y[i])

    return sum(x)
            














            
    
