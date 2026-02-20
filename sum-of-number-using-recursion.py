def get_sum(numbers):
    sum_of_numbers=0
    if(len(numbers)==0):
        return sum_of_numbers
    return numbers[len(numbers)-1]+get_sum(numbers[:len(numbers)-1])

numbers = input().split()
new_num=[]
for item in numbers:
    new_num+=[int(item)]
sum_of_numbers = get_sum(new_num)
print(sum_of_numbers)