

from numpy import random

def passgenerater():
    
    
    password=[]
    password.append( chr(random.randint(33,47)) )#add special_characters
    password.append( chr(random.randint(58,65)) )
    password.append( chr(random.randint(91,96)) )
    password.append( chr(random.randint(123,127)) )
    for i in range(4):
        password.append( chr(random.randint(65,91)) ) #add capital_letters       
        password.append( chr(random.randint(97,123)) ) #add small_letters
        password.append( chr(random.randint(48,58))) #add numbers 
    
    random.shuffle(password)# randomly content order
    
    Final_pass=''.join(password)
    return Final_pass
        
        
newpass = passgenerater()    
print(newpass)