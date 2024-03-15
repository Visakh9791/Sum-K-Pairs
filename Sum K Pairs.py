def convert_num_list_to_num(str_num_list): 
    numlist=[]
    for item in str_num_list:   
        num=int(item)
        numlist.append(num) 
    return numlist

def get_unique_pairs(num_list,pair_sum):
    unique_pairs_set=set() 
    for cur_index in range(len(num_list)-1): 
        num_1= num_list[cur_index]
        num_2= pair_sum - num_1
        
        remaining_list=num_list[cur_index+1: ] 
        if num_2 in remaining_list:
            pair=(num_1,num_2)
           
            sorted_pair=tuple(sorted(pair))  
            unique_pairs_set.add(sorted_pair)
    return (unique_pairs_set) 