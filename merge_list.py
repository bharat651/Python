def merge_the_list(a,b,merge_list=[]):
    if(len(b)==0):
        return merge_list
        
    else:
        merge_list.append(a[0])
        merge_list.append(b[0])
        return merge_the_list(a[1:],b[1:],merge_list)

A=input().split()
B=input().split()
result=merge_the_list(A,B)
print(result)