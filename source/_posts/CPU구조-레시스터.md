---
title: CPU구조_레지스터
tags: ['computer_science']
categories: [☁️ TIL]
thumbnail: ''
permalink: ''
status: ''
date: 2021-06-03 00:35:59
---

CPU 구성과 디자인 
`` ``
<!-- excerpt -->
<!-- toc -->

---

# CPU 구성요소

> 중앙처리장치 = CPU(Central Processing Unit)
>- 레지스터 세트 (Register set) : 명령어를 실행시 필요한 데이터를 보관
>- 산술논리장치 (ALU; Arithmetic Logic Unit) : 명령어를 실행하기 위한 `마이크로 연산` 수행
>  - 마이크로 연산 종류- shift, count, clear, load
>- 제어장치 (Contol Unit) : RS 간의 정보전송 감시, ALU에 수행할 동작 지시. ID(명령어해독기) 로부터 보내진 신호를 기준으로 명령어 실행

## 각 레지스터들의 기능

- `MAR` Memory Address Register : 메모리의 `상태`
- `MBR` Memory Buffer Register : 메모리 `임시저장공간`
- `IR` Instruction Register 명령어 레지스터 : 계수기가 지정하는 주소에 기억된 `명령어를 해독`하기 위해 `임시 기억`
  - `ID` Instruction decoder 명령어 해독기: IR에 들어있는 명령코드의 해석
- `PC` (Program Counter) 프로그램 계수기 : `다음 수행될 명령어`가 들어있는 주소(주기억장치)를 기억.
- `SR` Status Register 상태레지스터: CPU의 상태를 나타내는 특수목적의 레지스터. flag 정보를 저장한다.
  - 연산결과 상태
  - 0(Z; Zero), 부호(S; sign), 오버플로우(V; overflow), 캐리(C; carry), 인터럽트(I; interrupt)
- `WR` Work Register 작업레지스터: `산술논리연산`을 실행할 수 있게 자료 및 결과 저장. (GPR 은 ALU를 사용하지 않는다.)
- `GR` General Purpose Register 범용 레지스터 : 작업 레지스터에서 `데이터가 용이하게 처리`되도록 임시자료 저장

__ADD 명령의 실행예__

|seq|stage|flow|function|
|----|----|----|---------|
|1 |FETCH| MAR <- PC | 다음 실행할 명령어의 주소를 `MAR`로 이동|
|2 |FETCH| MBR <- 기억장치[MAR] | MAR 이 지정하는 주소의 내용을 `MSR`로 이동|
|3 |FETCH| IR <- MBR | MBR의 내용을 `IR 명령어 레지스터`로 이동|
|||_<어떤 명령인가 ?>_||
|4| EXECUTE| MAR <- IR[OPRD] | 명령어 레지스터의 주소 부분을 `MAR`로 이동|
|5| EXECUTE| MBR <- 기억장치[MAR] | ADD 할 내용을 `MBR`로 이동|
|6| EXECUTE| WR <- GR[IR] | IR에서 지정하는 GR의 내용을 `WR`로 이동|
|7| EXECUTE| WR <- WR + MBR | `ADD 작업`: data(WR) + data(MBR) |
|8| EXECUTE| GR[IR] <- WR | WR의 결과를 `GR`로 이동|
|9| EXECUTE| PC <- PC+1 | 다음 명령어 수행 위해 `PC값 증가`|

## CPU 내부 구조

> 명령어 구성 및 실행
  - 레지스터 간의 전송문으로 나타나는 컴퓨터의 각 연산이 어떻게 동작하는가?
  - __컴퓨터의 구조__: 내부 레지스터, 타이밍, 제어구조 명령어 집합에 의해 정의

### 레지스터 전송 언어
- `마이크로 연산` : 레지스터에 저장된 데이터 조작을 위해 실해되는 동작
- 하나의 `Clock Pulse` 클럭 펄스 내에서 실행.
  - shift, count, clear, road etc.

### 레지스터 전송

- 레지스터 전송의 기본기호

<img width="473" alt="레지스터_전송_기호" src="https://user-images.githubusercontent.com/28856435/120518845-f7bde100-c40c-11eb-9643-9e9cac53d0dc.PNG">

<br>

- R1 -> R2 : 치환연산자를 이용한 레지스터간 정보 전송
- _P: R1 -> R2_
  - `if(P=1) then(R1->R2)`
  - `소스`레지스터로부터 `목적`레지스터까지의 연결.
  - 목적 레지스터애는 조건부 처리 가능한 `병렬로드` 기능이 있어야한다.

> 레지스터 전송을 나타내는 각 문장들은 그 전송을 수행하는 `하드웨어가 구성되어 있음`을 의미한다.


### CPU 디자인
- 다양한 `디바이스들 간` 상호 연결
  - `직접연결`: 연결 복잡도가 장치수의 `제곱`에 비례
  - `버스연결`
    - `공용선`에 의한 연결 -> MUX (멀티플렉서) 를 이용한다.
    - `디코더` decoder 이용 -> 코드화된 데이터로부터 정보를 찾아내는 논리회로
    - 가성비가 높다.
    - 관리를 위한 다양한 방식이 존재한다.
- 자료구조
  - 스택(stack): 주 함수에서 `서브루틴`을 호출할 경우(콜스택)
  - 큐(queue): 버퍼(buffer) 등과 같이 `순차적 처리`를 요하는 자료의 대기시에 활용
  - 데크(deque): 스택과 큐의 동작을 동시에 가능. (*이건 잘 모르겠다..)
    - 입력제한 데크: scroll
    - 출력제한 데크: shelf