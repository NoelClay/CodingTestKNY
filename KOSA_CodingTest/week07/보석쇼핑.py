#식을 세우기 어려웠는데 머리 속에서 시뮬레이션을 여러번 돌리다가 아이디어를 얻어냈다. 20분 걸린듯
#타겟 넘버는 결국 모든 조건을 만족하면서 즉 n명을 처리가능한 경우를 만족하면서 가장 최소 값을 얻어내야한다.
#일반적으로 생각했을때 최대 비효율 값은 n을 times로 나눈 값(나머지가 있다면 +1) 만큼 
# times의 최대요소값에 곱한 만큼을 소요시간이라고 따지면 정말 비효율적으로 다른 심사위원들이 놀거다.
#그런데 상관없다. 이진탐색 할거고, 해를 찾는건 n을 만족하는 최소 시간이니까. 타겟 시간을 심사위원 수만큼 돌린다음에 나눈 몫
#만큼 카운트 하면 그 시간안에 처리 가능한 인원수를 누적합으로 얻어낼 수 있다.

def binary_search_function(source_list, target_count):
    s_value = 1
    e_value = int(max(source_list))
    f_result = int(target_count)/len(source_list)
    i_result = 0
    if f_result%1 != 0:
        i_result = int((f_result//1)+1)
    else:
        i_result = int(f_result)
    e_value *= i_result
    #복잡하지만 최대값은 일단 제한 둘 수 있다.

    while True:
        m_value = (s_value + e_value)//2
        cnt = 0
        
        for s in source_list:
            cnt = cnt + m_value//s
        
        #최소값을 찾는 조건식 크면 줄이고 같아도 줄여 그렇게 타이트하게 줄여낸다음에
        if cnt >= target_count:
            e_value = m_value-1
        else:
            s_value = m_value+1
            
        #줄이고 줄인 e_value가 쥐어짜내진 상태면 최소값 스타트밸류를 출력
        if s_value > e_value:
            return s_value
        
    

def solution(n, times):
    return binary_search_function(times, n)

print(solution(6, [7,10]))