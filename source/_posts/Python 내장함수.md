---
title: Python 내장함수
tags: ["python",'python 이진연산','rJust']
categories: [☁️ Python]
thumbnail: ''
permalink: ''
date: 2020-04-22 16:10:28
---

1) 알고리즘 문제 예제를 통해 zip 내장 함수, 이진연산, rJust함수 알아보기
2) (번외) 숫자를 한 자리수로 잘라 각각 리스트에 담기
<!-- excerpt -->
<!-- toc -->


### zip 내장 함수, 이진연산

#### zip() 은 길이가 같은 자료형을 묶어준다.
__예를 들면, 다음과 같다.__
```python
zip([3,4,5], [1,2,3]) => (3,1),(4,2),(5,3)
zip('ABC', [1,2,3])   => (A,1), (B,2), (C,3)
```

#### (1)두 배열을 받아, n 을 받아 (2)binary 연산후 (3)자릿수만큼 빈곳은 "#"을 채운다.


```python
def ziplist(n):
    arr1 =[3,4,5]
    arr2 = [1,2,3]
    n = 5

    for num1, num2 in zip(arr1, arr2):
        print(num1, num2)
        tmp = bin(num1|num2)[2:] # 여기서 파이썬의만의 '문자열 슬라이싱' 아래에서 개념확인
        print('이진연산 후 '+tmp)

        tmp = tmp.rjust(n, '#')
        print('결과 '+tmp)
    return tmp
```
__출력결과__
```
(3, 1)
이진연산 후 11
결과 ###11
(4, 2)
이진연산 후 110
결과 ##110
(5, 3)
이진연산 후 111
결과 ##111
```


### python 문자열 슬라이싱
```python
>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
```

### rJust 함수 : N자릿수로 리턴(빈곳은"#" 으로 채우기)
```python
def rjst(n):
    list= ['1','2','3']
    tostring = "".join(list)
    if n > len(tostring):
        tostring = tostring.rjust(n, '#')
    print("tostring : " + tostring)
    # tostring : #######123

 rjst(10)
```

### (번외) 숫자를 한 자리수로 잘라 각각 리스트에 담기
```python
def numToList(number):
    n = 234
    list = [ int(i) for i in str(n)]
    print(list)
    return list
    # list= [2, 3, 4]
```