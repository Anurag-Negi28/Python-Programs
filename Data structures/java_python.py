java={'John','Jack','Jill','Joe'}
python={'Jake','John','Eric','Jill'}
print('No. of students in python are: ',len(python))
print('No. of students only in java are: ',len((java)-(python)))
print('No. of students only in python are: ',len((python)-(java)))
print('No. of students in both java and python are: ',len((python)&(java)))
print('No. of students either in python or java but not in both are: ',len((python)^(java)))
print('No. of students in java or python are: ',len((python)|(java)))
