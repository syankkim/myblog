---
title: ↔️ Linked List 구현 - Double Linked
tags: ['linked_list']
categories: [☁️ Algorithm]
thumbnail: ''
permalink: ''
status: ''
date: 2021-08-10 09:27:23
---

Linked List with Python
이중 연결 리스트를 구현하여, 특정 값을 추가해본다.
<!-- excerpt -->
<!-- toc -->

# Doubley linked list
- 이중 연결 리스트
- 양방향 연결로, 노드 탐색이 양방향으로 가능하다.

> 기본적으로 만들었던 링크드 리스트는 next 값만 존재했지만, Doubly linked list 에서는 prev를 추가하여 해당 Node의 이전 값도 연결해준다.

## prev를 추가한 linked list
```python
class Node: 
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next
    
class NodeMgt:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head
    
    # 노드 추가
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            # new 라는 노드가 추가 되면 prev, next의 노드와 모두 연결해주어야 한다.
            new = Node(val)
            node.next = new
            new.prev = node
            self.tail = new
    
    # 전체 리스트 출력
    def desc(self):
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next
```

<br>

* 0 - 10 까지의 수를 저장한 링크드 리스트를 생성한다.

<img width="744" alt="스크린샷 2021-08-11 오후 6 00 05" src="https://user-images.githubusercontent.com/28856435/129001021-e7a258eb-7c7a-4fec-9455-64a2c5889e72.png">

<br>


## 특정 값을 갖는 노드 찾기 from head? tail?
- prev, 노드의 이전값이 존재하기 때문에 tail, 리스트의 끝에서부터 탐색이 가능하다.
- head, 노드의 처음과 tail, 끝에서 특정 값을 갖는 노드을 찾는 함수를 추가 구현한다.

```python
    # 리스트의 처음부터 탐색
   def sch_from_head(self, val):
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.val == val:
                return node
            else:
                node = node.next
        return False
    
    # 리스트의 끝 부분부터 탐색
    def sch_from_tail(self, val):
        if self.tail == None:
            return False
        node = self.tail
        while node.val!=val:
            node = node.prev
        if node == None:
            return False
        return node
```

<br>

* 특정 값을 갖는 노드를 탐색한다. 찾는 수가 없다면 False를 리턴한다.

<img width="909" alt="스크린샷 2021-08-11 오후 6 10 33" src="https://user-images.githubusercontent.com/28856435/129002492-da7c1a19-2d33-4391-8cac-cc504812ffaf.png">


## 원하는 위치에 값을 추가
- 위에서 구현했던 특정 값을 갖는 노드 위치를 찾는다.
- 그 노드의 이전에 추가하려는 값을 넣는다.

```python
   def insert_before(self, val, targetVal):
        if self.head == None:
            self.head = Node(val)
            return True
        else:
            node = self.tail
            while node.val != targetVal:
                # tail 부터 탐색한다면 다음 탐색할 값은 node.prev
                node = node.prev
            if node == None:
                return False
            # 위치를 찾고 나면 추가하려는 값으로 new node를 생성한다.
            new = Node(val)
            # node 끼리 연결
            node_prev = node.prev
            node_prev.next = new
            new.next = node
            node.prev = new
            return True
```

<br>

* 5라는 값의 위치 이전에 224 값을 넣어본다.

<img width="810" alt="스크린샷 2021-08-11 오후 6 19 38" src="https://user-images.githubusercontent.com/28856435/129003843-51628435-aa75-4af6-9669-aaf8fcd5898e.png">

<br>

## 전체 코드

```python
class Node: 
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next
    
class NodeMgt:
    
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head
    
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(val)
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self):
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next
    
    def sch_from_head(self, val):
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.val == val:
                return node
            else:
                node = node.next
        return False
    
    def sch_from_tail(self, val):
        if self.tail == None:
            return False
        node = self.tail
        while node.val!=val:
            node = node.prev
        if node == None:
            return False
        return node
                
                
    def insert_before(self, val, targetVal):
        if self.head == None:
            self.head = Node(val)
            return True
        else:
            node = self.tail
            while node.val != targetVal:
                node = node.prev
            if node == None:
                return False
            new = Node(val)
            node_prev = node.prev
            node_prev.next = new
            new.next = node
            node.prev = new
            return True
```