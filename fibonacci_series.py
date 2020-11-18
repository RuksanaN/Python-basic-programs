i=0
a=0
b=1
show=0
n=int(input("Type a limit:"))
if(n>=2):
  print(a)
  print(b)
  while(i<n-2):
    show=a+b
    print(show)
    a=b
    b=show
    i=i+1
elif n==1:
    print(a)
else:
    print("no value")



