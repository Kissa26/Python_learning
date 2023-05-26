from urllib.request import urlopen
from bs4.element import SoupStrainer
import requests
import lxml 
from bs4 import BeautifulSoup

import json


global l , nr

l={
     "name": ["amount ","unit"]
     
     }

nr = 0

def verif(name,a):
    global nr
    b=[]
   
    for index in range(0,nr):
           if l.get(name) != None :
               x=l[name]
               y=str(x[0])
               print(y)
               y+='+'+str(a)
               b.append(y)
               b.append(x[1])
               l[name]= b
               return True 
    nr+=1
    return False 
        

def reteta(url):
    
    
    global nra,u,name
    f = requests.get(url)
    soup = BeautifulSoup(f.content,'lxml')
    
    

    for i in soup.find_all(attrs={"class" : "wprm-recipe-ingredient"} ):
       b=[]
       if i.find(attrs={"class" : "wprm-recipe-ingredient-name"}) != None :
        name= i.find(attrs={"class" : "wprm-recipe-ingredient-name"}).text
       if i.find(attrs={"class" : "wprm-recipe-ingredient-amount"}) != None :

         a=i.find(attrs={"class" : "wprm-recipe-ingredient-amount"}).text
       if i.find(attrs={"class" : "wprm-recipe-ingredient-unit"}) != None :
         u=i.find(attrs={"class" : "wprm-recipe-ingredient-unit"}).text
     
       if verif(name,a) == False:
           b.append(a)
           b.append(u)
           l[name]=b
           #nr+=1   
    jsonf=[]
   
    #jsonStr=json.dumps(l)
         
   # jsonf.append(jsonStr)
    #print(jsonStr)
    with open("sample.json", "w") as outfile:
       json.dump(l, outfile)
             
    
def main():
   
    while (1):
        
        print("introduceti linkul retetei")
        if input() !=  "quit" :
           a=input()
           reteta(str(a))
        else:
           break
    
main()