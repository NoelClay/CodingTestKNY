package chapter05;

/*
문제 분석 나눠 생각하기
1 배열에서 두 수를 선택하는 모든 경우의 수를 구합니다.
2 과정 1에서 구한 수를 새로운 배열에 저장하고 중복값을 제거합니다.
3 배열을 오름차순으로 정렬하고 반환합니다.
*/
import java.util.*;

class P114_Solution_Answer {
    public int[] solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<>(); // 1 중복값 제거를 위한 해시셋 생성
        // 2 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
        for (int i = 0; i < numbers. length - 1; i++) {
            for (int j = i + 1; j < numbers. length; j++) {
            // 3 두 수를 더한 결과를 해시셋에 추가
            set.add(numbers[i] + numbers[j]);
        }

        }
        //4 해시셋의 값을 오름차순 정렬하고 int[] 형태의 배열로 변환하여 반환
        return set.stream().sorted().mapToInt(Integer :: intValue).toArray();
    }
}