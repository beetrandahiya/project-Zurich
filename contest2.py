from itertools import permutations, combinations
nm=input().split()
n=int(nm[0])
m=int(nm[1])
w=[]
for i in range(m):
    w.append(int(input()))

while(len(w)<n):
    w.append(0)

l=list(permutations(w))

sp=0

for i in range(len(l)):
    s=0
    li=l[i]
    for j in range(0,n):
        for k in range(j,n):
            s+=abs(k-j)*li[j]*li[k]

    if(s>sp):
        sp=s

print(sp)


    
    