s = input()
vowels = ["a","e","i","o","u"]
maxi,count = 0,0
for i in range(len(s)):
    if s[i] in vowels:
        count+=1
    else:
        if count>=maxi:
            maxi = count
        count = 0
if count>=maxi:
    maxi = count
print(maxi)
