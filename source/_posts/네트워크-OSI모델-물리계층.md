---
title: 네트워크_OSI모델_물리계층
tags: ['network', 'osi_7_layer']
categories: [☁️ TIL]
thumbnail: ''
permalink: ''
status: ''
date: 2021-06-16 15:17:17
---

`#osi_7_layer` `#tcp_ip`
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
- Bandwidth(대역폭)::8차선 도로
  - 주어진 시간대에 네트워크를 통해 이동가능한 정보의 양
- Throughput(처리량)::8차선 도로를 달리는 자동차의 양
  - 단위 시간당 디지털 데이터 전송으로 처리하는 양
- BackPlane
  - 네트워크 장비가 최대로 처리가능한 데이터 용량
- CPS(Connections Per Second): 초당 커넥션 연결수, L4
- CC(Concurent Connections): 최대 수용가능한 커넥션
- TPS(Transactions Per Seconds): 초당 트랜젝션 연결수, L7, HTTP성능
- 데이터 단위
  - bit & Byte 존재. Kilo, Mega, Giga, Tera로 표현

## UTP 케이블
- Unshielded Twisted Pair, 주로 근거리 통신망에 사용되는 케이블로, 이더넷망 구성시 가장 많이 보임

### 코드배열
- 8P8C: 8개의 선 배열에 따라 다이렉트 또는 크로스 케이블로 구성
  - Direct Cable: PC to Hub -> DTE to DCE
  - DTE(Data Terminal Equipment), DCE(Data Communication Equipment)

### Auto MDI-X
- Automatic Medium Dependent Interface Crossover
- 어떤 노드의 연결인지에 따라 다이렉트와 크로스 케이블을 선택하는 불편함을 개선하여, `케이블 타입에 관계없이` 노드 상호간 `자동`으로 통신 가능

### Wi-Fi
- 비영리 기구인 Wi-Fi Aliance의 상표로 전자기기들이 무선랜에 연결할 수 있게 하는 기술
- 무선랜 구성시 WIPS(보안)-AP(무선 Hub)





