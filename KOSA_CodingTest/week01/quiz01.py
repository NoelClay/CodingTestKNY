from collections import deque

def solution(bridge_length, weight, truck_weights):
  answer=0
  time = 0
  #그냥 반복문마다 time을 증가시키면 시간 초과다. n^2 따라서 스킵의 기술이 필요함.
  #딜레이가 될때는 과감하게 앞에거가 나갈때까지 초를 계산해서 나간뒤에 초를 리셋팅하고 다시 추가해야함.
  timeOnRoad = deque()
  idxPrevTruckOnRoad= 0
  idxCurrentTruck = 0
  weightCurrent = 0
  #각 시점마다 상태를 리세팅하기 위한 반복문이라고 다시 생각 0초일때는? 추가만할거야.
  #-> 여기가 틀렸다. 0.1초 1.1초는 신경 쓰지 않는다. 그저 0초 순간 1초 순간이다.
  #문제에서 제시한 0초때는 아무것도 안하고 있는 상태이고, 1초+길이가 첫번째 요소가 이미 빠져나간 상태
  #딱 그렇게 생각하고 풀어야함. 여기를 0으로 세팅하고 푸니까 답이 안나왔었다.
  while idxCurrentTruck<len(truck_weights):
    time+=1
    # print("반복문 스타트")
    # print(time)
    # print(truck_weights[idxCurrentTruck:])
    # print(timeOnRoad)
    

    #case0: 지금 나와야 되는 애가 있다. 나올놈 먼저 나오고 나서 들어갈지 말지 정하지
    if timeOnRoad and timeOnRoad[0]+bridge_length == time:
      #나올 시간이 되었으면 나와야지
      # print("지금 나오는 애가 있어")
      # print(truck_weights[idxPrevTruckOnRoad])
      timeOnRoad.popleft()
      weightCurrent -= truck_weights[idxPrevTruckOnRoad]
      idxPrevTruckOnRoad += 1
    #case1: 들어갈 수 있어.
    if weightCurrent + truck_weights[idxCurrentTruck] <= weight:

      # print("지금 들어가는 애가 있어")
      # print(truck_weights[idxCurrentTruck])
      timeOnRoad.append(time)
      weightCurrent += truck_weights[idxCurrentTruck]
      idxCurrentTruck += 1
    #나올놈 나오고 들어갈 놈 들어갔다. 그런데 아무것도 안한경우가 있을거 아닌가. 아니다 정확히는
    #들어가고 싶었는데 못들어간 경우. 그때는 무의미한 반복으로 time++ 하는게 아니라, 앞에놈이
    #나올 시간으로 시간을 스킵해주는 로직이 필요하다.
    elif timeOnRoad:
      # print("딜레이가 시작되었어")
      
      # print("맨앞에 있는 " + str(timeOnRoad[0]) + " 이놈이 빠져나가기 직전은")
      time = timeOnRoad[0] + bridge_length -1
      #-1을 해준 이유는 명확하다 지금 이거는 실질적인 시간이 아니라 스킵용 코드이다. 이 트럭이 빠져나오기 바로 직전까지로 시간을 세팅해준거다. 아 이걸 생각 못했었네...
    

    #   print("현재시간을 " + str(time) +" 으로 맞출거야")
      
    # print("반복문 최종상태야")
    # print(time)
    # print(truck_weights[idxCurrentTruck:])
    # print(timeOnRoad)

  if timeOnRoad:
    
    answer = max(time, timeOnRoad.pop() + bridge_length )
  else:
    answer = time
  #timeOnRoad.pop() 은 이게 올라가 있는 시점이다. 즉 달리고 있다. 여기에 브릿지 길이만큼 더하면
  #끝나는 시간이 반환
  
  return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
