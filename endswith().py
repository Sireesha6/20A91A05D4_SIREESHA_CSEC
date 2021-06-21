s=str(input("Enter string"))
res=s.endswith("N")
print("endswith()")
print(res)#False
res=s.endswith("n")
print("endswith()")
print(res)#True
res=s.endswith("o",0,4)
print("endswith()")
print(res)#False
res=s.endswith("o",0,5)
print("endswith()")
print(res)#True



'''
Enter stringpython
endswith()
False
endswith()
True
endswith()
False
endswith()
True'''

