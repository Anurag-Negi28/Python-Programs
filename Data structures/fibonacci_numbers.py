n=int(input("Enter the value: "))
fibonacci_numbers=[0,1]
for i in range(2,n):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(fibonacci_numbers)
