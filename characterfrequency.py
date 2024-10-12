#calculating frequency of characters in a string using dictionary
s=input()
s=s.upper()
d={}
for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
for i in d:
    print(d[i],i,sep='')
