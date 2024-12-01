package chapter05;
//https://school.programmers.co.kr/learn/courses/30/lessons/42840
/*
문제 나눠 생각하기
1. 각 수포자들의 순열을 담기
2. 문제와 수포자들 순열로 비교하여 정답을 카운팅하기
3. 카운팅 했을때 가장 높은 숫자들을 뽑아서 정렬

입력값 분석
10000 문제. 따라서 nlogn 밖에 안됨

데이터 흐름 분석
순서 부터 값까지 전부 일치해야하므로 배열이 적절해 보임.
*/

/*
의사 코드
1. 수포자들의 순열을 만들자 12345 / 21232425/ 3311224455
2. 문제를 받아와서 전체 탐색 돌리는 동안 수포자들도 하나씩 탐색 인덱스가 증가해야해. 
3. 일치하면 카운트 증가
4. 가장 높은 카운트 녀석 순서대로 결과값에 담기
*/
import java.util.*;
// import java.stream.*;

class P116_Solution {
    public int[] solution(int[] answers) {
        //1. 수포자들의 순열을 만들자 12345 / 21232425/ 3311224455
        int[] a = {1,2,3,4,5};
        int[] b = {2,1,2,3,2,4,2,5};
        int[] c = {3,3,1,1,2,2,4,4,5,5};
        //2. 문제를 받아와서 전체 탐색 돌리는 동안 수포자들도 하나씩 탐색 인덱스가 증가해야해. 
        int acnt=0; int bcnt=0; int ccnt = 0;
        
        for(int i=0; i<answers.length ; i++){
            //3. 일치하면 카운트 증가
            if(answers[i] == a[i%a.length]) {acnt++;}
            if(answers[i] == b[i%b.length]) {bcnt++;}
            if(answers[i] == c[i%c.length]) {ccnt++;}
        }
        //4. 가장 높은 카운트 녀석 순서대로 결과값에 담기
        int max = -987654321;
        max = max < acnt ? acnt : max;
        max = max < bcnt ? bcnt : max;
        max = max < ccnt ? ccnt : max;
        List<Integer> res = new ArrayList<>();
        if(acnt == max) res.add(res.size(), 1);
        if(bcnt == max) res.add(res.size(), 2);
        if(ccnt == max) res.add(res.size(), 3);
        
        int[] result = res.stream().mapToInt(Integer::intValue).toArray();
        
        return result;
        
    }
}