def switch_pairs(a_list):
    for i in range(1,len(a_list),2):
        return_value = a_list.pop(i)
        a_list.insert(i-1,return_value)
        

switch_pairs(['four', 'score', 'and', 'seven', 'years', 'ago'])

#output = ['score', 'four', 'seven', 'and', 'ago', 'years']
