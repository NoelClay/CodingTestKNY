# aa 0 3
# ab 1
# ac 2 4
# 
# 0 1 2 -> 1~3
# 1 2 3 -> 2~4
# 1 2 3 4 
#
# xyz 0 1 2
# 0 -> 1,1
# 1
# 2
#
# zzz 0
# yyy 1 3
# nnnn 2
# bbb 4
# 0 1 2 3 4 -> 
# 0 1 2 3 4
#
def get_candidate_list_function(source_list):
    gem_dictionary = {}
    for current_index, s in enumerate(source_list):
        if s in gem_dictionary:
            gem_dictionary[s].append(current_index)
        else:
            gem_dictionary[s] = [current_index]
    
    result = []
    
    while True:
        temp_list = []
        for d in gem_dictionary.values():
            # 현재 d는 밸류즈 리스트중에서 리스트값 하나만 뽑아온셈
            if len(d) > 1:
                temp_list.append()
        
        
def solution(gems):
    answer = []
    
    candidate_list = get_candidate_list_function(gems)
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))