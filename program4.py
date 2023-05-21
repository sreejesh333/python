#Find the largest palindrome made from the product of two 3-digit numbers.

lar=1
for i in range(100,1000):
   for j in range(100,1000):
        a=i*j
        c=a
        s=0
        while(c!=0):
           b = c%10
           s=s*10+b
           c=c//10
        if(a == s):
          if(s>lar):
            lar=s
           
print(lar)
           
           
           
