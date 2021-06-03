n=int(input("Enter n value"))
i=1
flag=0
while(i<=n):
    if(n%i==0):
        flag=flag+1
    i=i+1    
if(flag==2):
    print("It is prime number")
else:
    print("It is not a prime number")


'''
OUTPUT
Enter n value54
It is not a prime number

Enter n value7
It is prime number'''
