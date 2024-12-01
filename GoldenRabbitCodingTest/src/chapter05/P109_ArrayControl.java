package chapter05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/*
 * 문제 02 배열 제어하기*★

저자 권장 시간_ 10분 | 권장 시간 복잡도_O(NlogN) | 출제_ 저자 출제

URL https://github.com/retrogemHK/codingtest_java/blob/main/solution/02.java

정수 배열을 하나 받습니다. 배열의 중복값을 제거하고 배일 데이터를 내림차순으로 정렬해서 반
환하는 solution() 함수를 구현하세요.

제약 조건

• 배열 길이는 2 이상 1,000 이하입니다.
• 각 배열의 데이터 값은 -100,000 이상 100,000 이하입니다.


입출력의 예

입력

[4, 2, 2, 1, 3, 4]
[2, 1, 1, 3, 2, 5, 4]

출력
[4, 3, 2, 1]
[5, 4, 3, 2, 1]
 */

/*
문제 분석 연습
* 문제 자르기: 1. 배열 선정렬 2. N번 탐색하며 int pre 와 int cur 를 비교하여 같으면 삭제하기 -> 실제 삭제는 연산 횟수가 증가하므로
비어있는 ArrayList 만들고 put()을 생략하기
3. 만들어진거 출력

제약 사항 파악: 첫번째 값은 미리 저장하고 int i=1부터 탐색해도 괜춘. 그럴때 사이즈가 1이라면 그냥 리턴때리고 사이즈가2라면 한번은 검사할 필요 있음.

그리디한가: X

데이터 흐름: 원본저장은 Array, 출력으로 만드는건 ArrayList
*/

/*
 * 의사 코드
 * 1. 입력을 받습니다.
 * 2. 정렬을 합니다.
 * 3. 중복을 제거하여 담을 공간을 생성합니다.
 * 4. 정렬된 원본을 이용하여 하나씩 담습니다.
 * 5. 사이즈가 1이라면 그냥 바로 반환하고요. 2 이상이라면은 일단 맨첫번째 녀석은 비교용 변수로 저장하고 2번째부터 탐색해도 됩니다.
 * 6. 이렇게 할려면 원본도 가변이어야 되는군요.
 */

public class P109_ArrayControl {

    public static void main(String[] args) throws IOException{
        //1. 입력을 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // int[] intArray = new int[1000]; -> 원본도 가변으로
        ArrayList<Integer> originList = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine(), ",");
        while(st.hasMoreTokens()){
            originList.add(Integer.parseInt(st.nextToken()));
        }

        //2. 정렬을 합니다.
        // Arrays.sort(intArray); -> ArrayList는 Collections를 사용합니다. -> 내림차순으로 하기 위해 reverseOrder
        Collections.sort(originList, Collections.reverseOrder());
        System.out.println(originList);

        //3. 중복을 제거하여 담을 공간을 생성합니다.
        ArrayList<Integer> answerList = new ArrayList<>();
        System.out.println(answerList);

        /*
        * 4. 정렬된 원본을 이용하여 하나씩 담습니다.
        * 5. 사이즈가 1이라면 그냥 바로 반환하고요. 2 이상이라면은 일단 맨첫번째 녀석은 비교용 변수로 저장하고 2번째부터 탐색해도 됩니다.
        */
        if(originList.size() < 2 ){
            System.out.println(originList);
            return;
        }
        else{
            int pre = originList.get(0);
            answerList.add(answerList.size(),pre);
            for(int j=1; j<originList.size(); j++){
                int cur = originList.get(j);
                if(pre == cur) continue;
                else{
                    answerList.add(answerList.size(),cur);
                    pre = cur;
                }
            }
            System.out.println(answerList);
            return;
        }

    }
}
