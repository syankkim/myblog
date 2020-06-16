---
title: CODING TEST {"싱글숫자 구하기"} with Java
tags: ['java','codingtest']
categories: [☁️ coding test]
thumbnail: ''
permalink: ''
date: 2020-04-22 16:03:14
---

📜 매일매일 코딩테스트 with 자바
1) 배열안에는 커플숫자 여러개와 싱글숫자 하나만 존재한다. 싱글숫자 구하기.
2) 여기서 다시 깨닫는 기초. JAVA 기본형(Primitive type) vs 참조형(Reference type)
<!-- excerpt -->
<!-- toc -->

---
<br/>

## [문제] 싱글숫자 구하기
> Q. Given a non-empty array of integers, every element appears twice except for one. Find that single one.

__문제.__
다들 아시겠지만, 해석해보자면 배열 안에 자기 짝이 없는 Single N 을 리턴하는 문제이다.
누구나 생각할 수 있는 이중 for 문을 사용해 풀었는데
이상하게도 아래 주석된 부분의 `if(list.get(i)==list.get(j))` 이 부분에서 비교를 잘 못하는 오류가 발생했다.
두 자리 수 까지는 비교연산이 잘 되는데 왠지 세자리 수 부터 안되는 듯 보였다.
혹시 하여 세자리 수에서 십의자리를 늘려가며 까지 연산 테스트를 했는데 130부터 비교되지 않는것..
 
__해결.__
해결책은 가장 근본적인 데에 있었다.
리스트의 Generics 가 Integer 로 되어 있었는데 `==` 연산자를 써서 비교했던것 ..
자세한 설명은 아래에서 더 하겠다.

```java
public int singleNumber(int[] nums) {
        int single = 0;
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());

        for(int i=0; i<list.size(); i++){
            boolean isSingle = true;
            for(int j=i+1; j<list.size(); j++){
                // if(list.get(i)==list.get(j)){        ----> ERROR
                if(list.get(i).equals(list.get(j))){
                    isSingle = false;
                    list.remove(list.get(i));
                    j--;
                    list.remove(list.get(j));
                    i--;
                    break;
                }
            }
            if(isSingle){
                single = list.get(i);
                break;
            }
        }
        return single;
    }
```
<br/>

## JAVA 기본형(Primitive type) vs 참조형(Reference type)

__기본형 (Primitive type)__
o 연산자를 `값` 으로 비교할 수 있다. 즉, 산술연산이 가능하다.
o 초기값을 필요로 한다.
o 종류
  `void`, `boolean`, `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`, `void`

__참조형의 종류에는 아래와 같은 타입들이 존재한다.__
o 연산자가 객체의 `주소값` 으로 비교된다. 산술연산이 불가하다.
o 초기값을 NULL 로 지정할 수 있다.
o 종류
  `Void`, `Boolean`, `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`, `Character`