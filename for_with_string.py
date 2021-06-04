name=input("Enter name")
print(name)
print(name[0])
size=len(name)
print("Size of %s is %d" %(name,size))
print("First approach of string access without index")
for i in name:
    print(i)
print("Second approach of string access with index ")
for i in range(size):
    print(name[i])


'''
Output
Enter namePython Class
Python Class
P
Size of Python Class is 12
First approach of string access without index
P
y
t
h
o
n
 
C
l
a
s
s
Second approach of string access with index 
P
y
t
h
o
n
 
C
l
a
s
s'''
