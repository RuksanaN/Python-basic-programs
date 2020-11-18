n=int(input("Enter a number:"))
if(n==1 or n==2):
    print(n,"is prime")
for i in range(2,n):
    if(n%i==0):
        print(n,"is not prime")
        break
    else:
        print(n,"is prime")
        break
