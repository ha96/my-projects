import oopLib as ol
import pandas as pd 
global abc
abc=0
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.colheader_justify', 'center')

while (1):
   pick=ol.welcome()
   
   if pick == "4" :
       break
   if pick == "3" :
       print("\nIf you are the admin :\nPlease contact the program Devolopers : ")
       print("\n1- suhaib.abualhijaa@gmail.com .")
       print("\n2- hazemmaabreh@gmail.com .")
       print("\nIf you are an Employee :\nPlease contact the head manager to change your password .\n")
       continue
   if pick == "1" :
     c,user1,access1=ol.getEmployee() 
     if(access1  =='ad'):
       while(1):
            if (abc==10):
                abc=0
                break

            if(c==0):
                break
            if(c==2):
                print("\nYou are not allowed to enter the Admin work space brcause you are an Employee please choose 2 from main menu .\n")
                break
            if(c==1):
                while(1):
                    print("-----------------------------------------------")
                    print("                 Main Menu")
                    print("1- Check Bank Account.\n2- Check available cars for sale.")
                    print("3- Check booked cars for sale.\n4- Available renting cars.")
                    print("5- Rented cars.\n6- Check cars to buy .")
                    print("7- Check sold Cars . \n8- Check all employees .")
                    print("9- Add new employee. \n10- Remove employee.")
                    print("11- Change Employee's Paswoord.\n12- Email.")
                    print("13- Online Sold Cars Notifications .")
                    print("14- Online rinted Cars Notifications .") 
                    print("15- Change cars status .")
                    print("16- LogOut")
                    print("-----------------------------------------------")
    
                    while (1) :
                        ch=(input("\nPlease enter your choise : "))
                        if(ch not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]):
                            print("\nYou made wrond choise , please re-enter again.\n")
                            continue
                        else:
                            break
                    if(ch=="1"):
                        ol.bankManeg()
                        continue
                    
                    if(ch=="2"):
                        sellcount=0
                        for i in ol.sellCars:
                            if ol.sellCars[i][-1]=="available":
                                sellcount +=1
                        if sellcount==0:
                            print ("\nThere is no available cars right now .")
                            continue
                        else:
                            
                            ol.avlCarSell()
                            continue
                                    
                    if(ch=="3"):        
                        ol.bookCarSell()
                        continue
                    if(ch=="4"):
                        ol.avlCarRent()
                        continue
                        
                        
                    if(ch=="5"):
                        ol.rentedCar()
                        continue
                    
                    if(ch=="6"):
                        ol.showBuyCars ()
                        ol.buyCar()
                        ol.buycou=0
                        ol.rencou=0
                        continue
                        
                    if(ch=="7"):
                        print("\n")
                        ind=["Agent Name","Visa Code","Selling method" , "Car Price"]

                        data=pd.DataFrame(ol.selledCarsinfo,index=(ind))
                        if (ol.isEmpty(data)) :
                            print("\nThere is no sold cars .")
                            continue
                        else :
                            print(data)
                            continue     
                    if(ch=="8"):
                        while(1):      
                            print("\n\n-----------------------------------------------")
                            print("                 Employees Menu\n")
                            print("1- Employees with System Access .")
                            print("2- Employees without System Access .")
                            print("3- Back to Menu .")
                            print("-----------------------------------------------")    
                            while(1):
                               pickEm=input("\nPlease enter your choise here : ")
                               if(pickEm not in ["1","2","3"]):
                                   print("\nYou put wrong Choise , please re-enter again .\n")
                                   
                                   continue
                               else:
                                   break
                            if(pickEm == "1"):
                                ol.employeeList()
                                continue
                            if(pickEm =="2"):
                                emplist=["Employee Name" , "Salary" ]
                                if (ol.isEmpty(ol.otherEmployees)):
                                    print("\nThere is no employees to show .")
                                else:
                                    employeesTabel=pd.DataFrame( ol.otherEmployees , index=(emplist))
                                    print(employeesTabel)
                                    continue
                            if (pickEm)=="3":
                                break
                                
                    if(ch=="9"):
                        while(1):      
                            print("\n\n-----------------------------------------------")
                            print("                Add Employees Menu\n")
                            print("1- Add Employees with System Access .")
                            print("2- Add Employees without System Access .")
                            print("3- Back to Menu .")
                            print("-----------------------------------------------")    
                            while(1):
                               pickEma=input("\nPlease enter your choise here : ")
                               if(pickEma not in ["1","2","3"]):
                                   print("\nYou put wrong Choise , please re-enter again .\n")
                                   continue
                               else:
                                   break
                            if(pickEma == "1"):
                                ol.addEmployee ()
                                continue
                            if(pickEma =="2"):
                                ol.otherEmp ()
                                continue
                            if (pickEma)=="3":
                                break
                        
                        
                        
                    if(ch=="10"):
                        while(1):      
                            print("\n\n-----------------------------------------------")
                            print("                Remove Employees Menu\n")
                            print("1- Remove Employees with System Access .")
                            print("2- Remove Employees without System Access .")
                            print("3- Back to Menu .")
                            print("-----------------------------------------------")    
                            while(1):
                               pickEmd=input("\nPlease enter your choise here : ")
                               if(pickEmd not in ["1","2","3"]):
                                   print("\nYou put wrong Choise , please re-enter again .\n")
                                   continue
                               else:
                                   break
                            if(pickEmd == "1"):
                                ol.removeEmployee()
                                continue
                            if(pickEmd =="2"):
                              print('\n')
                              for i in range(len(ol.otherList)) :
                                    print("Employee's Name  : " + ol.otherList[i] )
                              while(1):
                                name=input("\nEnter the Employee's Name : ")
                                if(name in ol.otherList):
                                    for i in ol.otherEmployees: 
                                        if (name == ol.otherEmployees[i][0]):
                                            ifDelEmp=input("\nIf you are sure to delete this Employee press 1 ,else press any key : ")
                                            if(ifDelEmp=="1"):

                                                ol.otherList.remove(str(ol.otherEmployees[i][0]))
                                                (ol.otherEmployees).pop(i)
                                                break 
                                            
                                    break
                                
                                else : 
                                    print("\nThere is no employee with this username , please re-enter .")
                                    break  
                                    
                            if(pickEmd =="3"):
                                break
                            

                        
                    if(ch=="11"):
                        ol.changeEmpPass()
                        continue
                                
                    if (ch=="12"):
                        ol.adminEmails(user1)
                        continue
                    if(ch=="13"):
                        if(len(ol.adminBuyMail)!=0):
                        
                            ind=["Car","Agent Name","Visa Code","Selling method" ,"car price", "portion paid","rest price","status"]
     
                            data=pd.DataFrame(ol.adminBuyMail,columns=(ind))
                            print(data)
     
                            
                            print("\nNew car was sold as mentioned before , and the money was automatically added to bank account .")
                            delNot=input("\n\nIf you want to clear all notifications press 1 , else press any key .")
                            if(delNot =="1" ):
                                ol.adminBuyMail.clear()                                                                
                            continue
                        else :
                            print("\nThe notification inbox is empty .")
                        continue
                    
                    if(ch=="14"):
                        if(len(ol.adminrentMail)!=0):
                            ind=["Car","Agent Name","Visa Code","Selling method" ,"rent price/day", "amount paid","duration","status"]
     
                            data=pd.DataFrame(ol.adminrentMail,columns=(ind))
                            print(data)
     
                            
                            print("\nNew car was rented as mentioned before , and the money was automatically added to bank account .")
                            delNot=input("\n\nIf you want to clear all notifications prees 1 , else press any key .")
                            if(delNot =="1" ):
                                ol.adminrentMail.clear()
                            continue
                        else :
                            print("\nThe notification inbox is empty .")
                            
 
                        continue
                     
                    if(ch=="15"): 
                        while(1):      
                            print("\n\n-----------------------------------------------")
                            print("                 Chaning Cars Status Menu\n")
                            print("1- Change booked for sell cars status to available .")
                            print("2- Change rented cars status to available .")
                            print("3- Back to Menu .")
                            print("-----------------------------------------------")    
                            while(1):
                               pick=input("\nPlease enter your choise here : ")
                               if(pick not in ["1","2","3"]):
                                   print("\nYou put wrong Choise , please re-enter again .\n")
                                   
                                   continue
                               else:
                                   break
                            
                                                               
                            if pick=="1": 
                                if(ol.isEmpty(ol.bookedcar)):
                                    print("\nThere is no booked cars .")
                                else :  
                                    li=list(ol.bookedcar.keys())
                                    for i in range(len(li)):
                                        print(str(i+1)+"-"+" "+str(li[i]))
                                    
                                    while(1):    
                                        pikcar=(input("\nPlease enter the car number  :"))
                                        l=[]
                                        for i in range(1,len(li)+1):
                                            l.append(str(i))
                                            
                                        if(pikcar not in l ):
                                                print("\nYour choise is wrong , please re-enter a right number .")
                                                continue
                                        else : 
                                                break
                                            
                                    ol.sellCars[li[int(pikcar)-1]][-1]="available" 
                                    del ol.bookedcar[li[int(pikcar)-1]]

                            if pick=="2":
                                if(ol.isEmpty(ol.RENTEDcars)):
                                    print("\nThere is no booked cars .")
                                    
                                else :
                                    li=list(ol.RENTEDcars.keys())
                                    for i in range(len(li)):
                                        print(str(i+1)+"-"+" "+str(li[i]))
                                    
                                    while(1):    
                                        pikcar=(input("\nPlease enter the car number  :"))
                                        l=[]
                                        for i in range(1,len(li)+1):
                                            l.append(str(i))
                                            
                                        if(pikcar not in l ):
                                                print("\nYour choise is wrong , please re-enter a right number .")
                                                continue
                                        else : 
                                                break
                                            
                                    ol.rentCars[li[int(pikcar)-1]][-1]="available" 
                                    del ol.RENTEDcars[li[int(pikcar)-1]]
                            
                            if pick=="3":
                                pick="0"
                                break
                      
                        
                    if(ch=="16"):
                        abc=10

                        break
                    
                        
              
     if(access1  =='a' or access1  =='s'):
         global ccc
         global kkk
         global a

         if(access1  =='a'):
             exit2=1
             while(1):
                if(exit2==0):
                    break
                if(c==0):
                    break
                while(1):
                    if c==1:
                        print("\nYou are not allowed to enter employee work space brcause you are an admin please choose 1 from main menu .")
                        break
                    if c==2:
                        
                        print("-----------------------------------------------")
                        print("                 Employee Menu\n")
                        print("1- Check available cars for sale.")
                        print("2- Check booked cars for sale.")
                        print("3- Available renting cars.")
                        print("4- Rented cars.")
                        print("5- Bank Account management .")
                        print("6- Email.")  
                        print("7- Online Sold Cars Notifications  .")
                        print("8- Online rinted Cars Notifications  .") 
                        print("9- LogOut .")
                        print("-----------------------------------------------")
                        while(1):
                            bkch=(input("\nEnter your choise here : "))
                            if(bkch not in ["1","2","3","4","5","6","7","8","9"]):
                                print("\nWrong choice . ")
                                continue
                            else:
                                
                                break
                        if bkch=="1":
                             sellcount=0
                             for i in ol.sellCars:
                                 if ol.sellCars[i][-1]=="available":
                                     sellcount +=1
                             if sellcount==0:
                                 print ("\nThere is no available cars right now.")
                                 continue
                             else:
                                 
                                 ol.avlCarSell()
                                 continue
                        if bkch=="2":
                            ol.bookCarSell()
                            continue
                        if bkch=="3":
                            ol.avlCarRent()
                            continue
                        if bkch=="4":
                            ol.rentedCar()
                            continue
                        if bkch=="5":
                            userKey=ol.employeeKey(ol.employees,user1)
                            if "a"==ol.employees[userKey][-2]:
                                ol.bankManeg()
                                continue
                            else:
                                print("\nYou are NOT authorised to use this feature.")
                                continue
                        if bkch=="6":
                            ol.employeesEmailCheck(user1)
                            continue
                            
                        if bkch=="7"  :
                            userKey=ol.employeeKey(ol.employees,user1)
                            if "a"==ol.employees[userKey][-2]:
                                if(len(ol.accountantBuyMail)!=0):
                                
                                    ind=["Car","Agent Name","Visa Code","Selling method" ,"car price", "portion paid","rest price","status"]
             
                                    data=pd.DataFrame(ol.accountantBuyMail,columns=(ind))
                                    print(data)
             
                                    
                                    print("\nNew car was sold as mentioned before , and the money was automatically added to bank account.")
                                    delNot=input("\n\nIf you want to clear all notifications prees 1 , else press any key .")
                                    if(delNot =="1" ):
                                        ol.accountantBuyMail.clear()
                                        
                                        
                                    continue
                                else :
                                    print("\nThe notification inbox is empty .")
                                    
                            else:
                                print("\nYou are NOT authorised to use this feature. ")
                                continue
                            
                                                        
                        if bkch=="8" : 
                            userKey=ol.employeeKey(ol.employees,user1)
                            if "a"==ol.employees[userKey][-2]:
                                if(len(ol.accountantrentMail)!=0):
                                    ind=["Car","Agent Name","Visa Code","Selling method" ,"rent price/day", "amount paid","duration","status"]
             
                                    data=pd.DataFrame(ol.accountantrentMail,columns=(ind))
                                    print(data)
             
                                    
                                    print("\nNw car was rented as mentioned before , and the money was automatically added to bank account .")
                                    delNot=input("\n\nIf you want to clear all notifications prees 1 , else press any key .")
                                    if(delNot =="1" ):
                                        ol.accountantrentMail.clear()
                                    continue
                                else :
                                    print("\nThe notification inbox is empty .")
                                    
                            else:
                                print("\nYou are NOT authorised to use this feature. ")
                                continue
                                                    
                      
                         
                        if bkch=="9":
                            ol.c1=0
                            ol.k1=0
                            ol.a=0
                            exit2=0
                            break
                
                     
                 
         if(access1  =='s'):
            exitt=1
            
            while(1):
                 if(exitt==0):
                    break
                 if(c==0):
                     break
                 while(1):
                     if c==1:
                         print("\nYou are not allowed to enter employee work space brcause you are an admin please choose 1 from main menu .")
                         break
                     if c==2:
                         
                         print("-----------------------------------------------")
                         print("                 Employee Menu\n")
                         print("1- Check available cars for sale.")
                         print("2- Check booked cars for sale.")
                         print("3- Available renting cars.")
                         print("4- Rented cars.")
                         print("5- Email.")  
                         print("6- Showroom sales operations .") 
                         print("7- LogOut .")
                         print("-----------------------------------------------")
                         while(1):
                             bkch=(input("\nEnter your choise here : "))
                             if(bkch not in ["1","2","3","4","5","6","7"]):
                                 print("\nWrong choice . ")
                                 continue
                             else:
                                 
                                 break
                         if bkch=="1":
                              sellcount=0
                              for i in ol.sellCars:
                                  if ol.sellCars[i][-1]=="available":
                                      sellcount +=1
                              if sellcount==0:
                                  print ("\nThere is no available cars right now.")
                                  continue
                              else:
                                  
                                  ol.avlCarSell()
                                  continue
                         if bkch=="2":
                             ol.bookCarSell()
                             continue
                         if bkch=="3":
                             ol.avlCarRent()
                             continue
                         if bkch=="4":
                             ol.rentedCar()
                             continue
                         if bkch=="5":
                             ol.employeesEmailCheck(user1)
                             continue
                             
                         
                                                     
                         if bkch=="6":
                            for i in  ol.employees:
                                if ol.employees[i][0]==user1:
                                    keyuser=i
                            if  ol.employees[keyuser][-2]=="s":
                                
                                ol.editShow()
                                continue
                            else:
                                print("\nYou are NOT authorised to use this feature. ")
                                continue
                                
                          
                         if bkch=="7":
                             ol.c1=0
                             ol.k1=0
                             ol.a=0
                             exitt=0
                             break

           
  
             
   if pick=="2":
       ol.agentmenu()
       
                   
                   
                   
           
               
       