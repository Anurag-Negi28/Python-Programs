def check(t):
    if t==1:
        print(True)
    else:
        print(False)
if __name__ == '__main__':
    s = input()
    t=0
    for i in s:
        if i.isalnum():
         t=1
         break
    check(t)
    t=0
    for i in s:
        if i.isalpha():
         t=1
         break
    check(t)  
    t=0
    for i in s:
        if i.isdigit():
         t=1
         break
    check(t)  
    t=0
    for i in s:
        if i.islower():
         t=1
         break
    check(t)
    t=0
    for i in s:
        if i.isupper():
         t=1
         break
    check(t)      
