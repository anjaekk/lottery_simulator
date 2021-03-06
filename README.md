# 🎰 lottery_simulator
---

파이썬으로 구현한 Lottery Simulator


## 1. 개요
---
사용자의 선택에 따라 수동(1~6개) 혹은 자동으로 사용자의 번호를 입력받고 매번 새롭게 생성되는 당첨번호와 비교하여 당첨 여부를 알려준다. 

## 2. 구현 상세 내용
---
### 1) 입력받기
(1) `원하는 번호를 공백(' ')으로 구분해 입력해 주세요.`라는 문구가 나오면 원하는 번호를 공백으로 구분해 입력한다.
>**입력 예시)**
```
1 22
```

(2) 입력된 번호중 0이거나 45를 초과하는 번호는 삭제한다.

### 2) 사용자 번호 배정받기
(1) 자동이라면 6개의 숫자를, 수동이라면 6개 - 입력받은 숫자의 개수를 랜덤으로 출력해준다.
(2) 출력된 번호는 1~45까지의 숫자이며, 중복된 번호가 없도록 한다.

>**출력 예시)**
```
당신의 번호는 아래와 같습니다. 
[1, 4, 22, 26, 31, 35]
```

### 3) 당첨여부 의사 확인
(1) `당첨여부를 확인하시겠습니까? Y / N`로 확인 의사를 묻는다. 
(2) 사용자는 y, Y, n, N 중 한개로 답한다.

>**입력 예시)**
```
y
```

### 4) 당첨번호 및 당첨여부 확인
(1) 보너스 번호를 포함하여 랜덤으로 생성된 7개의 번호를 생성한다. 앞의 6자리는 오름차순으로 정렬되어있으며 보너스 번호를 정렬에서 제외시킨다.
>**출력 예시)**
```
당첨번호는 아래와 같습니다. 
[10, 12, 19, 33, 36, 44, 4]
```

(2) 당첨여부를 확인하기전 긴장감 조성을 위해 3초 카운팅을 해준다.
>**출력 예시)**
```
3 
2
1
```

(3) 사용자의 번호와 당첨번호를 비교하여 맞는 숫자의 수에 따라 당첨 여부를 출력한다.(2등은 5개의 일반번호와 보너스번호가 당첨된 경우이다.)
>**출력 예시)**
```
아쉽게도 낙첨입니다.
```

(4) 당첨결과는 다음과 같이 출력된다.

- 1등
```
결과: 6개 일치
축하합니다! '1등' 당첨입니다.
```
- 2등
```
결과: 5개 일치 및 보너스 번호 일치
축하합니다! '2등' 당첨입니다.
```
- 3등
```
결과: 5개 일치
축하합니다! '3등' 당첨입니다.
```
- 4등
```
결과: 4개 일치
축하합니다! '4등' 당첨입니다.
```
- 5등
```
결과: 3개 일치
축하합니다! '5등' 당첨입니다.
```
- 그외
```
아쉽게도 낙첨입니다.
```
