package chapter05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
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
문제 분석
이런 문제를 보면 직접 코드를 구현하고 싶은 마음이 들 수도 있지만 자바에서는 미리 구현된 좋은
메서드들이 많으므로 그런 메서드들도 활용해보면 좋습니다. 이 문제가 딱 그렇게 풀었을 때 좋은
문제입니다. 코드를 살펴봅시다.
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

public class P109_ArrayControl_Answer {
    public static void main(String[] args) throws IOException{
        //1. 입력을 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // int[] intArray = new int[1000]; -> 원본도 가변으로
        int[] arr = new int[6];
        StringTokenizer st = new StringTokenizer(br.readLine(), ",");
        int i = 0;
        while(st.hasMoreTokens()){
            arr[i] = (Integer.parseInt(st.nextToken()));
            i++;
        }
        //1. 중복 제거
        Integer[] result = Arrays.stream(arr).boxed().distinct().toArray(Integer[] :: new);
        Arrays.sort(result, Collections.reverseOrder()); // 2 내림차순 정렬
        // int형 배열로 변경 후 반환
        System.out.println(Arrays.stream(result).mapToInt(Integer::intValue).toArray());
        int[] arr2 = Arrays.stream(result).mapToInt(Integer::intValue).toArray();
        for(int m : arr2){
            System.out.println(m);
        }
        return;
    }
}
