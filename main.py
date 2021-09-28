x = int(input())
pr=1
for i in range ( 2 , int(x/2)+1):
    if x%i ==0:
        pr=0
if pr ==0:
    print ("Nu este Prim")
else :
    print ("Prim")
