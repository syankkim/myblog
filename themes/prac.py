



# Stack 은 데이터의 삽입과 삭제가 저장소의 맨 뒷부분에서만 일어나는 자료구조이다.
# 장점으로는 한번 참조된 곳은 다시 참조될 확률이 높다는 점.
# 단점으로는 데이터를 탐색하기가 어렵다는 점이다.
# 사용 : 함수의 콜스택, 문자열을 역순으로 출력, 연산자 후위표기법

# 필수구현
# push (return None) : 맨 위에 값추가
# pop (return data) : 가장 최근 값을 제거

# peak (data, -1) : 변형없이 맨 위의 값을 출력
# isEmpty (boolean) : 스택이 비어있는지 확인



class StackByArray(list):
    def __init__(self, max_length = 50):
        self.stack = []
        # self.top = -1
        self.max_length = max_length
    
    def push(self, data):
        self.stack.append(data)

    def pop(self, data):
        if self.isEmpty():
            raise Exception('STACK EMPTY ERROR!')
            return -1
        self.stack.pop()

    def isEmpty():
        if len(selt.stack)==0:
            return True
        return False
    
    def peak(self):
        #-1은 역순으로 조회
        return self.stack[-1]

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