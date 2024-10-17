<h1>[1번 사다리 문제]</h1>
<br>
최악의 경우를 고려할때 1초마다의 동작을 일일히 시뮬레이션 구현하기에는 n^2이라 무조건 시간초과
<br>

그래서 최악의 경우인 딜레이가 발생하는 경우엔 어차피 다리를 건너고 있는 첫번째 녀석이 나가기 전까지는 의미없는 동작이라
<br>

초를 스킵하는 로직이 필요했음
<br>

그러기 위해선 첫번째 녀석이 언제 들어갔는지를 저장해야. 첫번째 녀석이 나오는 시간대로 세팅하면 초스킵 가능할거
<br>

그러기 위한 자료형으로 들어간 순서대로 나오고 알아서 맨 앞자리로 정렬을 따로 할필요가 없는 큐를 사용하기로함.
<br>

<h2> [필요한 데이터] </h2>
1. 다리의 길이 <br>
2. 줄지어 서있는 트럭무게 리스트<br>
3. 다리가 버티는 무게<br>
4. 현재 누적된 무게<br>
<br>

<h2> [필요한 기능] </h2>
<br>

1. 퇴장 체크: 지금 다리 건너고 있는것들 중 가장 앞에 있는애가 다 건넜는지?
<br>

2. 입구컷 체크: 지금 들어가려는 트럭의 무게를 합했을때 버틸수 있는지?
<br>

  -> 3. 만약 입구컷 당했으면 딜레이걸린거. 맨앞에 있는놈이 나가기 직전 타임으로 점프
<br>

다시 1번부터 3번까지 반복 언제까지? 마지막 친구가 다리를 건널때까지
<br>

반복이 끝나면 다리 제일 마지막으로 들어온애가 나가야 되는 시간으로 또 점프
<br>

그 시간 + 1 이 정답
<br>


<br>

<h1>[2번 레이저 문제]</h1>
<br>

그림이 어지러워서 당황했었는데 생각보다는 간단했었음. 단 무조건 입력해주는 쪽에서 오류없게 입력을 해준다는 가정이면 간단
<br>

분기는 2갈래 ( 이거냐 ) 이거냐에 따라 동작이 다름
<br>

( 이거는 무조건 저장 그리고 입력해주는 쪽에서 무조건 ( 이걸로 시작할거니까 예외 업슴
<br>

) 이거는 2가지 케이스가 있음 직전에 파싱해서 가져온 데이터가 ) 닫는 괄호면 이미 레이저를 쏘고 막대기 끝을 가리키는 괄호고
<br>

이전 타이밍에 가져온 데이터가 ( 여는 괄호였으면 레이저를 쏴야된다는 신호임.
<br>

레이저를 쏜다 = 앞에 쌓여진 막대기 개수 만큼 조각이 떨어져 나감
<br>

막대기를 닫는다 = 닫는 순간 막대기 한개는 이제 더이상 관여를 하지 않는다는 소리이므로 쌓여져 있는 ( 여는 괄호 하나 없애고, 막대기 조각은 +1
<br>

주어진 규칙만 입력에서 지켜주면 주어진 문자열 하나씩 파싱하면 예외없이 막대기 조각 개수 계산 가능
<br>

<h2> [필요한 데이터] </h2>
<br>
1. 직전 데이터가 무엇인지 체크할 char형 변수 하나<br>
2. 맨나중 인덱스처리 할 필요 없는 스택형 자료구조 한개(push(), pop()만 제대로 되면 됨)<br>
3. int형 정답 변수<br>

<h2> [필요한 기능] </h2>
1. 파싱해서 가져온 데이터가 ( 여는 괄호면 스택에 저장<br>
2. 파싱해서 가져온 데이터가 ) 닫는 괄호일때 <br>
    2-1. 직전 데이터가 ( 여는 괄호였으면 스택에서 pop한 뒤에 스택의 길이만큼 정답에 더함<br>
    2-2. 직전 데이터가 ) 닫는 괄호였으면 스택에서 pop한 뒤에 1만큼 정답에 더함<br>