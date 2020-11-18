a=input("Get a number:")
num=a
sum=0
rem=0
a=int(a)
while a>0:
    rem=a%10
    sum=sum+(rem**len(num))
    a=a//10
if int(num)==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

