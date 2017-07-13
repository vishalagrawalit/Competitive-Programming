for _ in range(int(input())):
    s = input()
    
    new,string = '',''
    
    for i in range(len(s)-1, -1, -1):
        if s[i]!='.':
            string += s[i]

        if s[i]=='.' or i==0:
            new = "." + string + new
            string = ''
            
    print(new[1:])
 
