
def passchecker(password):
    spcharcoun=0
    cablittercoun=0
    smallittercoun=0
    numcoun=0
    if len(password)<8:
        print ("short password :the minimum number of characters for the password is 8")
        return 0
    elif len(password)>16 :
        print("too long password:the maximum number of characters for the password is 16")
        return 0
    else:
        for i in password:
            if (ord(i) in range(33,47))or (ord(i) in range(58,65)) or (ord(i) in range(91,96)) or (ord(i) in range(123,127)):
               spcharcoun +=1
               continue
               
            if ord(i) in range(65,91) :
                cablittercoun +=1
                continue
                
            if ord(i) in range(97,123) :
                smallittercoun +=1
                continue
                
            if ord(i) in range(48,58) :
                numcoun +=1
        
        if  spcharcoun==0:
            print("ypur password is missing  special_characters\n  ")
            
        if  cablittercoun==0:
            print("ypur password is missing  capital_letters\n  ")
            
        if  smallittercoun==0:
            print("ypur password is missing  small_letters\n  ")
            
        if  numcoun==0:
            print("ypur password is missing  numbers\n  ")
            
        if  spcharcoun==0 or  cablittercoun==0 or  smallittercoun==0 or numcoun==0 :
            return 0
        
        if spcharcoun>0 and  cablittercoun>0 and  smallittercoun>0 and numcoun>0 :
            print("good password\n ")
            return 1
        
            
print(passchecker("123456789hA*")  )          
                
    
    
    




    