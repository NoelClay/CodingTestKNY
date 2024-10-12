# 그냥 단순 이진탐색 만들어볼까?
# 먼저 입력이 들어올때 정렬하고, 중앙 인덱스로 중앙값 선택한뒤 n번 탐색하며 빼서 누적합을 구해 타겟 넘버인지 체크
# 작으면? 끝값= 중앙값-1 크면? 초기값=중앙값+1

n, m = map(int, input().split())

data_list = sorted(map(int, input().split()))

def binary_search_function(source_list, target_number):
    s_index = 0
    s_value = source_list[s_index]
    e_index = len(source_list)-1
    e_value = source_list[e_index]
    while True:
        m_value = (s_value+e_value) // 2
        cnt = 0    
        for s in source_list:
            temp = s-m_value
            temp = max(temp, 0)
            cnt = cnt + temp
        
        if cnt == target_number:
            return m_value
        elif cnt > target_number:
            s_value = m_value+1
        else:
            e_value = m_value-1
        
        if s_value > e_value:
            return m_value
        
        
print(binary_search_function(data_list, m))