def get_largest_square(numbers):
    each_number=int(numbers[0])**2
    if(len(numbers)==1):
        return each_number
    return max(each_number,get_largest_square(numbers[1:]))

numbers = input().split()
result=get_largest_square(numbers)
print(result)
