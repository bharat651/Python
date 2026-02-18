def smallest_sum_of_N_element(number,no_of_element):
    number=sorted(number,reverse=False)
    result=sum(number[:no_of_element])
    print(result)
    
given_list=input().split(",")
no_of_element=int(input())
string_to_number=[]
for item in given_list:
    string_to_number+=[int(item)]
smallest_sum_of_N_element(string_to_number,no_of_element)