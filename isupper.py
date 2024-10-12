def function(str1,str2):
    str=str1+str2
    c=""
    for i in str:
        if i.isupper():
            c=c+i
    return c
str1=input()
str2=input()
print(function(str1,str2))





