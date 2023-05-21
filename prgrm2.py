#Find the sum of even numbers in a fibanocci series whose limit is 4000000


range=4000000
sum=0
a=1
b=1

while b < range:
   if b%2 == 0:
     sum += b
     
   c = a+b
   a,b = b,c
   
print(sum)
      
