Username=input()
if(Username=="CSEC"):  #Outer if block
    password=input()
    if(password=="AEC"):   #Inner if block
        print("Valid student")
    else:    #Executed when inner if block is false
         print("Invalid password")
else:         ##Executed when outer if block is false
    print("Invalid Username! Please check it")
    
#oUTPUT

#CSEC
#AEC
#Valid student


#CSEC
#ADC
#Invalid password


#CSEB
#Invalid Username! Please check it
