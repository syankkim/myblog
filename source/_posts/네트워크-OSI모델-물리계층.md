---
title: 네트워크-OSI모델, 물리계층과 데이터링크계층
tags: ['network', 'osi_7_layer']
categories: [☁️ Network]
thumbnail: ''
permalink: ''
status: ''
date: 2021-06-16 15:17:17
---

OSI모델의 물리계층? 우리가 알던 그 장비.
항상 접하던 Ethernet, 스위치, ARP 프로토콜에 대하여.
`#osi_7_layer` `#tcp_ip` `#csma_cd` `#switch` `#ethernet` `#arp`
<!-- excerpt -->
<!-- toc -->

---

# TCP/IP

> 네트워크 프로토콜의 모음.
`패킷 통신 방식`의 `IP`와
`전송 조절 프로토콜`인 `TCP`로 이루어져 있다.

* __TCP/IP & OSI 7 Layer__

<table>
    <thead>
        <tr>
            <th>TCP/IP</th>
            <th>Service/Protocol</th>
            <th>OSI 7Layer</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>Application</td>
            <td rowspan=3>HTTP, SMTP, DNS</td>
            <td>Application</td>
        </tr>
        <tr>
            <td>Presentaition</td>
        </tr>
        <tr>
            <td>Session</td>
        </tr>
        <tr>
          <td>Transport</td>
          <td>TCP, UDP</td>
          <td>Transport</td>
        </tr>
        <tr>
          <td>Network</td>
          <td>IP, ICMP, OSPF</td>
          <td>Network</td>
        </tr>
        <tr>
          <td rowspan=2>Network Interface</td>
          <td rowspan=2>Ethernet</td>
          <td>Data Link</td>
        </tr>
        <tr>
          <td>Physical</td>
        </tr>
    </tbody>
</table>

<br>

---

# 물리계층
> OSI 7 Layer 1계층의 하드웨어

- 네트워크 장치의 `전기적, 기계적` 속성과 전송하는 수단
- `데이터 링크` 계층 프레임 --> (bit를 Signal 로 인코딩) --> `네트워크 장치`로 전송
- 통신 장치와 커넥터, 인코딩(Bit to Signal), 송수신을 담당하는 회로 등의 요소 포함
- 전송하는 수단인 Signaling(신호)은 전기, 광, 무선 등이 있다.

## 물리계층 장비
- 허브 & 리피터
  - 허프는 전기신호를 증폭하여 포트에 연결된 PC들끼리 통신이 가능
  - 리피터는 현재 거의 쓰이지 않는다. 세기를 더 증폭하여 더 멀리까지 통신이 가능


### 허브 동작방식
> 허브는 `브로드캐스팅` 통신과 `CSMA/CD` 방식을 사용, `Half Duplex` 모드이다.

- 브로드캐스팅 1 : All
- 유니캐스트 1 : 1
- 멀티캐스트 1 : N


### CSMA/CD
> Carrier Sense Multiple Access / Collision Detection

1. Carrier Sensing: 데이터를 보내기 전에 다른 노드에서 데이터를 보내는 중인지 확인
2. Multiple Access: 데이터를 보내는곳이 없으면 전송
3. Collision Detection: 동시간대의 데이터 충돌 후 정지. 일정시간 이후 재동작

### 전송방식
1. Simplex: 단방향 통신으로 수신측은 송신척에 응답 불가
2. Half Duplex: 반이중 전송방식. 무전기.
3. Full Duplex: 전이중 전송방식. 전화기.

### 케이블/커넥터
- `TP`(Twisted Pair)
  - 총 8가닥의 선으로 구성. 두개의 선을 서로 꼬아놓음
    - UTP(Unshield Twisted Pair), STP(Shielded Twisted Pair)
- `Coaxial`(동축)
  - 선 중앙에 심선있음. 전화 또는 회선망 등 사용
- `Fiber`(광)  - 전기신호이 자기장이 없는 빛으로 통신하기 때문에 장거리 고속통신 가능
    - 모드(Single, Multi), 커넥터타입(LC, SC)
- 광 트랜시버
  - 광통신에 사용되는 네트워크 인터페이스 모튤 커넥터
    - SFP, GBIC 등

### 장비의 Capacity 성능
- __Bandwidth__(대역폭)::8차선 도로
  - 주어진 시간대에 네트워크를 통해 이동가능한 정보의 양
- __Throughput__(처리량)::8차선 도로를 달리는 자동차의 양
  - 단위 시간당 디지털 데이터 전송으로 처리하는 양
- __BackPlane__
  - 네트워크 장비가 최대로 처리가능한 데이터 용량
- __CPS__(Connections Per Second): 초당 커넥션 연결수, L4
- __CC__(Concurent Connections): 최대 수용가능한 커넥션
- __TPS__(Transactions Per Seconds): 초당 트랜젝션 연결수, L7, HTTP성능
- 데이터 단위
  - bit & Byte 존재. Kilo, Mega, Giga, Tera로 표현

## UTP 케이블
**::Unshielded Twisted Pair, 주로 근거리 통신망에 사용되는 케이블로, 이더넷망 구성시 가장 많이 보임**

### 코드배열
- **8P8C**: 8개의 선 배열에 따라 다이렉트 또는 크로스 케이블로 구성
  - Direct Cable: PC to Hub -> DTE to DCE
  - Cross Cable: PC to PC, Hub to Hub -> DTE to DTE, DCE to DCE
  - DTE(Data `Terminal` Equipment), DCE(Data `Communication` Equipment)

### Auto MDI-X
- Automatic Medium Dependent Interface Crossover
- 어떤 노드의 연결인지에 따라 다이렉트와 크로스 케이블을 선택하는 불편함을 개선하여, `케이블 타입에 관계없이` 노드 상호간 `자동`으로 통신 가능

### Wi-Fi
- 비영리 기구인 Wi-Fi Aliance의 상표로 전자기기들이 무선랜에 연결할 수 있게 하는 기술
- 무선랜 구성시 WIPS(보안)-AP(무선 Hub)

### Wireshark
> 오픈소스 패킷 분석 프로그램

- 인터페이스를 선택하고 실시간 패킷 확인과 저장, 분석이 가능
- pcap 파일을 통해서 Fram-L2-L3-L4 정보 확인 가능


---

# 데이터링크 계층
> OSI 7 Layer 2계층. 인접한 네트워크 노드끼리 데이터를 전송하는 기능과 절차 제공
- 물리계층에서 발생가능한 오류를 감지, 수정
- 대표적인 프로토콜에는 `이더넷`, 장비는 `스위치`

## 부계층 MAC & LLC
- **MAC (Media Access Control)**: 물리적인 부분. 매체간의 연결방식 제어, 1계층과 연결
- **LLC (Logical Link Control)**: 논리적인 부분. Frame을 만들어 3계층과 연결

## 주요기능
**:: Framing, 회선제어, 흐름제어, 오류제어**

### Framing
- 데이터그램을 캡슐화하여 프레임단위로 만들고 `header` 헤더와 `trailer` 트레일러 추가
- 헤더: 목적지, 출발지 주소, 데이터 내용 정의
- 트레일러: `비트에러` 감지

### 회선제어
- **Select 모드**: 송신자가 나머지 수신자들을 선택하여 전송
- **Poll 모드**: 수신자에게 데이터 `수신 여부를 확인`하여 응답을 확인하고 전송

### 흐름제어
**:: 송신자와 수신자의 데이터를 처리하는 속도 차이를 해결하기 위한 제어**
- Feedback 방식의 Flow Control, 상위 계층은 Rate기반
- **Stop & Wait** : 데이터를 보내고 `ACK` 응답이 올 때까지 기다림
  - 간단히 구현될 수 있지만 비효율적
  - 데이터를 보내고 ACK응답이 오지 않으면 일정시간 후 `다시 보냄`
- **Sliding window**: ACK 응답 없이 여러개의 프레임 연속 전송
  - 1) PC1: Frame 전송후 Window size축소
  - 2) PC2: (현재ACK)-(이전ACK)= Window size
  - 3) PC1: ACK 수신후 Window size 확장

### 오류제어
**:: 전송중에 오류나 손실 발생시 수신측에서 에러탐지 및 재전송**
- **ARQ(Automatic Repeat Request)**: 프레임 손상시 재전송 수행과정
- **Stop & Wait ARQ**
  - 전송측에서 `NAK` 수신시 재전송
  - 주어진 시간에 ACK 안오면 재전송
- **Go Back n ARQ**
  - 1) 전송측 Frame 6개전송
  - 2) 수신측 NAK 3으로 손상응답
  - 3) 전송측 3이 포함된 345 재전송
- **Selective Repeat ARQ**
  - 손상된 Frame만 `선별`하여 재전송

## 이더넷 프레임 구조

### Ethernet v2
__::__ 데이터 링크 계층에서 MAC 통신과 프로토콜 형식을 정의

- **Preamble**: 이더넷 프레임의 시작과 동기화
- **Dest Addr**: 목적지 MAC주소
- **Src Addr**: 출발지 MAC주소
- **Type**: 캡슐화된 패킷의 프로토콜정의
- **Data**: 상위 계층의 데이터
- **FCS(Frame Check Sequence)**: 에러체크

## 스위치
**:: 2계층의 대표적인 장비. MAC주소 기반 통신**
- 허브의 단점을 보완
  - Half duplex -> Full duplex
  - 1 Collision Domain -> 포트별 Collision Domain
- L3 스위치: 라우팅 기능이 있는 스위치

### 스위치 동작방식
**:: 목적지 주소를 MAC 주소 테이블에서 확인, 연결된 포트로 프레임 전달**
1. **Learning**: 출발지 주소가 MAC 테이블에 없으면 해당 주소 저장
2. **Flooding-Broadcasting**: 목적지 주소가 MAC 테이블에 **없으면** `전체포트`로 전달
3. **Forwarding**: 목적지 주소가 MAC 테이블에 **있으면** `해당 포트`로 전달
4. **Filtering-Collision Domain**: 출발지와 목적지가 `같은 네트워크 대역`일 경우 다른 네트워크로 전달하지 않음
5. **Aging**: MAC 주소 테이블의 정보를 일정시간 이후에 삭제

## ARP
**:: ARP(Address Resolution Protocol)- IP주소를 통해 MAC주소를 알려줌**
(ARP Request -- ARP Reply)

### ARP 동작과정

1. **PC1(172.10.10.1) --> PC2(172.10.10.9) 패킷전송** 시도
  - PC1 자신의 `ARP Cache Table` 에서 목적지 `MAC주소` 확인
2. ARP Cache Table 에 있을경우: 패킷전송
   ARP Cache Table 에 **없을경우**: `ARP Request`-Broadcasting
3. PC2(172.10.10.9) 에서 목적지 MAC주소 `ARP Reply`
4. 목적지 MAC주소 ARP Cache Table 에 `저장`, `패킷 전송`

### ARP 헤더구조(pcap)
- Hardware Type: ARP 동작하는 네트워크 환경, 이더넷
- Protocol Type: 프로토콜 종류
- Hardware & Protocol Length
- Operation: 명령코드, 1=ARP Request, 2=ARP Reply
- Hardware Address=MAC, Protocol Address=IP