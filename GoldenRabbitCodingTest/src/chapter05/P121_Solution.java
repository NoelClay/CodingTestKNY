package chapter05;

/*
나눠생각하기
1. 행렬의 곱셈 공식 구현 : 가로곱하기 세로 각각 다더한거
2. 다차원 배열을 어떻게 저장할지 : 무조건 2차원 행렬이래.

예외 고려하기
곱할 수 있는 배열만 주어지니 신경꺼

입력값 고려하기
100 x 100 행렬 끼리의 곱셉 연산. n=100 n^3도 가능

의사코드
1. 행렬의 곱셈공식을 구현하라1 : 뭐끼리 곱할지
2. 곱셈공식2 : 뭐끼리 더할지
3. 곱셈공식3 : 그 결과를 어디에 저장할지

1. 먼저 arr2의 열의 개수가 열을 결정
arr1의 행의 개수가 총 더해야하는 양을 결정

2x3 x 3x2 = 2x2
3x2 x 2x2 = 3x2

1행 1열끼리 곱하고 더해, 1행 2열끼리 곱하고 더해 2행 1열끼리 곱하고 더해 2행 2열끼리 곱하고 더해 3행 1열끼리 곱하고 더해 3행2열끼리 곱하고 더해

1행 1열끼리 1열만큼 1행만큼 곱하고 더해, 1행 2열끼리 1열만큼 2행만큼 곱하고 더해, 1행 3열끼리 1열만큼 3행만큼 곱합고 더해
2행 1열끼리 2열만큼 1행만큼 곱하고 더해, 2행 2열끼리 2열만큼 2행만큼 곱하고 더해, 2행 3열끼리 2열만큼 3행만큼 곱합고 더해
*/


class P121_Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        //2x3 x 3x2 = 2x2 | 3x2 x 2x2 = 3x2
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        
        //1. 행렬의 곱셈공식을 구현하라1 : 뭐끼리 곱할지
//1행 1열끼리 1열만큼 1행만큼 곱하고 더해, 1행 2열끼리 1열만큼 2행만큼 곱하고 더해, 1행 3열끼리 1열만큼 3행만큼 곱합고 더해
//2행 1열끼리 2열만큼 1행만큼 곱하고 더해, 2행 2열끼리 2열만큼 2행만큼 곱하고 더해, 2행 3열끼리 2열만큼 3행만큼 곱합고 더해
        
        for(int i=0; i<arr1.length; i++){ //arr1 행의 개수
            for(int j=0; j<arr2[0].length; j++){//arr2 열의 개수
                for(int k=0; k<arr2.length; k++) {// arr1 열의 개수 == arr2 행의 개수 이게 성립을 안하면 애초에 암되는 녀석
                    answer[i][j] += arr1[i][k] * arr2[k][j];
                    //n행 m열의 값은 arr1 n행의의 모든값과 arr2 m열의 모든 값을 끼리끼리 곱하여 더한것. <- 이게 공식 구현
                }
            } 
        }
        
        return answer;
    }
}