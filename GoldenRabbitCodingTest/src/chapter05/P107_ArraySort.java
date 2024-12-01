package chapter05;

import java.util.Arrays;

/*
 * 문제 01 배열 정렬하기★
저자 권장 시간_ 10분 | 권장 시간 복잡도_ O(NlogN) | 출제_ 저자 출제
JEFURL https://github.com/retrogemHK/codingtest_java/blob/main/solution/01.java

저자 선생님이 직접 만든 개념 확인 문제입니다. 깃허브 코드를 확인해주세요.

정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요.

제약 조건

• 정수 배열의 길이는 2 이상 10^5 이하입니다.
• 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하입니다.

입출력의 예

입력
[1,-5, 2,4, 3]
[2, 1, 1, 3, 2, 5, 4]
[6,1,7]

출력
[-5, 1, 2, 3, 4]
[1,1, 2, 2, 3, 4,5]
[1, 6, 7]
 * 
 */

public class P107_ArraySort {

    public static void main(String[] args) {
        int[] arr = { 1, -5, 2, 4, 3 };
        System.out.println(Arrays.toString(solution(arr)));
    }

    public static int[] solution(int[] arr) {
        Arrays.sort(arr);
        return arr;
    }
}
