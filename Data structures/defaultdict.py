#calculating frequency of a character in a string using default dictionary(Ignoring cases)
from collections import defaultdict
s=input()
s=s.upper()
d=defaultdict(int)
for char in s:
        d[char]+=1
for i in d:
    print(d[i],i,sep='')
