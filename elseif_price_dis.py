price=int(input("Enter the amount"))
if price>1000:
    dis=0.1*price
    bill=price-dis

elif price>2000:
    dis=0.2*price
    bill=price-dis

elif price>3000:
     dis=0.3*price
     bill=price-dis

elif price>5000:
     dis=0.4*price
     bill=price-dis

else:
    dis=0
    finalamt=price-dis
    print("No discount")
    
print("Discount:",dis)
print("Bill",bill)

#OUTPUT

#Enter the amount1500
#Discount: 150.0
#Bill 1350.0


#Enter the amount3000
#Discount: 300.0
#Bill 2700.0



#Enter the amount800
#No discount
#Discount: 0


#Enter the amount4000
#Discount: 400.0
#Bill 3600.0
