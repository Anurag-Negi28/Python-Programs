if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    largest=-200
    sec_largest=-200
    for i in arr:
        if(i>largest):
            sec_largest=largest
            largest=i
        if(i>sec_largest and i!=largest):
            sec_largest=i
    print(sec_largest)
        
        
