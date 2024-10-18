
def two_pointer(source_list, target_number_zero):
    left_index = 0
    right_index = len(source_list)-1
    alter_answer_set_list = []
    
    while True:
        test_value = source_list[left_index] + source_list[right_index]
        # alter_answer_set_list.append([test_value, left_index, right_index])
        alter_answer_set_list.append([abs(test_value), left_index, right_index])
        
        if test_value == target_number_zero:
            # alter_answer_set_list.append([test_value, left_index, right_index])
            # break
            return [test_value, left_index, right_index]
        elif test_value < target_number_zero:
            left_index += 1
        else:
            right_index -= 1
        
        # alter_answer_set_list.append([abs(test_value), left_index, right_index])
        
        if left_index >= right_index:
            break
    
    # close_alter_answer_set_list = alter_answer_set_list.copy()
    alter_answer_set_list.sort()
            
    
    return alter_answer_set_list[0]
        
n = int(input())

# data_list = [map(int, input().split()) for _ in range(n)]
data_list = list(map(int, input().split()))
result = two_pointer(data_list, 0)

print(f"{str(data_list[result[1]])} {str(data_list[result[2]])}")