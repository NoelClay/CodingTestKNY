# 숫자를 입력받으면 거까지 도달하는 최단거리 반환

#최소값 비교를 쉽게 하기 위해 inf 상수 추가
INF = 987654321

# 숫자 입력 받기
N = int(input())

# 최단거리 저장용 리스트 추가
dptable = []

#반복할때마다 1씩 증가한 값이 추가되는게 아니다 건너뛰어 저장할수도 있으니 미리 인덱스가 생성되어 있어야함. N은 1에서 30000까지 들어온다고 한다 그래서 그냥 30001 추가
dptable = [0 for _ in range(30001)]
#1까지 연산이기에 1은0 추가하고 시작인덱스도 1로 바꾸니 오류 해결
dptable[1] = 0

#반복문 끝내는 플래그와 시작용 인덱스
isEnd = False
i = 1


#이전 경우의 수 중에서 가장 최소값에서 +1 해야하는 함수
def checker(x):
  # print(x)
  # 초기화
  global INF, dptable
  a = []
  res = []
  # 1로 빼는 경우의 수 가능하면 일단 빼고
  if x > 0:
    a.append(x - 1)
  #각각 나누어 떨어지는 경우의 수가 가능한 경우 값 초기화
  if x % 2 == 0:
    a.append(int(x / 2))
  if x % 3 == 0:
    a.append(int(x / 3))
  if x % 5 == 0:
    a.append(int(x / 5))

  # 이제 각 dp 테이블을 순회하며 그 중 최소값을 선택하여 +1을 저장함.
  for j in a:
    res.append(dptable[j])

  return min(res) + 1


#반복문 시작
while not isEnd:
  i += 1
  dptable[i] = checker(i)
  # print("i : " + str(i))
  # print("dptable : " + str(dptable[i]))
  if i == N:
    isEnd = True

print(dptable[N])
#print(dptable)
