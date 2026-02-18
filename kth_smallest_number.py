def kthSmallestNumber(number):
    print(number[Kth-1])
N=input().split(",")
Kth=int(input())
number=[]
for item in N:
    number+=[int(item)]
number=sorted(number)
kthSmallestNumber(number)