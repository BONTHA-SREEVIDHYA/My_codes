s=input()
n=len(s)
l=[]
f=input()
print(s[0])
for i in range(0,n):
    for j in range(1,n+1):
        l.append(s[i:j])
if f in l:
    print(l.count(f))
    
        
