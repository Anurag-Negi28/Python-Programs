str1=input("enter first string: ")
str2=input("enter second str: ")
str=''
print(f'Actual string : {str1:s}')
print(f'Actual string : {str2:s}')
for i in str1:
    if i.isupper():
        str+=i
for i in str2:
    if i.isupper():
        str+=i
print(str)
    
