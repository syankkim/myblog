---
title: 링크드리스트 구현-removeNode함수
tags: ['linked_list']
categories: [☁️ Algorithm]
thumbnail: ''
permalink: ''
status: ''
date: 2021-07-20 23:27:23
---

Linked List with Python
특정 노드값을 지워주는 함수를 만들어본다.
<!-- excerpt -->
<!-- toc -->

# Manage Linked Likst

## Remove Node

지난 포스팅에 기본적으로 Linked List 객체를 만들고, 추가하여 출력까지 할 수 있는 `NodeMgt` 클래스를 간단히 구현했었다.
이번에는 이 클래스에서 특정 노드를 `remove` 할 수 있는 함수를 추가적으로 구현해 보았다.
<br>
* 아래 remove 함수를 보면, 총 3가지 경우의 로직으로 분기된다.
  - 1) head 값이 None 일때, 그냥 return
  - 2) head 값이 지우려는 바로 그 값일 때, head의 포인터가 head의 다음값을 바라보게 한다. (그러면 원레 head를 가리키던 값은 리스트 연결성을 잃는다. -지워짐)
  - 3) 마지막 로직은, prev_node(이전노드)와 node(현재노드) 값을 while문을 타기전에 저장한다.
       while 문은 node 값이 지우려는 그 값일 때 빠져나올 수 있다.
       빠져나오게 되면, prev_node 의 next 값은 node (지우려는 값) 값이 아닌, node.next 를 바라보게 한다.
       지우려는 값은 리스트에서 연결성이 끊겨서 지워진다.

```python
def remove(self, val):
        if self.head==None:
            return
        
        if self.head.val==val:
            self.head=self.head.next
            return

        prev_node=self.head
        node=self.head.next
        print('val: %s prev: %s node: %s ' % (val, prev_node.val, node.val))
        while node.val!=val:
            prev_node=prev_node.next
            node=node.next
            print('val: %s prev: %s node: %s ' % (val, prev_node.val, node.val))
            
        prev_node.next=node.next
```

<br>

## Use Function

* 아래와 같이 linkedList 객체를 만들고 함수를 사용하여 특정 Node가 지워지는 것을 확인한다.

<img width="960" alt="스크린샷 2021-07-20 오후 11 47 12" src="https://user-images.githubusercontent.com/28856435/126345349-79de8dec-56a4-4b73-b578-f5fa86f002f6.png">

<br>


* Linked List 구현 전체 소스코드

```python
class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
    
class NodeMgt:
    def __init__(self, val):
        self.head=Node(val)
    
    def add(self, val):
        if self.head==None:
            self.head=Node(val)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(val)

    # >>>> 특정 노드를 지워주는 함수 추가      
    def remove(self, val):
        if self.head==None:
            return
        
        if self.head.val==val:
            self.head=self.head.next
            return

        prev_node=self.head
        node=self.head.next
        print('val: %s prev: %s node: %s ' % (val, prev_node.val, node.val))
        while node.val!=val:
            prev_node=prev_node.next
            node=node.next
            print('val: %s prev: %s node: %s ' % (val, prev_node.val, node.val))
            
        prev_node.next=node.next
    
    def printNode(self):
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next
                
```

<br>

# Today...

_
어느새 2021년의 절반이 훌쩍 넘었다.
시간은 가고 있지만, 그 지나간 시간만큼 나는 얼마나 무엇을 이뤄냈는지 ..?
_
요즘 공부에 신경을 많이 쓰지 못하고 있다. 알고리즘을 어서 습득해야 하는데 말이다 !!
_
최근에 mac mini를 사서 개발하는 재미가 쏠쏠하다.
_
어떤 결실을 위해서는 꾸준함이 답인것 같다.
포기하지 말고 한결같이 노력해야 함이다.

...

