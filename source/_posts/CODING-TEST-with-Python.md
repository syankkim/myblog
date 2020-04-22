---
title: CODING TEST with Python
tags: ['python']
categories: ['coding test']
thumbnail: ''
permalink: ''
status: ''
date: 2020-04-12 23:51:24
---

📜 매일매일 코딩테스트 with 파이썬
1) 정수N 자릿수의 합
2) X부터 X만큼 증가, N개를 저장하는 리스트
3) 배열내 갹 문자열의 인덱스 n번째 글자기준 정렬
<!-- excerpt -->
<!-- toc -->

## Return  n 정수를 받아서 각자리수의 합

```python
#========================================================
## 코딩 테스트
#========================================================
# 문제 설명
# n 정수를 받아서 각자리수의 합을 구함 

def substring(n):
    sum = 0
    num = str(n)
    for i in range(0,len(num)):
        print("i = "+str(i))

        cut= num[i:i+1]
        print("num {0}=> cut {1}".format(num, cut))
        sum += cut
        print(sum)
    return sum

def solution(n):
    answer = substring(n)
    return answer

print("result : " + str(solution(123)))
```

## Return x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트

```python
#========================================================
## 코딩 테스트
#========================================================
# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 
# 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.

def solution2(x, n):
    answer= []
    for i in range(1, n+1):
        answer.append(x*i)
        print("answer : {0}".format(answer))
solution2(2, 5)
```

## 각 문자열의 인덱스 n번째 글자기준 정렬

```python
#========================================================
## 코딩 테스트
#========================================================
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 
# 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 
# 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

# 입출력 예 1
# sun, bed, car의 1번째 인덱스 값은 각각 u, e, a 입니다. 이를 기준으로 strings를 정렬하면 [car, bed, sun] 입니다.

# 입출력 예 2
# abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다. 따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다. 
# abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.

def makeArr(strings, n):
    answer = []
    tupList = []
    for i in strings:
        tmp = i[n:n+1]
        tup = (i, tmp)
        tupList.append(tup)
        print(tupList) 
        # 기본 튜플 정렬 
        # key = lambda x : x[0]
        # 1) 1번째 원소 정렬후 0번째 원소로 정렬
        # key = lambda x : (x[1], x[0])
        # 2) 1번째 원소 내림차순 정렬후 0번째 원소로 정렬
        # key = lambda x : (-x[1], x[0])
    tupList.sort(key = lambda x : (x[1],x[0]))
    print("after sort")
    print(tupList)
    return answer
    

stringList = ['abcw', 'abce', 'cdx']
n = 2
makeArr(stringList, n);
```



