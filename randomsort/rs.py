import random
n= int(input("Enter no of elements in list"))-1
li=list(map(str,input().split()))
while True:
    count=0
    for x in range(n):
        if li[x]<li[x+1]:
           count=count+1
        else:
            break
    if count==n:
       break
    a=random.randint(0,n)
    b=random.randint(0,n)
    li[a],li[b]=li[b],li[a]

print(" ".join(li))

