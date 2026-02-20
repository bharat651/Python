def get_sum_of_squares(numbers):
    if(len(numbers)==0):
        return 0 
    else:
        return (numbers[len(numbers)-1]**2)+get_sum_of_squares(numbers[:len(numbers)-1])
    
numbers = input().split()
new_list=[]
for item in numbers:
    new_list+=[int(item)]
squares_sum = get_sum_of_squares(new_list)
print(squares_sum)