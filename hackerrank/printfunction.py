#The included code stub will read an integer n from STDIN.

#Without using any string methods, try to print the following:123...n
n = int(input())
if n>=1:
    for i in range(1,n+1):
        print(i,end="")#used to print in the same line with characters in semi colon
            
