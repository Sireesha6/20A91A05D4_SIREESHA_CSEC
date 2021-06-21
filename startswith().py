s="python"
#checking the string s is started with K or not
res=s.startswith("K")#Captital-K
print("startswith()")
print (res)#False
print("startswith()")
res=s.startswith("P")#Captital-P
print (res)#False
res=s.startswith("p",0,4)
print("starts with() start and end index")
print(res)
res=s.startswith("p")
print(res)#True


'''
startswith()
False
startswith()
False
starts with() start and end index
True
True
'''
