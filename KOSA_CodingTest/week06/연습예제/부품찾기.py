#접근 방법
#n개의 데이터가 주어지는데 그 n이 굉장히 크다.
#그런데 단순 데이터만 찾아주면 된다. 그러면 퀵소트로 정렬한뒤에 2진 탐색하는게 더 빠르다.

N = int(input())
pList = sorted(map(int, input().split()))
M = int(input())
sList = sorted(map(int, input().split()))

#찾는게 나오면 yes 출력 없으면 no 출력 이진탐색 구현 bSearch
def binary_search(source_list, target_number):
    s_index = 0
    m_index = len(source_list)//2
    e_index = len(source_list)-1
    while True:
        if source_list[m_index] == target_number:
            return m_index
        elif source_list[m_index] > target_number:
            e_index = m_index-1
            m_index = (s_index+e_index)//2
        elif source_list[m_index] < target_number:
            s_index = m_index+1
            m_index = (s_index+e_index)//2
        if s_index > e_index:
            return -1
        
for s in sList:
    if binary_search(pList, s) == -1:
        print("no")
    else:
        print("yes")

