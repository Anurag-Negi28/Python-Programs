n=int(input('Enter the number of inputs'))
lst=[]
x=[]
marks=[]
for i in range(n):
      name=input('Enter the name ')
      x.append(name)
      map(int,marks.append(input('Enter marks ').split()))
      x.extend(marks)
      lst.append(x)
for i,y in enumerate(lst):
      avg=(lst[i][1]+lst[i][2]+lst[i][3])/3
      print(f'Average of {lst[i]:s} is {avg:.2f}')
      
