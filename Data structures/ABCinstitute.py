student_name={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
print(student_name)
l=-1
sl=-2
for i in student_name:
    if student_name[i] > l:
        sl=l
        l= student_name[i]
    elif student_name[i] > sl and l!= student_name[i]:
        sl= student_name[i]

print("TOP TWO SCORERS ARE:->",l,sl)
    
sum=0
for i in student_name:
    sum=sum+int(student_name[i])
print("AVERAGE MARKS OF INSTITUTE IS:->")
print(sum/len(student_name))
