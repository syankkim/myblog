---
title: CODING TEST with Python
tags: ['python','codingtest']
categories: [☁️ coding test]
thumbnail: ''
permalink: ''
date: 2020-04-22 16:03:14
---

📜 코딩테스트 with Python
Q. 동전
`백준` `알고리즘`
<!-- excerpt -->
<!-- toc -->

---
<br/>


## [문제] 
> Q. 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

## [입력]

```
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
```

## [예제 입력]

```
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
```

## [예제 출력]
```
> 6
```

## [문제 답변]

```python
def coin(priceArr):
    global price

    priceArr.sort(reverse=True)

    total = 0
    for i in priceArr:
        if (price // i) > 0:
            total+= price // i
            price -= (price // i)*i
            if price==0:
                break
    return total



if __name__ ==  '__main__':
    arrLen, price= map(int, input().split())
    priceArr = []
    for i in range(arrLen):
        priceArr.append(int(input()))

    print(coin(priceArr))
```