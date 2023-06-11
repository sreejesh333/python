

def whileloop(n,i):
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers


numbers = []
a = whileloop(6,0)
print(a)
for i in a:
    print(i)

