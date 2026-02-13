N=int(input())

for i in range(N):
    K=0
    M=int(input())
    for j in range(1,M+1):
        if(M%j==0):
            K+=1
    if(K==2):
        break
print(M)