
def mysum(n):
    sum=0
    for i in range(n):
       # sum=n*(n+1)/2
        sum=sum(n-1)+n
        return sum
     
n1=mysum(5)
print ("The sum of 5 numbers "+str(n1))