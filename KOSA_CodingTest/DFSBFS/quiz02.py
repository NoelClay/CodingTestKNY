#결국 DFS가 필요함. 따라서 재귀로 구현
#새로운 숫자를 만날때 마다 plus minus 2개 다 호출 2배씩 쌓임. 마지막에 벗겨지는 순간 반환값을 뱉을거.
#그 때 그새기가 원하는 타겟인지 검사해서 answer+=1 쭉쭉

#그런데 왜 점화식짜기가 어렵지.. 수학적으로 식을 어캐세워야 될지 모르겠어서.. 그냥 반복문..
#반복문은 겁나 간단하다.. 근데 점화식이 궁금하다. 점화식으로 푼사람한테 설명점 해다라고 해야겠다.
def solution(numbers, target):
    answer = 0

      #최초 세팅값은 계산에 영향을 주지 않게
    stack = [[-1,0]]
    maxidx = len(numbers)-1
    while(stack):
        curidx, curval = stack.pop()
        if curidx == maxidx: 
            if curval == target:
                answer += 1
            else:
                continue
        else:
            stack.append([curidx+1, curval+numbers[curidx]])
            stack.append([curidx+1, curval-numbers[curidx]])
    return answer    
