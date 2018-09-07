import random
from random import randint
n= int(input(""))
li=[int(input()) for x in range(n)]
while True:
    a=random.randint(0,len(li)-1)
    b=random.randint(0,len(li)-1)
    s1=li[a]
    li[a]=li[b]
    li[b]=s1
    count=0
    for x in range(len(li)-1):
        if li[x]<li[x+1]:
           count=count+1
        else:
            break
   
    if count==len(li)-1:
       break
    
for x in range(len(li)):
    print(li[x],end=' ')

