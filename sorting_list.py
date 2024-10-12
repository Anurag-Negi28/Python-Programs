if __name__ == '__main__':
    list=[]
    smallest=100
    s_smallest=100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        value=[name,score]
        list.append(value)
    for i in range(len(list)):
        if list[i][1]<smallest:
            s_smallest=smallest
            smallest=list[i][1]
        if list[i][1]<s_smallest and list[i][1]!=smallest:
            s_smallest=list[i][1]
    lst=[]
    for i in range(len(list)):
        if list[i][1]==s_smallest:
            lst.append(list[i][0])
    lst.sort()
    for i  in lst:
        print(i)
