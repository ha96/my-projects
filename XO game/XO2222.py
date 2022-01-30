# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:53:07 2021

@author: hp
"""
import pandas as pd
from numpy import random 
class plaeyer:
    def __init__(self,name1=0,name2=0,symbol1=0,symbol2=0):
        self.name1=name1
        self.name2=name2
        self.symbol1=symbol1
        self.symbol2=symbol2
        
    def getInfo(self):
        print("Welcome to X and O Game")
        l=["X","O","x","o"]
        self.name1=(input("Plyer1:please enter your name :"))
        
        self.symbol1=(input("\nPlyer1:please enter your Choice X or O :"))
        while self.symbol1 not in l :
            
          self.symbol1=(input("\nyour input is not correct please reenter your cohise :"))
            
        self.name2=(input("\nPlyer2:please enter your name :"))
        self.symbol2=(input("\nPlyer2:please enter your Choice X or O :"))
        while (self.symbol2 not in l) or (self.symbol2 is self.symbol1) :
            self.symbol2=(input("\nyour input is not correct please reenter your cohise :"))
        return [self.name1,self.name2,self.symbol1,self.symbol2]    
    #def choise(self):
                
class playspace:
        def __init__(self,l2=0,info=0,score1=0,score2=0):
            self.score1=score1
            self.score2=score2
            self.l2=l2
            self.l2=[0,1,2,3,4,5,6,7,8]
            self.info=info
            
            #super().__init__()
            self.info=plaeyer.getInfo(self)
        def plot(self):    
            play={"col1" :self.l2[0:3],"col2" :self.l2[3:6],"col3" :self.l2[6:]}
            
            #l2=[1,2,3,4,5,6,7,8,9]
            print ("this is the play space :\n")
            tabel=pd.DataFrame(play,index=["row1","row2","row3"])
            print(tabel)
        def start(self):
            print("\n now all plyers have to roll the dice the player with grater result will start if the the two number are equal yao have to rol agen ")
            while(1):
                player1choice=(input("\nPlyer1:please press any key to roll the dice :"))
                x1=random.randint(6)
                print("\nthe number is :",x1)
                player2choice=(input("\nPlyer2:please press any key to roll the dice :"))
                x2=random.randint(6)
                print("\nthe number is :",x2)
                if x1 != x2:
                    break
            if x1>x2:
                print("\nPlyer1 will start ")
                return 1
            else:
                print("\nPlyer2 will start ")
                return 2
        def win(self):
            if self.l2[0]==self.l2[1] and self.l2[0]==self.l2[2]:
                return [1,0]
            if self.l2[3]==self.l2[4] and self.l2[3]==self.l2[5]:
                return [1,3]
            if self.l2[6]==self.l2[7] and self.l2[6]==self.l2[8]:
                return [1,6]
            if self.l2[0]==self.l2[3] and self.l2[0]==self.l2[6]:
                return [1,0]
            if self.l2[1]==self.l2[4] and self.l2[1]==self.l2[7]:
                return [1,1]
            if self.l2[2]==self.l2[5] and self.l2[2]==self.l2[8]:
                return [1,2]
            if self.l2[2]==self.l2[4] and self.l2[2]==self.l2[6]:
                return [1,2]
            if self.l2[0]==self.l2[4] and self.l2[0]==self.l2[8]:
                return [1,0]
            return [0,0]
        
        def cheack(self):
                #self.score1=0
                #self.score2=0
                result=playspace.win(self)
                if result[0]==1:
                    if self.l2[result[-1]]==self.info[2]:
                        print("/nthe winner is player1:",self.info[0])
                        self.score1=self.score1+1
                        print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                        return 1
                    if self.l2[result[-1]]==self.info[3]:
                        print("/nthe winner is player2:",self.info[1])
                        self.score2=self.score2+1
                        print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                        return 1
                return  0   
                    
        def game(self):
          
          playspace.plot(self)
          c=0
          
          
          while(1):
            y=playspace.start(self)
            playspace.plot(self)  
            #t=int(input("if you want to start the game please enter ( 1 ) to exsit ( 0 )"))  
            while(c<=8):
                if(y==1):
                  x=int(input("\nplayer1:please enter the position number:"))
                  while(str(self.l2[x]).isalpha()):  
                    x=int(input("\nplayer1:please enter the position number becase the position is taken:"))
                  self.l2[x]=self.info[2]
                  playspace.plot(self)
                  result=playspace.win(self)
                  ch=playspace.cheack(self)
                  if ch :
                      break
                  c=c+1
                  if c==9:    
                      print("there is no winner")
                      print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                      break
                  
                  x=int(input("\nplayer2:please enter the position number:"))  
                  while(str(self.l2[x]).isalpha()):  
                    x=int(input("\nplayer2:please enter the position number becase the position is taken:"))
                  self.l2[x]=self.info[3]
                  playspace.plot(self)
                  ch=playspace.cheack(self)
                  if ch :
                      break
                  c=c+1
                  if c==9:    
                      print("there is no winner")
                      print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                      break
                if(y==2):
                    x=int(input("\nplayer2:please enter the position number:"))  
                    while(str(self.l2[x]).isalpha()):  
                      x=int(input("\nplayer2:please enter the position number becase the position is taken:"))
                    self.l2[x]=self.info[3]
                    playspace.plot(self)
                    result=playspace.win(self)
                    ch=playspace.cheack(self)
                    if ch :
                      break
                    c=c+1
                    if c==9:    
                        print("there is no winner")
                        print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                        break
                    x=int(input("\nplayer1:please enter the position number:"))
                    while(str(self.l2[x]).isalpha()):  
                      x=int(input("\nplayer1:please enter the position number becase the position is taken:"))
                    self.l2[x]=self.info[2]
                    playspace.plot(self)
                    result=playspace.win(self)
                    ch=playspace.cheack(self)
                    if ch :
                      break
                    c=c+1
                    if c==9:    
                        print("there is no winner")
                        print("the score is \n",self.info[0]+" :",self.score1,"\n",self.info[1]+" :",self.score2)
                        break
                
                """""print(result)
                if result[0]==1:
                    if self.l2[result[-1]]==self.info[2]:
                        print("/nthe winner is player1:",self.info[0])
                        score1=score1+1
                        print("the score is \n",self.info[0]+" :",score1,"\n",self.info[1]+" :",score2)
                        break
                    if self.l2[result[-1]]==self.info[3]:
                        print("/nthe winner is player2:",self.info[1])
                        score2=score2+1
                        print("the score is \n",self.info[0]+" :",score1,"\n",self.info[1]+" :",score2)
                        break"""
                    
               
            
            t=int(input("if you want to play more please enter ( 1 ) to exsit ( 0 ):"))
            if t==0:
                break
            else:
                self.l2=[0,1,2,3,4,5,6,7,8]
                c=0
                
          
                        
            
                        
                
            
            
            
        
        
#a=plaeyer()

b=playspace()
b.game()
