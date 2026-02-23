def extent_list(N):
    new_list=[]
    for i in range(N):
        mini_list=input().split()
        new_list.extend(mini_list)
        new_list.sort()
    return new_list

N=int(input())
result=extent_list(N)
print(result)