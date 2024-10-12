r=0
print("Enter a number ")
n=input()
n=int(n)
num=n
while(n>0):
    d=n%10
    r=++d+r*10
    n=n//10
if(num==r):
    print("It is palindrome ")
else:
    print("Not a palindrome")


