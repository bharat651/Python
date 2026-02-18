def smallest_number_in_list(number,index):
    number=number[index:]
    print(min(number))
    
given_list=input().split(",")
index=int(input())
string_to_number=[]
for item in given_list:
    string_to_number+=[int(item)]
smallest_number_in_list(string_to_number,index)