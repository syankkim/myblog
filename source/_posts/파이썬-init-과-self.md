---
title: 파이썬의 __init__ 과 self
tags: []
img: <img width="100" src="https://user-images.githubusercontent.com/28856435/95408953-9c118580-095b-11eb-8dfb-745bbf437ffd.png">
categories: [☁️ Python]
thumbnail: ''
permalink: ''
date: 2020-10-08 11:38:09
---

자주쓰는 \_\_init\_\_ 그리고 self 무엇을 의미하는 것일까?
`생성자` `인스턴스`
<!-- excerpt -->
<!-- toc -->


---

## 생성자 __init__

 **\_\_init\_\_** : 파이썬의 생성자를 나타낸다.
클래스 Person() 를 호출하면 객체가 생성되고 `__init__` 메소드에 첫 번째 매개변수로 전달된다.
추가 매개변수 또한 가능하다.

**self** : 객체 자체의 인스턴스를 의미한다.
파이썬은 다른 객체지향 언어와는 달리 (대부분 메소드에 숨겨진 매개변수로 전달) `self` 와 같이 명시적으로 선언해야 한다.

---

<br>

## 클래스 Person 예시
```python
class Person:
    def __init__(self, name, age):
        self.n_name= name
        self.n_age= age

    def getName(self):
        print(self.n_name)

    def addAge(self, num):
        self.n_age += num
        print(self.n_age)


p = Person('Jenny', 12)
p.getName()
p.addAge(5)
```

**결과**
>Jenny
17

**# Line2** : self 가 포함되어 있지만 실제로 `name` 과 `age` 두가지 매개변수만 전달한다.
**# Line9** : self 의 `n_age` 값에 `addAge` 에 매개변수로 전달되는 숫자를 더해 출력한다.




