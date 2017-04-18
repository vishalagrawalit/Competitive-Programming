string = input()
vowels = ['a','e','i','o','u','y']
count=0
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        print("No")
        break
    if string[i] in vowels and string[i+1] in vowels:
        print("No")
        break
    else:
        count+=1
if count==len(string)-1:
    print("Yes")
    
