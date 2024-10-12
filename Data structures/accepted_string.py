string =input("Input a string ") 
string1 = string.replace(" ","")
count= ""
for i in string1[0:len(string):2]:#or for i,char in enumerate(string):(we can use enumerate function to access both index and character in a string)
    count+=i
print("resultant_string: ",count)
count1=count[::-1]
print("expected_output: ",count)
