package chapter05;
// https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=java
/*
문제 분석 나눠 생각하기
1. 모든 경우의 수를 다 구하기
2. 중복을 제거하기
3. 오름차순으로 출력하기

문제 분석 제약사항 파악
딱히 특별한 예외는 파악되고 있지 않음

입력값 분석
100이하니까 n^3도 가능하다

데이터 흐름 파악
중복을 제거하는건 배열에도 있어 distinct() or treeset도 방법
정렬을 하는건 sort()가 있어.
*/

/*
의사 코드
1. 입력을 보존한다.
2. 입력을 기반으로 모든 경우의 수를 구한다.
3. 경우의 수에서 중복을 제거한다.
4. 경우의 수에서 오름차순 정렬을 한다.
*/
import java.util.*;
import java.util.stream.*;

class P114_Solution {
    public int[] solution(int[] numbers) {
        
        //1. 입력을 보존한다.
        int[] origin = numbers;
        
        //2. 입력을 기반으로 모드 경우의 수를 구한다.
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=0; i<origin.length; i++){
            for(int j=i+1; j<origin.length; j++){
                result.add(result.size(), origin[i] + origin[j]);
            }
        }
        
        //3. 중복을 제거한다.
        List<Integer> intStreamToList = result.stream().distinct().collect(Collectors.toList());
        
        //4. 정렬한다.
        Collections.sort(intStreamToList);
        
        int[] arr = intStreamToList.stream().mapToInt(Integer::intValue).toArray();
        return arr;

    }
}