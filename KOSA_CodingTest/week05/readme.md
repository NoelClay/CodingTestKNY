# 5주차 DP and BitMasking

## 문제 리스트 

1. 동전2
2. IP주소

<br>

### 동전2

<br>

#### 풀이접근
1. 무조건 더해서 원하는 타겟 넘버를 만드는 최소한의 경우의 수를 구하는 문제임.
2. dfs를 이용해서 푸는 것보다 DP가 효율적인건 이미 이전 최적해가 있다면 그걸 이용하면 되기 때문임
<br>

##### 필요한 데이터
1. 총 돈전의 수, 타겟 넘버
2. 동전의 값 배열
3. 각 타겟넘버마다 만들 수 있는 계속 갱신되는 후보해 리스트
4. DP 테이블
<br>

##### 필요한 기능
1. 최소 경로를 반환해야하므로 DP테이블에는 큰값으로 미리 초기화
2. 타겟 넘버가 동전값일때 미리 DP테이블에 초기화
3. out of Index를 제외하는 후보해 만들어서 마지막에 최소 경로값 +1로 dp값 갱신
   
<br>

##### 해맸던 점
- out of index를 유발하는 초기값 설정을 찾는데 오래걸림

<br>

### IP주소(실패)

<br>

#### 풀이접근
1. 앞의 32-m자리가 일치한다고 하는데 그 일치하는 녀석이 네트워크 주소
2. 그런데 m은 최소값이어야됨. 그래서 모든 들어오는 주소에 &연산자로 갱신하여 나오는 값이 네트워크 주소 그자체
3. 왜냐하면 m은 최소값으로 맞출거니까 
4. 네트워크 주소를 만들어내는 m을 찾으면 그 m을 기준으로 앞은 전부 1 뒤는 전부 0이면 네트워크 마스크도 도출

<br>

##### 필요한 데이터
1. 네트워크 주소를 만들 배열, 네트워크 마스크를 만들 배열
2. $$ 2^{0}~에서 ~ 2^{7}까지를~ 저장한~ 배열$$

<br>

##### 필요한 기능
1. 입력이 들어올때마다 네트워크 주소 배열에 &연산자 처리하여 가장 큰 값의 네트워크 주소를 만든다.
2. 그 네트워크 주소를 가지고 m을 만든다.
3. m을 가지고 네트워크 마스크를 만든다.
   
##### 해맸던 점
- 그래서 m을 어떻게 만들건데를 해결을 못한 상황..