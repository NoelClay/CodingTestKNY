package chapter05;
//https://school.programmers.co.kr/learn/courses/30/lessons/42840

import java.util.*;
// import java.stream.*;

class P116_Solution_Answer {
    public int[] solution(int[] answers) {

        // 1 수포자들의 패턴
        int[][] pattern = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        // 2 수포자들의 점수를 저장할 배열
        int[] scores = new int[3];

        // 3 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
        for (int i = 0; i < answers. length; i++) {
            for (int j = 0; j < pattern. length; j++) {
                if (answers[i] == pattern[j][i % pattern[j]. length]) {
                    scores[j]++;
                }
            }
        }

        //4 가장 높은 점수 저장
        int maxScore = Arrays.stream(scores).max().getAsInt();
        // 5 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < scores. length; i++) {
            if (scores[i] == maxScore) {
                answer.add(i + 1);
            }
        }
        //6 배열로 변환 하는거
        return answer.stream().mapToInt(Integer :: intValue). toArray();
    }
}
/*
1 수포자들의 패턴을 미리 배열에 저장합니다.

2 수포자들의 패턴과 답안을 비교해서 일치하는 개수를 저장하는 배열을 선언했습니다. 이렇게 배열을
생성하게 되면 초깃값은 0입니다.

3 정답과 수포자들의 패턴을 비교해서 각 수포자들의 점수를 구하는 부분입니다. 바깥 반복문은
answers, 안쪽 반복문은 patterns의 데이터를 하나씩 가리킵니다. answer의 각 답안과 수포자
들의 정답을 하나씩 비교하면서 정답이 일치하는 수포자의 경우 score를 1만큼 더합니다. 정답
패턴의 길이가 수포자의 답안 길이보다 긴 경우 정답 패턴의 처음 데이터와 다시 비교할 수 있도록
나머지 연산자를 사용했습니다.
if (answers[i] == pattern[j][i % pattern[j].length])

4 반복문에서 구한 각 수포자들의 점수 중 가장 큰 점수를 찾습니다. 
Arrays.stream(scores).max().getAsInt();

5 가장 큰 점수를 갖는 수포자들을 찾아서 배열에 담아 반환합니다.

6. 배열로 변환 ArrayList -> array
answer.stream().mapToInt(Integer :: intValue). toArray();
 * 
 */