---
title: CODING TEST with Java
tags: []
categories: [☁️ Algorithm]
thumbnail: ''
permalink: ''
date: 2020-04-14 00:05:31
---

📜 매일매일 코딩테스트 with 자바
1) 최대공약수와 최소공배수를 반환하는 함수 구현
2) 행렬의 덧셈을 반환하는 함수구현
<!-- excerpt -->
<!-- toc -->

---

## 최대공약수와 최소공배수

```java
// =====================================================================================================
// 문제 설명
// 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수,
// solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
// 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

// 제한 사항
// 두 수는 1이상 1000000이하의 자연수입니다.
// =====================================================================================================

public int[] solution(int n, int m) {
    int[] answer = new int[2];
    int min = 1000000; int max=0;
    
    int fstnum =0;
    int sndnum = 0;
    List<Integer> fstnumArr = new ArrayList<>();
    int multi = 1;
    if(n<m){
        fstnum= n;
        sndnum = m;
    }else{ fstnum =m; sndnum=n; }
    
    System.out.println("fstnum : "+fstnum);
    for(int i=1; i<=fstnum; i++){
        System.out.println(String.format("i= %d/ fstnum 나머지= %d", i, fstnum%i));
        if(fstnum%i==0) {
            fstnumArr.add(i);
        }
    }
    System.out.println("fstnumArr : "+ fstnumArr);
    
    for(int i= fstnumArr.size()-1; i>=0; i--){
        if(sndnum%fstnumArr.get(i)==0){
            if(min>fstnumArr.get(i)){
                min = fstnumArr.get(i);
            }
            multi *= fstnumArr.get(i);
        }
    }
    System.out.println("최대 공약수 : " + min);
    System.out.println("multi : " + multi);
    
    // 최대공배수는 각 2개 숫자를 (최소공약수들의 곱의 값으로 나눈 수)* (최소공약수들의 곱)
    max = (n/multi) * (m/multi) * multi;
    System.out.println("최소 공배수 : "+ max);
    
    return answer;
}

public static void main(String args[]) throws Exception{
    int[] answer = new Solution().solution(3, 12);
}
```


## 행렬의 덧셈

```java   
    // =====================================================================================================
    // 문제 설명
    // 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
    // 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
    // =====================================================================================================
public int[][] solution2(int[][] arr1, int[][] arr2) {
    int len = arr1.length;
    int[][] answer =  new int[len][arr1[0].length];
    
    for(int i=0; i<2; i++){
        for(int j=0; j<arr1[i].length; j++){
            answer[i][j] = arr1[i][j] + arr2[i][j];
            System.out.println("answer : "+ Arrays.deepToString(answer));
            //1차원 배열에서는 toString 가능, 2차원 이상에서는 Arrays.deepToString(answer) 
        }
    }
    
    return answer;
}
public static void main(String args[]) throws Exception{
    // int[] answer = new Solution().solution(3, 12);
    int[][] arr1 = {{1},{3}};
    int[][] arr2 = {{2},{3}};
    int[][] answer = new Solution().solution2(arr1, arr2);
}

```