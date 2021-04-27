---
title: CODING TEST  {SockMerchant} with Python
tags: ['python','codingtest']
categories: [☁️ Algorithm]
thumbnail: ''
permalink: ''
date: 2020-06-15 10:03:11
---

📜 코딩테스트 with Python
Q. SockMerchant
`HackerRank` `알고리즘`
<!-- excerpt -->
<!-- toc -->

---
<br/>


## [문제] SockMerchant
> Q. Complete the sockMerchant function below.
For example, there are  socks with colors . There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is.

## [문제 답변]

```python
import sockMerchant

def sockMerchant(n, ar):
    if len(ar) !=n:
        print('리스트 길이를 확인해주세요')
        return 0

    ar_count = dict()
    cnt =0
    for sock in ar:
        if sock not in ar_count.keys():
            ar_count[sock] = 1
        else:
            if(ar_count[sock]<2):
                ar_count[sock] += 1
                cnt +=1
            else:
                # del(ar_count[sock]) #같은 key 가 있을때 마지막 값으로 덮어씌워지므로 할필요 없음
                ar_count[sock] = 1

            print('ar_dic : {0} / cnt : {1}'.format(ar_count, cnt))
    return cnt


#  __name__에는 '__main__' 이 들어감. 시작점(entry point) 이다.
if __name__ == '__main__':
    n = int(input('리스트 길이 입력: '))
    ar = list(map(int, input('리스트 원소 입력: ').rstrip().split()))
    print(sockMerchant(n, ar))
```