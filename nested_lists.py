n = int(input()) 
c = [] 
d = [] 
for i in range(n): 
    a =[]  
    for j in range(2):  
        if j == 0: 
            a.append(input())  
        else: 
            x=float(input()) 
            a.append(x) 
            d.append(x)  
    c.append(a)  
c.sort() 
d.sort() 
d = list(dict.fromkeys(d)) 
for i in range(0,n): 
    if d[1] == c[i][1]: 
        print(c[i][0])
