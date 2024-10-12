customer_details={1001:'john',1004:'Jill',1005:'Joe',1003:'Joe',1003:'Jack'}
print('Customer details are:',customer_details)
print('Number of customers are:',len(customer_details))
print('Customer names are:',sorted(customer_details.values()))
del customer_details[1005]
print('customer details after updation:',customer_details)
customer_details[1003]='Mary'
print('customer details after updation:',customer_details)
cust_id=int(input('Customer id: '))
for i in customer_details:
    if(i==cust_id):
        print('Exist')
        break
    else:
        print('not exist')
        break
