# 7주차 투포인터

## 문제 리스트 

1. 용액 [링크](https://www.acmicpc.net/problem/2467)
2. [카카오 인턴]보석 쇼핑 [링크](https://school.programmers.co.kr/learn/courses/30/lessons/67258)

<br>

### 용액

<br>

#### 풀이접근
1. 정렬이 되어 있다는 전재라면 인덱스0 값과 인덱스끝 값을 더한건 평균과 가까울것. 그런데..
2. 0보다 작다면? 최소값이 최대값보다 절대값이 더 크다는 소리(일단 마이너스니까..) 그러므로 왼쪽 인덱스를 1만큼 증가시키고 다시 비교해야지 0과 더 가까워지는지를 체크하겠지.
3. 이러한 아이디어로 0보다 클때 오른쪽 인덱스를 왼쪽으로 당겨온다.
4. 그러다가 둘이 만나다못해 왼쪽인덱스가 오른쪽 인덱스를 넘어가면 끝끝내 0이 되는 조건에 도달을 못한것.(아웃오브 인덱스가 안되게 유의 불가능한 인덱스 된순간 참조하지말고 종료시키기)
5. 하지만 문제는 0을 찾는게 아니라 0이랑 가까운 조건을 반환하므로 모든 후보해들을 저장해놓고 그중 최소절대값 조건을 반환하면 됨.

<br>


##### 해맸던 점
1. 

<br>

### 보석 쇼핑

<br>

#### 풀이접근
1. 이 문제를 이렇게 풀 수 있는지는 모르겠다만... 일단 전체 리스트가 들어올때 선형탐색하며 키-밸류 쌍으로 저장
2. 키는 해당 리스트 요소의 문자열 값이고,
3. 밸류는 해당 문자열 요소가 리스트의 몇번째 인덱스에 있었는지를 저장한 리스트다.
4. 이후 모든 문자가 조합되어야 하므로 밸류 인덱스를 일단 뽑아서 가장 작은 값과 가장 큰값을 하나의 인스턴스로 뽑아냄.
5. 이후 하나씩 가능한 후보해(가능한 모든 경우의 수랑은 차원이 다르게 경우의수가 좁혀짐..)를 계속 만들어서 뽑아냄. 
6. 그 중 가장 길이가 짧으면서 시작 인덱스도 가장 작은 인스턴스가 답임.

<br>
   
##### 해맸던 점
1. 