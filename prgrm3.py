#What is the largest prime factor of the number 13195 ?



lar=1
for i in range(2,13195):
   if(13195%i==0):
      for j in range(2,i):
         if(i%j==0):
           break
      else:
        if(i>lar):
           lar=i
         
         
print(lar)
