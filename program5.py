#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


sum=0
sum1=0
for i in range(1,101):
   sum=sum+i**2
   sum1=sum1+i
   
dif=sum1**2-sum
print(dif)
