import numpy as np
import pandas as pd
global bankBalance 
bankBalance=45000

global cc
global kk
cc=0
kk=0
global c1
global k1
c1=0
k1=0
global a
a=0
global buycou 
buycou=0
global rencou
rencou=0
global empPass
empPass=0
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.colheader_justify', 'center')

sellCars={ "toyota 2015": ["Prius","3500cc","Blue","4 g" , "leather seats , 4WD",6000,"available"],
          "mazda 2014": ["M3","3400cc","Green","3 g" , "Cruise control , Apple car play",8500,"available"],
          "mercedes 2018": ["C63","6400cc","White","7 g" , ",Panorama",12300,"available"],
          "mitsubishi 2013": ["Lancer","1600cc","Silver","4 g" , "Automatic gear ,sensors",4960,"available"],          
          "Kia 2020": ["Rio","1800","Black","4 g" , "Manual gear ,Stearing Control",9800,"available"]
        }
selledCarsinfo={}
bookedcar=dict({})

rentCars = { "Hondai 2015": ["MD","2600CC","Blue","4 g" , "leather seats ,4WD",60,"available"],
          "Audi 2014": ["A4","3400cc","Grey","4 g" , "Full Options ",90,"available"],
          "GMC 2018": ["C63","6400cc","Red","7 g" , "Panorama ,4WD",120,"available"],
          
    }


RENTEDcars={}


showRSoomBuy={ "BMW 2019": ["225","3500cc","Black","4 g" , "Automatic gear ,Heated seats",8200],
          "Volkswagen  2017": ["Golf","3700cc","Blue","4 g" , "Cruise control , Andorid Auto",7500],
          "PORSCHE  2020": ["911S","4200cc","White","8 g" , "Panorama , Turbo",12300],
          "OPEL  2013": ["vectra","1600cc","yellow","4 g" , "Manual gear ",4200],          
          "Ferrari  2020": ["f40 ","9200cc","Red","4 g" , "Manual gear , Super Charge",18600],
          "Kia 2020": ["Rio","1800","Black","4 g" , "Manual gear ,Stearing Control",36522],
          "Hondai 2015": ["MD","2600CC","Blue","4 g" , "leather seats ,4WD",8000],
        }

employees ={ "admin" :["a","ad","1"],
             "sales" :["b", 500,"s","456"],
             "sales2" :["d", 123,"s","888"],
             "accountant" :["c",650,"a", "789"]
                       

    }


userPassList=[]
for i in employees:
    userPassList.append(employees[i][0])

otherEmployees ={"cleaner":["anas",500]}
otherList=[]
for i in otherEmployees:
    otherList.append(otherEmployees[i][0])
 
accountantBuyMail=[]
accountantrentMail=[]
adminBuyMail=[]
adminrentMail=[]

employeesEmail=dict({})

adminEmail={"omar":["there is no sold cars today "],
            "ali": [" bmw was booked"],
            "khalid": [" ferari was rented "]}


avbSell=["Model","Engien","Color","Condition","Additions","Price","Status"]
avbRent=["Model","Engien","Color","Condition","Additions","Price per day","Status"]

avb2Sell=["Model","Engien","Color","Condition","Additions","Price "]

bookedSellCar=dict({})
rentedCars=dict({})
carList=list(showRSoomBuy.keys())

def isEmpty (Dict):
    conv=list(Dict.keys())
    if(len(conv)==0):
        return True 
    else:
        return False

def deletEmil (adminEmail,kye) :
    adminEmail.pop(kye)
    
def adminEmailSend(user):
    global kk
    global cc
    if user =="a":
        listemp=[]
        for i in employees:
           listemp.append(employees[i][0])
        print("\nfor which user do you want to send the email ")
        for i in range(1,len(listemp)+1):
            print(str(i)+"-"+str(listemp[i-1]))
            
        while(1):    
            pikUser=(input("\nplease enter the user number  :"))
            l=[]
            for i in range(1,len(listemp)+1):
                l.append(str(i))
                
            if(pikUser not in l ):
                    print("\nyour choise is wrong , please re-enter a right number .")
                    continue
            else : 
                    break    
        print("\n please write your E-mail here , when you done press Enter :\n")
        
        email=input("")
        redyemail="  : "+email
         
        
        x=str(listemp[int(pikUser)-1])
        lofkey=list(employeesEmail.keys())
        lofkey2=list(adminEmail.keys())
        if user==x:
            redyemail2= email
            print("\nyou send an E-mail for your self so it will be adressed as a Note .")
            x="Note"
            if len(lofkey2)==0:
                adminEmail[x]=redyemail2
            else:
                
             for i in lofkey2:
                if x == i:
                    kk +=1
             if kk==0:
                    adminEmail[x]=redyemail2
             
             if kk>0:
                x=x+str(kk)
                adminEmail[x]=redyemail2 
            
        else:
               
                
                cc =0
                    
                x=str(user.upper())+"-->"+x
                if len(lofkey)==0:
                    employeesEmail[x]=redyemail
                else:
                    
                 for i in lofkey:
                    if x == i:
                        cc +=1
                    if x+str(cc) == i :
                        cc +=1
                 if cc==0:
                        employeesEmail[x]=redyemail
                 
                 if cc>0:
                    x=x+str(cc)
                    employeesEmail[x]=redyemail 
                 
        
        
        
   
    
    
def adminEmails(user1):
    while(1):
            print("\n\n-----------------------------------------------")
            print("                 Admin E-mails Menu\n")
            print("1- Check  Inbox .")
            print("2- Send E-mails .")
            print("3- Delete E-mails .")
            print("4- Back to Menu .")
            print("-----------------------------------------------")    
            while(1):
               pick=input("\nplease enter your choise here : ")
               if(pick not in ["1","2","3","4"]):
                   print("\nyou put wrong Choise , please re-enter again .\n")
                   continue
               else:
                   break
            if (pick =="1"):
                empty=isEmpty(adminEmail)
                if empty :
                    print("\nYou don't have any E-mails .")
                else : 
                    print("\nThese are the E-mails  in your inbox :")
                    data=pd.DataFrame(adminEmail,index=["E-mails"])
                    newData=data.T
                    print("\n\n")
                    print(newData)
    
            if (pick =="2"):
                
                adminEmailSend(user1)
                
    
            if (pick =="3"):
              if(not isEmpty(adminEmail)):
                print("\n")
                while(1):
                    adminKyeList=list(adminEmail.keys())

                    print("\nThese are the E-mail  in your inbox : ")
                    print("-----------------------------------------------")    

                    data=pd.DataFrame(adminEmail,index=["E-mails"])
                    newData=data.T
                    print("\n")
                    print(newData )
                    print("-----------------------------------------------")    

                    print("\n")
                    for i in range(len(adminKyeList)):
                        print(str(i+1) + "   " + adminKyeList[i])
                    while(1):    
                        delPick=(input("\nplease enter the email number you want to delete : "))
                        l=[]
                        for i in range(1,len(adminKyeList)+1):
                            l.append(str(i))
                        
                        if(delPick not in l ):
                            print("\nyour choise is wrong , please re-enter a right number .")
                            continue
                        else : 
                            break
                    ifDel=input("\nIf you are sure to delete this E-mail press 1 ,else enter any thing : ")
                    
                    if ifDel =="1":
                        deletEmil(adminEmail,adminKyeList[int(delPick)-1])
                    conChoise=input("\nIf you want to continue deleting press * , else press any kye : ")
                    if conChoise == "*" and (not isEmpty(adminEmail)):
                        if ( isEmpty(adminEmail) )   :
                            print("\nYou don't have any E-mails .")  
                        continue 
                    else :
                        break
                    if isEmpty(adminEmail) : 
                        print("\nYou don't have any E-mails .")  
                        break
              else:
                print("\nYou don't have any E-mails .")  
                continue
            if (pick =="4"):
                break


def empEmailSend(user):
        global k1
        global c1
        global a
        if user !="a":
            listemp=[]
            for i in employees:
               listemp.append(employees[i][0])
            print("\nFor which user do you want to send the email ")
            for i in range(1,len(listemp)+1):
                print(str(i)+"-"+str(listemp[i-1]))
                
            while(1):    
                pikUser=(input("\nplease enter the user number : "))
                l=[]
                for i in range(1,len(listemp)+1):
                    l.append(str(i))
                    
                if(pikUser not in l ):
                        print("\nYour choise is wrong , please re-enter a right number .")
                        continue
                else : 
                        break    
            print("\nPlease write your E-mail here when you done press Enter :\n")
            
            email=input("")
            redyemail="  : "+email
             
            
            x=str(listemp[int(pikUser)-1])
            lofkey=list(employeesEmail.keys())
            lofkey2=list(adminEmail.keys())
            if user==x:
                redyemail2= email
                print("\nYou send an email for your self ,so it will be adressed as a Note .")
                x="Note "+str(user)
                
                if len(lofkey)==0:
                    employeesEmail[x]=redyemail2
                else:
                    
                 for i in lofkey:
                    if x == i:
                        k1 +=1
                 if k1==0:
                        employeesEmail[x]=redyemail2
                 
                 if k1>0:
                    x=x+str(k1)
                    employeesEmail[x]=redyemail2 
                
            elif x=="a" :
                y=user
               
                if len(lofkey2)==0:
                    adminEmail[y]=redyemail
                else:
                    
                 for i in lofkey2:
                    if y == i:
                        c1 +=1
                 if c1==0:
                        adminEmail[y]=redyemail
                 
                 if c1>0:
                    y=y+str(c1)
                    adminEmail[y]=redyemail 
                
            
            
            else:
               
                a =0
                    
                    
                x=str(user.upper())+"-->"+x
                if len(lofkey)==0:
                    employeesEmail[x]=redyemail
                else:
                    
                 for i in lofkey:
                    if x == i:
                        a +=1
                    if x+str(a) == i :
                        a +=1
                 if a==0:
                        employeesEmail[x]=redyemail
                 
                 if a>0:
                    x=x+str(a)
                    employeesEmail[x]=redyemail 
                 
                

def PassCheck():
    while(1):
        while(1):
            passWord=input("\nPassword : ")
            print("\n")
            if len(passWord)<8 :
                print("\nYour password is too short , it should be 8 charachters or more ,\nplease re-enter appropriate one. ")
                continue
            else:
                break
        up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        low=up.lower()
        num="0123456789"
        symb="(){}[],.:;\/*-+.!@#$%^&*_=|<>~"
        x=0
        y=0
        z=0
        b=0
        for i in range(len(passWord)):
            if passWord[i] in up :
                x =1             
            if passWord[i] in low :
                y =1
            if passWord[i] in num :
                z =1
            if passWord[i] in symb :
                b =1
        if (x+y+z+b) == 4:
            print("\nYour pasword  contains all the requirements .")
            return passWord
            
        else :
            if(x!=1):
                print("Your password doesn't contain capital letters.")
                
            if(y!=1):
                print("Your password doesn't contain small letters .")
                
            if(z!=1):
                print("Your password doesn't contain numbers .")
                
            if(b!=1):
                print("Your password doesn't contain symboles .")
            print("\nPlease re-enter an appropriate password .")
            continue          
def employeesEmailCheck(user):
    while(1):
            print("\n\n-----------------------------------------------")
            print("                 E-mails Menu\n")
            print("1- Check  Inbox .")
            print("2- Send E-mails .")
            print("3- Delete E-mails .")
            print("4- Back to Menu .")
            print("-----------------------------------------------")    
            while(1):
               pick=input("\nPlease enter your choise here : ")
               if(pick not in ["1","2","3","4"]):
                   print("\nYou put wrong Choise , please re-enter again .\n")
                   continue
               else:
                   break
            
            
            newEmpEmail=dict({})
            for i in employeesEmail :              
               if user in i :                   
                   newEmpEmail[i]=employeesEmail[i]
            if (pick =="1"):
                if isEmpty(newEmpEmail) :
                        print("\nYou don't have any emails .")
                else : 
                    print("\nThese are the E-mails  in your inbox :")
                    data=pd.DataFrame(newEmpEmail,index=["E-mails"])
                    newData=data.T
                    print("\n\n")
                    print(newData)
    
            if (pick =="2"):
                empEmailSend(user) 
                
                
    
            if (pick =="3"):
              if(not isEmpty(newEmpEmail)):
                print("\n\n")
                while(1):
                    employeeKyeList=list(newEmpEmail.keys())

                    print("\nThese are the E-mails in your inbox :")
                    data=pd.DataFrame(newEmpEmail,index=["E-mails"])
                    newData=data.T
                    print("\n\n")
                    print(newData )
                    print("\n")
                    for i in range(len(employeeKyeList)):
                        print(str(i+1) + "   " + employeeKyeList[i])
                    while(1):    
                        delPick=(input("\nPlease enter the E-mail number you want to delete : "))
                        l=[]
                        for i in range(1,len(employeeKyeList)+1):
                            l.append(str(i))
                        
                        if(delPick not in l ):
                            print("\nYour choise is wrong , please re-enter a right number .")
                            continue
                        else : 
                            break
                    ifDel=input("\nIf you are sure to delete this E-mail press 1 ,else press any key : ")
                    if ifDel =="1":
                        deletEmil(newEmpEmail,employeeKyeList[int(delPick)-1])
                        deletEmil(employeesEmail,employeeKyeList[int(delPick)-1])
                    conChoise=input("\nIf you want to continue deleting press * , else press any kye : ")
                    if conChoise == "*" and (not isEmpty(newEmpEmail)):
                        continue 
                    else :
                        break
                    if isEmpty(adminEmail): 
                        print("\nYou don't have any E-mails .")  
                        
                        break
              else:
                print("\nYou don't have any E-mails .")  
                continue
            if (pick =="4"):
                break
 
    
def employeeKey(emp,user):
    for i in emp:
      if emp[i][0]==user:
           return i
                
def otherEmp ():
  while(1):
    while(1):
        nameO=input("\nEnter the new  Employee's username : ")
        if nameO not in otherList :
            break
        else : 
            print("\nThe username is already taken before , please enter different one .")
            continue
    
    print("\nEnter the new Employee's Job description (PS:you can't dd any new employee as an admin .\n")

    while(1):
        jobO=input("\nJob description : ")
        jobO=jobO.lower()
        if jobO =="admin":
            print("\nYou can't add any employee as an admin  please re-enter a new job description for this employee .")
            continue
        
        else:
            break
    
    if(jobO in otherEmployees):
        print("\nYou have already an Employee(s) with same job name .\n")
        checkk=input(("\nIf you want to Exit press 1 , or press any key to continue to adding the employee : "))
        if(checkk=="1"):
            break
        emcount=0
        for i in otherEmployees :
            if jobO in i:
                emcount +=1 
        jobO=jobO+str(int(emcount)+1)    
    salaryO=0
    while(1):
        cO=0
        salaryO=(input("\nPlease enter the new Employee's Salary : "))
        for i in salaryO:
            if i.isdigit():
                cO +=1
        if cO==len(salaryO):
            salaryO=int(salaryO)
            break
        else:
            print("\nThe salary input is containing characters please enter numbers only .")
            continue
   
            
    otherEmployees[jobO]=[nameO,salaryO]
    otherList.append(nameO) 
    break

def addEmployee () :
   while(1): 
        while(1):
            name=input("\nEnter the new  Employee's username : ")
            if name not in userPassList :
                break
            else : 
                print("\nThe user name is already taken before , please enter different one .")
                continue
        
        print("\nEnter the new Employee's Job description (PS:you can't dd any new employee as an admin .\n")
    
        while(1):
            job=input("\nJob description : ")
            job=job.lower()
            if job =="admin":
                print("\nYou can't add any employee as an admin  please re-enter a new job description for this employee .")
                continue
            
            else:
                break
        if(job in employees):
            print("\nYou have already an Employee(s) with same job name .\n")
            checkk=input(("\nIf you want to Exit press 1 , or press any key to continue to adding the employee : "))
            if(checkk=="1"):
                break
            emcount=0
            for i in employees :
                if job in i:
                    emcount +=1 
            job=job+str(int(emcount)+1)        
        print("\nEnter the new Employee's passWord :\n\nPS:Password should be more than 8 chracters ,")
        print("and contains : Capital Letters , Small Letters , Numbers and Characters .")
        passWord=PassCheck()
        
        salary=0
        while(1):
            c=0
            salary=(input("\nPlease enter the new Employee's Salary : "))
            for i in salary:
                if i.isdigit():
                    c +=1
            if c==len(salary):
                salary=int(salary)
                break
            else:
                print("\nThe salary input is containing characters please enter numbers only .")
                continue
            
        
        while(1):    
            acc=["s","a"]
            acces=input("\nPlease enter the accessibility ,a for accountants ,s for sales : ")
            acces=acces.lower()
            if(acces not in acc ):
                print("\nThe accessibility you have entred is not exist .")
                print("\nIf you want to add "+ str(acces)+ " as a new accessibility , contact the programmer .")
                continue 
            else : 
                break
                

        employees[job]=[name,salary,acces,passWord]
        
        userPassList.append(name)
        break
        
def removeEmployee():
    print('\n')
    for i in range(len(userPassList[1:])) :
        print("Employee # " + str(i+1)+"  : " + userPassList[i+1] )

    while(1):
     name=input("\nEnter the Employee's username : ")
     if name ==userPassList[0]:
         print("\nYou can not delete the admin .")
         break
     if(name in userPassList ):
         
         
         for i in employees: 
             if (name == employees[i][0]):
                 ifDelEmp=input("\nIf you are sure to delete this Employee press 1 ,else press any key : ")
                 if(ifDelEmp=="1"):
                     userPassList.remove(str(employees[i][0]))
                     (employees).pop(i)
                
                 break
         break
     else : 
         print("\nThere is no employee with this username , please re-enter .")
         break



def changeEmpPass():
    print('\n')
    for i in range(len(userPassList)) :
        print("Employee # " + str(i+1)+"  : " + userPassList[i] )
        
    passName=input("\nPlease enter the Employee's username : ")
    
    
    if passName in userPassList:
        passNew=PassCheck()
        for i in employees:
            if employees[i][0]==passName :
                employees[i][-1]=passNew    
    else:
        print("\nThe username is incorrect . ")            
def avlCarSell():
        check=dict({})
        for i in  sellCars:
            if sellCars[i][-1]=="available" :
                check[i]=sellCars[i]
                
                        
        data=check
            
        avbSell=["Model","Engien","Color","Condition","Additions","Price","Status"]
        carTable=pd.DataFrame(data,index=(avbSell))
        
        print(carTable)
def bookCarSell():
    ind=["Car","Agent Name","Visa Code","Selling method" , "Car Price","portion","rest price","status"]
    data=bookedcar
    
    bookedTabel=pd.DataFrame(data,index=(ind))
    list2=list(bookedcar.keys())
                        
    if len(list2)==0:
        print("\nThere is no booked cars .")
        
    else:
        print(bookedTabel)

def avlCarRent():
    check2=dict({})
    for i in  rentCars:
        if rentCars[i][-1]=="available" :
            check2[i]=rentCars[i]
                        
    data=check2
                        
    avbSell=["Model","Engien","Color","Condition","Additions","Price","Status"]
    carTable=pd.DataFrame(data,index=(avbSell))
    if isEmpty(check2):
        print("\nThere is no available cars for renting .")
    else:
        print(carTable)
                        


def rentedCar():
    data=RENTEDcars
    ind=["Car","Agent Name","Visa Code","Selling method" , "rent Price/day","amount paid","duration(days)","status"]
    for i in data:
        if data[i][-1]=="rented":
            RENTEDcars[i]=data[i]
    bookedTabel=pd.DataFrame(RENTEDcars,index=(ind))
    list2=list(RENTEDcars.keys())
                        
    if len(list2)==0:
        print("\nThere is no rented cars .")
                            
                        
    else:
        print(bookedTabel)

    

def employeeList():
    emplist=["User name" , "Salary" ,"accessibility","Password"]
    newDict=dict({})
    data=employees
    for i in data:
        if i =="admin":
            continue 
        newDict[i]=data[i]
    
    if isEmpty(newDict) :
        print("\nThere is no employees to show .")
        
    else:
               
        employeesTabel=pd.DataFrame(newDict , index=(emplist))
        print(employeesTabel)
                            
    
    
def showBuyCars () :
    data=showRSoomBuy
    buyTable=pd.DataFrame(data,index=(avb2Sell))
    print(buyTable) 
 

    
def buyCar():
    global buycou
    global rencou
    global bankBalance 

    while(1):      
        print("\n\n-----------------------------------------------")
        print("                 Buying Menu\n")
        print("1- Show your bank account .")
        print("2- If you want to buy a car .")
        print("3- Back to Menu .")
        print("-----------------------------------------------")    
        while(1):
           pick=input("\nPlease enter your choise here : ")
           if(pick not in ["1","2","3"]):
               print("\nYou put wrong Choise , please re-enter again .\n")
               
               continue
           else:
               break
        
        if pick == "1" :
            print("\nYou have : " + str(bankBalance) + "$ in your bank account .\n")
            continue
        if pick =="2":
            
            print("\n\n\n")
            for i in range(len(carList)) :
                print (str(i+1)+"- " + str(carList[i]) )
                c = list(range(1,len(carList)+1))
            for i in range(len(c)) :
                    c[i] = str(c[i])
            while(1):
                carSellect=(input("\nPlease pick the car you want to buy : "))
                if(carSellect not in c ):
                    print("\nThe car number you've sellected is not right , please re-enter again .")
                    continue 
                else : 
                    break 
            carSellect=int(carSellect)    
            carPrice=showRSoomBuy[carList [carSellect-1 ]][-1]
            if(bankBalance<carPrice):
                print("\nThe car price is more than the bank balance . you can't buy it right now , charge your account .")
                break 
            print("\n\nIn which category you want to put the new car ?")
            print("1- Cars for Sale . \n2- Cars for rent .")
            while(1):
                category=(input("press here : "))
                if category not in ["1","2"]:
                    print("\nWrong choise , please enter again .")
                    continue 
                else : 
                    break 
            
            convertDict=dict({})
            KYE=carList[carSellect-1]
            convertDict[carList[carSellect-1]] = showRSoomBuy[carList[carSellect-1]]
            bankBalance = bankBalance - convertDict[KYE][-1]
            carList.pop(carSellect-1)
            if category=="1" :
                print("\nThe actual price for the car is : " + str(convertDict[KYE][-1]) + ".")
                print("\nIn which price do you want to sell this car in your ShowRoom ?")
                
                while(1):
                    newPrice=(input("\nPut the price here : "))
                    if newPrice.isdigit():
                        newPrice=int(newPrice)
                        break
                    else:
                        print("\nWrong number , please enter again .")
                        
                    
                convertDict[KYE][-1]=newPrice
                convertDict[KYE].append("available")
                ll=list(sellCars.keys())
                for i in ll:
                   if KYE == i:
                       buycou +=1
                if(buycou ==0 ):
                    newKYE = KYE
                else :
                    newKYE = KYE+"( "+str(buycou)+" )"
                sellCars[newKYE]=convertDict[KYE]
                showRSoomBuy.pop(KYE)
                
                
                
                
                
                
            if category =="2" : 
                print("\nIn which renting price per day  do you want to rent this car in your ShowRoom .")
                while(1):
                    newPrice=(input("\nPut the price here : "))
                    if newPrice.isdigit():
                        newPrice=int(newPrice)
                        break
                    else:
                        print("\nWrong number , please enter again .")
                 
                convertDict[KYE][-1]=newPrice
                convertDict[KYE].append("available")
                ll=list(rentCars.keys())
                for i in ll:
                   if KYE == i:
                       rencou +=1
                if(rencou ==0 ):
                    newKYE = KYE
                else :
                    newKYE = KYE+"( "+str(rencou)+" )"
                    
                rentCars[newKYE]=convertDict[KYE]
                showRSoomBuy.pop(KYE)


        if pick =="3":
            break


            
            
            
            
            
                               

def welcome ():
   while(1):
       print("-----------------------------------------------")
       print("                 Welcome to MW3 Cars ShowRoom  \n")

       print("1- Employees Login.\n2- Agents .\n3- Forget Pssword.\n4- Exit .\n")
       print("-----------------------------------------------")

       pick=input("\nPlease enter your choise here : ")
       if(pick not in ["1","2","3","4"]):
           print("\nYou put wrong Choise , please re-enter again .\n")
           
           continue
       else:
           return pick
     
def getEmployee ():
        
        c=0
        global empPass   
        incoun=0
        enterCount=0
        while(incoun<5):
            userName=input("\nPlease enter your Username : ")
            if(userName) not in userPassList :
                 empPass=0
                 print("\nThe user name you entred is not found .")
                 incoun +=1
                 continue
            else :
                 enterCount=1
                 break
        while(enterCount):
            
               if(empPass<5):
                   passWord=input("\nPlease enter your Password : ")
                   
                   if (userName==employees["admin"][0])and (passWord==employees["admin"][-1]) :
                       print("\nWelcome Mr : " + str(employees["admin"][0])+"\n")
                       print("\nYou are the Admin .\n")
                       c=1
                       break
                       
                   for i in employees:
                       if (userName==employees[i][0])and (passWord==employees[i][-1]):
                           print("\nWelcome Mr :"+str(employees[i][0])+"\n")
                           c=2
                           break
                   if(c==2):
                       break
                       
                   if(c==0) :
                        print("\nYou entered a wrong Password or Username , pleaser re-enter again .\n")
                        empPass +=1
                        print("\nYou have just "+ str(5-empPass) + " attempts before temporary account blocking .")
                        continue 
               else : 
                   print("\nYour account has been temporarly blocked , please pick 4 from main menu to deal with this situation .")
                   if(userName) not in userPassList :
                       empPass=0

                       keyemp=employeeKey(employees,userName)
                       access=employees[keyemp][-2]
                       return c,userName,access
                   else :
                        newPassNum=np.random.randint(1000000,100000000,size=1)
                        newPassPh=np.random.randint(65,90,size=3)
                        nn=[]
                        for i in newPassPh:
                            nn.append(chr(i))
                        x=str(newPassNum[0])  
                        passWOOORD= "".join(nn)+str(x)
                        USERN=0
                        for i in employees :
                            if (employees[i][0]==userName):
                                USERN=i
                                break

                        employees[USERN][-1]=passWOOORD
                       
                        empPass=0

                        keyemp=employeeKey(employees,userName)
                        access=employees[keyemp][-2]
                        return c,userName,access
                   
                        
        
        empPass=0
        keyemp=employeeKey(employees,userName)
        access=employees[keyemp][-2]
        return c,userName,access
        

def bankManeg():
    global bankBalance
    while(1):
        print("-----------------------------------------------")
        print("                 Bank Menu\n")
        print("1- If you want to check your bank account  .")
        print("2- If you want to add any amount of money  .")
        print("3- If you want to withdraw any amount of money  .")
        print("4- Back to main menu  .")
        print("-----------------------------------------------")
        while(1):
            bkch=(input("\nEnter your choise here : "))
            if(bkch not in ["1","2","3","4"]):
                print("\nYou made wrong choise , please re-enter again.\n")
                continue
            else:
                break
        if(bkch=="1"):
                print("\nYou have : " + str(bankBalance) + "$ in your bank account .\n")
                
        if(bkch=="2"):
            while(1):
                    add=(input("\nPlease enter the amount you want to add  : "))
                    if add.isdigit():
                        break
                    else:
                        print("\nWrong input please re-enter .")
                        continue
            bankBalance += int(add)
            print("\nYou have : " + str(bankBalance) + "$ in your bank account .\n")
            continue
        if(bkch=="3"): 
                    while(1):
                        withdraw=(input("\nPlease enter the amount you want to withdrw  : "))
                        if withdraw.isdigit():
                            break
                        else:
                            print("\nWrong input please re-enter .")
                            continue
                    if(int(withdraw)>bankBalance)   :
                        print("\nYou do not have enough money to withdraw ")
                        continue
                    else :
                        bankBalance -= int(withdraw)
                        
                        print("\nYou have : " + str(bankBalance) + "$ in your bank account .\n")
                        continue
        if(bkch=="4"): 
                    break
    

def agentmenu():
    global bankBalance
    agentname=input("\nPlease enter your name : ")
    print("\n\n")
    while(1):
        print("-----------------------------------------------")
        print("                 Agent Menu\n")
        print("1- Cars to buy  .")
        print("2- Cars to rent  .")
        print("3- If you want to sell a car  .")
        print("4- Exit  .")
        print("-----------------------------------------------")
        while(1):
            bkch=(input("\nEnter your choise here : "))
            if(bkch not in ["1","2","3","4"]):
                print("\nYou made wrond choise , please re-enter again.\n")
                continue
            else:
                break
    
        if(bkch=="1"):
            global bankBalance
            while(1):
                print("-----------------------------------------------")
                print("                 Cars to buy Menu\n")
                print("1- Show all avaliable cars .")
                print("2- Pick car to buy  and choose payment method .")
                print("3- Exit .")
                print("-----------------------------------------------")
                while(1):
                    agch=(input("\nEnter your choise here : "))
                    if(agch not in ["1","2","3"]):
                        print("\nYou made wrong choise , please re-enter again.\n")
                        continue
                    else:
                        break
                
                checksell=dict({})
                for i in  sellCars:
                    if sellCars[i][-1]=="available" :
                        checksell[i]=sellCars[i]                
                if(isEmpty(checksell)):
                    print("\nThere is no cars to buy at this moment .")
                    break
                if agch=="1":
                    avlCarSell()
                    continue
                if agch=="2":
                    
                    listemp=[]
                    for i in checksell:
                       listemp.append(i)
                    print("\nWhich car you want to buy ?")
                    for i in range(1,len(listemp)+1):
                        print(str(i)+"-"+str(listemp[i-1]))
                        
                    while(1):    
                        pikcar=(input("\nPlease enter the car number : "))
                        l=[]
                        for i in range(1,len(listemp)+1):
                            l.append(str(i))
                            
                        if(pikcar not in l ):
                                print("\nYour choise is wrong , please re-enter a right number .")
                                continue
                        else : 
                                break
                    print("\nThis is the car you have picked .")
                    
                    print(listemp[int(pikcar)-1])
                    print("\nThe Properties for this car is :\n",checksell[listemp[int(pikcar)-1]])
                    print("\nThe car price is : ",checksell[listemp[int(pikcar)-1]][-2])
                   
                    confirm=input("\nIf you want to continue to purchasing this car press (1) ,else press any key : ")
                    if confirm=="1":
                        while(1):
                            print("-----------------------------------------------")
                            print("                 purchasing Menu\n")
                            print("1- Online purchasing .")
                            print("2- Booking .")
                            print("3- Pay at the fair .")
                            print("4- Back to menu .")
                            print("-----------------------------------------------")
                            while(1):
                                agb=(input("\nEnter your choise here : "))
                                if(agb not in ["1","2","3","4"]):
                                    print("\nYou made wrong choise , please re-enter again.\n")
                                    continue
                                else:
                                    break
                                      
                            if agb =="1":
                                print("\nYou will be asked to enter you VISA information ,and all of the information will be secured .")
                                print("\n")
                                visacode=input("\nPlease enter yor Visa code : ")
                                print("\n")
                                expdate=input("\nPlease enter the expiration date ex(mm-year) : ")
                                print("\nThe Purchasing proccess completed successfully .")
                                selledCarsinfo[listemp[int(pikcar)-1]]=[agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2]]
                                sellCars[listemp[int(pikcar)-1]][-1]="sold"
                                l=[listemp[int(pikcar)-1],agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2],checksell[listemp[int(pikcar)-1]][-2],"-","sold"]
                                accountantBuyMail.append(l)
                                adminBuyMail.append(l)
                                bankBalance +=  checksell[listemp[int(pikcar)-1]][-2]
                                print("\nPlease visit us in the showroom in irbid-bagdad.st-MW3 CO")
                                print("\nto compliete regitration and get your new car .")
                                break
                            
                            
                            
                            if agb == "2":
                                print("\nYou have choosed this car : "+str(listemp[int(pikcar)-1]))
                                print("\nThe car price is : ",checksell[listemp[int(pikcar)-1]][-2])
                                print("\nYou have to pay a portion of the car price to book this car at least 100$ .")
                                
                                
                                while(1):
                                    c=0
                                    portion=input("\nPlease enter the amount of money you want to pay : ")
                                    for i in portion:
                                        if i.isdigit():
                                            c +=1
                                    if c==len(portion) and checksell[listemp[int(pikcar)-1]][-2]>=int(portion)>=100:
                                        portion=int(portion)
                                        break
                                    else:
                                        print("\nThe portion input is containing characters or less than 100$, please re-enter correctly .")
                                
                                print("\nYou will be asked to enter you VISA information ,and all of the information will be secured .")
                                print("\n")
                                visacode=input("\nPlease enter yor Visa code : ")
                                print("\n")
                                expdate=input("\nPlease enter the expiration date ex(mm-year) : ")
                                print("\nThe booking proccess completed successfully.") 
                                rest=checksell[listemp[int(pikcar)-1]][-2]-portion
                                bookdata=[listemp[int(pikcar)-1],agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2],portion,rest,"booked"]                               
                                bookedcar[listemp[int(pikcar)-1]]=bookdata
                                sellCars[listemp[int(pikcar)-1]][-1]="booked"
                                bankBalance +=portion
                                l=[listemp[int(pikcar)-1],agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2],portion,rest,"booked"]
                                accountantBuyMail.append(l)
                                adminBuyMail.append(l)
                                
                                print("\nPlease visit us in the showroom in irbid-bagdad.st-MW3 CO")
                                print("\nto compliete the payment ,regitration and get your new car .")
                                break
                            if agb == "3":
                                print("\nPlease visit us in the showroom in irbid-bagdad.st-MW3 CO.")
                                print("\nThe car you picked will not be booked  ,you should visit us to complete the proccess .")
                            if agb=="4":
                                break
                    else:
                        break
                    
                    
                    
                    
                    
                            
                    
                if agch=="3":
                    break
            
            
        if(bkch=="2"):
            while(1):
                print("-----------------------------------------------")
                print("                 Cars to rent Menu\n")
                print("1- Show all avaliable rent cars .")
                print("2- Pick car to buy  and choose payment method .")
                print("3- Exit .")
                print("-----------------------------------------------")
                while(1):
                    agch=(input("\nEnter your choise here : "))
                    if(agch not in ["1","2","3"]):
                        print("\nYou made wrond choise , please re-enter again.\n")
                        continue
                    else:
                        break
                
                checksell=dict({})
                for i in  rentCars:
                    if rentCars[i][-1]=="available" :
                        checksell[i]=rentCars[i]                
                if(isEmpty(checksell)):
                    print("\nThere is no cars to rent at this moment .")
                    break
                if agch=="1":
                    avlCarRent()
                    continue
                if agch=="2":
                    
                    listemp=[]
                    for i in checksell:
                       listemp.append(i)
                    print("\nWhich car you want to rent ?")
                    for i in range(1,len(listemp)+1):
                        print(str(i)+"-"+str(listemp[i-1]))
                        
                    while(1):    
                        pikcar=(input("\nPlease enter the car number : "))
                        l=[]
                        for i in range(1,len(listemp)+1):
                            l.append(str(i))
                            
                        if(pikcar not in l ):
                                print("\nYour choise is wrong , please re-enter a right number .")
                                continue
                        else : 
                                break
                    print("\nThis is the car you have picked .")
                    
                    print(listemp[int(pikcar)-1])
                    print("\nand the Properties for this car is :",checksell[listemp[int(pikcar)-1]])
                    print("\nThe car renting price per day is : ",checksell[listemp[int(pikcar)-1]][-2])
                    while(1):
                        c=0
                        days=(input("\nPlease enter how many days do you want rent this car : "))
                        for i in days:
                            if i.isdigit():
                                c +=1
                        if c==len(days) and int(days)>0:
                            days=int(days)
                            break
                        else:
                            print("\nThe days input is containing characters please enter numbers only . ")
                            
                    rentmoney=days*checksell[listemp[int(pikcar)-1]][-2]
                    print("\nThe cost of rinting car during the duration you picked is : ",rentmoney)
                    confirm=input("\nIf you want to continue to rent this car press (1) ,else press any key .")
                    if confirm=="1":
                        while(1):
                            print("-----------------------------------------------")
                            print("                 purchasing Menu\n")
                            print("1- Online purchasing .")
                            print("2- Pay at the fair .")
                            print("3- Back to menu .")
                            print("-----------------------------------------------")
                            while(1):
                                agb=(input("\nEnter your choise here : "))
                                if(agb not in ["1","2","3"]):
                                    print("\nYou made wrong choise , please re-enter again.\n")
                                    continue
                                else:
                                    break
                                      
                            if agb =="1":
                                

                                
                                print("\nYou will be asked to enter you VISA information ,and all of the information will be secured .")
                                print("\n")
                                visacode=input("\nPlease enter yor Visa code : ")
                                print("\n")
                                expdate=input("\nPlease enter the expiration date ex(mm-year) : ")
                                print("\nThe rinting proccess completed successfully .")
                                
                                rentCars[listemp[int(pikcar)-1]][-1]="rented"
                                RENTEDcars[listemp[int(pikcar)-1]]=[listemp[int(pikcar)-1],agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2],rentmoney,days,"rented"]
                                l=[listemp[int(pikcar)-1],agentname,visacode,"Online",checksell[listemp[int(pikcar)-1]][-2],rentmoney,days,"rented"]
                                accountantrentMail.append(l)
                                adminrentMail.append(l)
                                

                                bankBalance +=  rentmoney
                                print("\nPlease visit us in the showroom in irbid-bagdad.st-MW3 CO")
                                print("\nto compliete regitration and get the car .")
                                break
                            
                            
                            
                            
                            if agb == "2":
                                print("\nPlease visit us in the showroom in irbid-bagdad.st-MW3 CO.")
                                print("\nThe car you picked will not be booked  ,you should visit us to complete the proccess .")
                            if agb=="3":
                                break
                    else:
                        break
                    
                    
                    
                    
                    
                            
                    
                if agch=="3":
                    break            
                        
        if bkch=="3":
            print("\nThis option is not aveliable now,its will be added soon .")
            
        if(bkch=="4"):
            break

def editShow():
    global bankBalance
    while(1):
        print("-----------------------------------------------")
        print("         Showroom Sales Operations Menu      \n")
        print("1- If you want to add sold car  .")
        print("2- If you want to add booked car .")
        print("3- If you want to add rented car  .")
        print("4- Back to main menu  .")
        print("-----------------------------------------------")
        while(1):
            bkch=(input("\nEnter your choise here : "))
            if(bkch not in ["1","2","3","4"]):
                print("\nYou made wrong choise , please re-enter again.\n")
                continue
            else:
                break
        if(bkch=="1"): 
            checksell=dict({})
            for i in  sellCars:
                if sellCars[i][-1]=="available" :
                    checksell[i]=sellCars[i]                
            if(isEmpty(checksell)):
                print("\nThere is no cars to buy at this moment .")
                continue
           
            
                
            listemp=[]
            for i in checksell:
               listemp.append(i)
            print("\nWhich car you want to buy ? ")
            for i in range(1,len(listemp)+1):
                print(str(i)+"-"+str(listemp[i-1]))
                
            while(1):    
                pikcar=(input("\nPlease enter the car number : "))
                l=[]
                for i in range(1,len(listemp)+1):
                    l.append(str(i))
                    
                if(pikcar not in l ):
                        print("\nYour choise is wrong , please re-enter a right number .")
                        continue
                else : 
                        break
            print("\nThis is the car you have picked .")
            
            print(listemp[int(pikcar)-1])
            print("\nand the Properties for this car is :",checksell[listemp[int(pikcar)-1]])
            abrove=input("\nIf are you sure that this is the right car press (1),else press any key .")
            if abrove=="1":
                agentname=input("\nPlease enter the agent name : ")
                visacode=input("\nPlease enter the agent visacode  : ")
                sellCars[listemp[int(pikcar)-1]][-1]="sold"
                selledCarsinfo[listemp[int(pikcar)-1]]=[agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2]]
                l=[listemp[int(pikcar)-1],agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2],checksell[listemp[int(pikcar)-1]][-2],"-","sold"]
                accountantBuyMail.append(l)
                adminBuyMail.append(l)
                bankBalance +=  checksell[listemp[int(pikcar)-1]][-2]
                print("\nThe money was automatically added to bank account .")
            else:
                continue
        if(bkch=="2"):
            checksell=dict({})
            for i in  sellCars:
                if sellCars[i][-1]=="available" :
                    checksell[i]=sellCars[i]                
            if(isEmpty(checksell)):
                print("\nThere is no cars to buy at this moment .")
                continue
           
            
                
            listemp=[]
            for i in checksell:
               listemp.append(i)
            print("\nWhich car you want to buy ?")
            for i in range(1,len(listemp)+1):
                print(str(i)+"-"+str(listemp[i-1]))
                
            while(1):    
                pikcar=(input("\nPlease enter the car number : "))
                l=[]
                for i in range(1,len(listemp)+1):
                    l.append(str(i))
                    
                if(pikcar not in l ):
                        print("\nYour choise is wrong , please re-enter a right number .")
                        continue
                else : 
                        break
            print("\nThis is the car you have picked :")
            
            print(listemp[int(pikcar)-1])
            print("\nand the Properties for this car is :",checksell[listemp[int(pikcar)-1]])
            abrove=input("\nIf are you sure that this is the right car press (1),else press any key : ")
            if abrove=="1":
                sellCars[listemp[int(pikcar)-1]][-1]="booked"
                agentname=input("\nPlease enter the agent name : ")
                
                visacode=input("\nPlease enter the agent visacode name : ")
                while(1):
                    co=0
                    portion=input("\nPlease enter the portion was paid form the agent and it's more than 100$ .")
                    for i in range(len(portion)):
                        if portion[i].isdigit():
                            co +=1
                    if co==len(portion) and int(portion)>=100 and int(portion)<=checksell[listemp[int(pikcar)-1]][-2]  :
                        break
                    else:
                         print("\nWrong input , please re-enter a right number .")
                rest=checksell[listemp[int(pikcar)-1]][-2]-int(portion)
                ind=["Car","Agent Name","Visa Code","Selling method" , "Car Price","rest price","portion","status"]
                bookedcar[listemp[int(pikcar)-1]]=[listemp[int(pikcar)-1],agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2],int(portion),rest,"booked"]
                l=[listemp[int(pikcar)-1],agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2],int(portion),rest,"booked"]
                accountantBuyMail.append(l)
                adminBuyMail.append(l)
                bankBalance +=  int(portion)
                print("\nThe money was automatically added to bank account .")
            else:
                continue
        if(bkch=="3"):
            checksell=dict({})
            for i in  rentCars:
                if rentCars[i][-1]=="available" :
                    checksell[i]=rentCars[i]                
            if(isEmpty(checksell)):
                print("\nThere is no cars to buy at this moment .")
                continue
           
            
                
            listemp=[]
            for i in checksell:
               listemp.append(i)
            print("\nWhich car you want to buy ?")
            for i in range(1,len(listemp)+1):
                print(str(i)+"-"+str(listemp[i-1]))
                
            while(1):    
                pikcar=(input("\nPlease enter the car number : "))
                l=[]
                for i in range(1,len(listemp)+1):
                    l.append(str(i))
                    
                if(pikcar not in l ):
                        print("\nYour choise is wrong , please re-enter a right number .")
                        continue
                else : 
                        break
            print("\nThis is the car you have picked : ")
            
            print(listemp[int(pikcar)-1])
            print("\nand the Properties for this car is :",checksell[listemp[int(pikcar)-1]])
            abrove=input("\nIf are you sure that this is the right car press (1),else press any key : ")
            if abrove=="1":
                
                agentname=input("\nPlease enter the agent name : ")
                
                visacode=input("\nPlease enter the agent visacode  : ")
                while(1):
                    co=0
                    days=input("\nPlease enter the renting days ( Positive number of days ) : ")
                    for i in range(len(days)):
                        if days[i].isdigit():
                            co +=1
                    if co==len(days) and int(days) >0 :
                        break
                    else:
                         print("\nWrong input , please re-enter a right number .")
                         
                days=int(days)         
                rentmoney=days*checksell[listemp[int(pikcar)-1]][-2]       
                
                ind=["Car","Agent Name","Visa Code","Selling method" , "rent Price/day","amount paid","duration(days)","status"]
                RENTEDcars[listemp[int(pikcar)-1]]=[listemp[int(pikcar)-1],agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2],rentmoney,days,"rented"]
                
                
                l=[listemp[int(pikcar)-1],agentname,visacode,"in showroom",checksell[listemp[int(pikcar)-1]][-2],rentmoney,days,"rented"]
                accountantrentMail.append(l)
                adminrentMail.append(l)
                
                
               
                bankBalance +=  int(rentmoney)
                print("\nThe money was automatically added to bank account .")                
                
        
                
                rentCars[listemp[int(pikcar)-1]][-1]="rented"
                
            else:
                continue            
            
            
        if(bkch=="4"):
            break








