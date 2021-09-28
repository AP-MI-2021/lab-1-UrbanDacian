
a=int(input())
b=int(input())
k=0
i=a
while k==0:
    if a%i==0 and b%i==0:
        k=1
    else:
        i -=1
print (i)