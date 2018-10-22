import numpy as np
from collections import defaultdict, Counter
fopen = open('A-large-practice.in','r')
lines = fopen.readlines()

a = []
b = []

for i in lines:
    b.append(i)
a.append(b[0][:-1])
for i in range(1,len(b),2):
    a.append([b[i][:-1],b[i+1][:-1]])
num = a[0]
list_file = open('jam.txt', 'w')
for i in range(1,int(num)+1):
    number,array=a[i][0],a[i][1]
    array = array.split()
    array = [int(x) for x in array]
    array = sorted(array)
    #print(array)
    n = len(array)
    #print(array)
    ans = 0;
    occurances = defaultdict(lambda :0)
    zero = 0
    for y in range(n-1,-1,-1):
        if array[y] ==0:
            zero +=1
        #print(y)
        for x in range(y-1,-1,-1):
            #if occurances[array[y]*array[x]]<0:
                #print(occurances[array[y]*array[x]])
            ans = ans + occurances[array[y]*array[x]]
        #print(occurances[array[y]] )
        occurances[array[y]] += 1
    print(int(ans+(n-zero)*zero*(zero-1)/2))        
    print("Case #{}: {}".format(i,int(ans+(n-zero)*zero*(zero-1)/2)),file=list_file)   
    