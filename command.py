if _name_ == '_main_':
    N = int(input())
    list=[]
    for i in range(N):
        command,*value=input().strip().split()
        value=list(map(int,value))
    if (command=="insert"):
        list.insert(value[0],value[1])
    if (command=="append"):
        list.append(value[0])
    if (command=="print"):
        print(list)
    if (command=="remove"):
        list.remove()
    if (command=="sort"):
        list.sort()
    if (command=="pop"):
        list.pop()
    if (command=="reverse"):
        list.reverse()
