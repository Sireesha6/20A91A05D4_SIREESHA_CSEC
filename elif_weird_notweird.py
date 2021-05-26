n=int(input("Enter n value"))
if (n%2!=0):
    print("weird")
elif(n>=2 and n<=5):
    print("Not weird")
elif(n>=6  and n<=20):
    print("Weird")
elif(n>20):
    print("Not weird")


#OUTPUT    
#Enter n value2
#Not weird


#Enter n value6
#Weird


#Enter n value20
#Weird


#Enter n value22
#Not weird    
