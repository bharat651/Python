def medianOfNumber(string_to_number,lenth_of_list):
    if(lenth_of_list%2==0):
        midel_index=lenth_of_list//2 
        result=sum(string_to_number[midel_index - 1 :midel_index + 1])/2
    else:
        midel_index=lenth_of_list//2
        result=string_to_number[midel_index]
    print(result)
the_input=input().split(",")
string_to_number=[]
for item in the_input:
    string_to_number+=[int(item)]
string_to_number=sorted(string_to_number,reverse=False)
lenth_of_list=len(string_to_number)
medianOfNumber(string_to_number,lenth_of_list)