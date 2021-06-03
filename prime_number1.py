n=int(input("Enter n value"))
i=1
flag=0
while(i<=n):
    if(n%i==0):
        flag=flag+1
        print("factor is",i)
    i=i+1
if(flag==2):
       print("It is a prime number")
else:
    print("It is not a prime number")
