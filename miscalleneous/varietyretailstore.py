total_cost=0
a=input("Enter the furniture you want to purchase")
n=int(input("Enter the quantity of furniture you want to purchase"))
found=False
furniture={"Sofa set":20000,"Dining Table":8500,"T.V Stand":4599,"Cupboard":13920}
for key,i in furniture.items():
      if(key==a):
       found=True
       total_cost=n*furniture[key]
       print(total_cost)
       break
       found==False
       print("Error")
       print("Bill amount is : 0")
