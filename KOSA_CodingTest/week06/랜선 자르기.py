#그니까 타겟넘버만큼 만들 수 있는 최대 길이를 구하는건데. 이 최대길이를 2진 탐색으로 찾아야겠네.
#시작값 0cm 끝값 최대길이 값 중앙값 0+최대길이 //2

def binary_search(source_list, target_number):
    # s_value = 0
    #길이는 1 이상으로
    s_value = 1
    e_value = max(source_list)
    while True:
        m_value = (s_value+e_value)//2
        cnt = 0
        for s in source_list:
            cnt = cnt + (s//m_value)
        
        # if cnt == target_number:
        #     return m_value
        #타겟넘버를 넘어가도 좋으니 최대 길이가 될때까지 계속 탐색하기 즉 타겟넘버가 되는 경우의 수가 여러개 일 수 있음
        if cnt >= target_number:
            s_value = m_value + 1
        else:
            e_value = m_value - 1
        
        # if s_value>e_value:
        #     return m_value
        #아 m_value가 타겟넘버인지는 관심없이 더이상 나누기가 불가능한 수준까지 반복문을 타이트하게 돌리고 나면
        #항상 s_value, m_value가 e_value를 넘어가는 지경까지 반복문을 돌리게 된다.
        #따라서 그 바로 직전 e_value가 반환값이 되는거.
        if s_value>e_value:
            return e_value
        
n, m = map(int, input().split())

data_list = [int(input()) for _ in range(n)]

print(binary_search(data_list, m))