def sum_of_the_digits(number):
    # Complete this recursive function
    each_number=int(number[0])
    if(len(number)==1):
        return each_number
    return each_number+sum_of_the_digits(number[1:])


number = int(input())
# Call the sum_of_the_digits function
result=sum_of_the_digits(str(number))
print(result)