def pay(hourlyWage, nHours):
    if nHours <= 40:
        return hourlyWage*nHours
    else:
        return 1.5*hourlyWage*(nHours-40)+hourlyWage*40

print (pay(12, 20))

print (pay(100, 50))




def monthlyPayment(P, r, n):
    return P*(1+r/12)**(12*n)*(r/12)/((1+r/12)**(12*n)-1)

print (monthlyPayment(400000, 4.5/100, 30))



def printBalance(P,r,n):
    for k in range(31):
        B=P*((1+r/12)**(12*n)-(1+r/12)**(12*k))/((1+r/12)**(12*n)-1)
        print ('Year: ', k,' Balance: ', B)

print (printBalance(400000, 0.045, 30))
    
        
