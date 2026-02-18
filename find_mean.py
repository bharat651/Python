def findMean(number,lenth):
    sum_of_number=sum(number)
    Mean=sum_of_number/lenth
    print(Mean)

N=input().split(",")
lenth=len(N)
number=[]
for item in N:
    number+=[int(item)]
findMean(number,lenth)