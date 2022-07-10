## 짜다보니 수도코드가아니라 그냥 짜게 되었습미다,, 
## 많이 부족하니까 더 효율적인 코드 아이디어 있으시면 마구마구 바꿔주세요!!

## import : 모듈 추가
#각자 만든 파이썬 파일을 추가하기 Ex) import subway as game1

import random
import requests
from bs4 import BeautifulSoup as bs
import time
import copy

## 게임 인트로! : 아스키아트, 인트로멘트
## 같이 꾸며봐요!!

## 사용자의 이름 입력받기
my_name = input('당신의 이름은?? : ')
print()

## 주량 보기 출력
print('ıllıllııllıllııllıllııllıllııllıllııllıllı \
당신의 주량은?? \
ıllıllııllıllııllıllııllıllııllıllııllıllı')
print('1. 알쓰 ~ 소주 반병 (2잔)')
print('2. 소주 반병 ~ 한병 (4잔)')
print('3. 소주 한병 ~ 한병 반 (6잔)')
print('4. 소주 한병 반 ~ 두병 (8잔)')
print('5. 소주 두병 ~ (10잔)')
print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

## 주량 입력받기 & 예외처리
class Not_1_5(Exception):
    pass

# (영훈) 보기 숫자가 아니라 보기에 따른 결과값을 넣어야 해서 수정했습니다.
while True:
    try:
        num = int(input('🤢 당신의 치사량은 얼마만큼인가요?(1 ~ 5 보기를 선택해주세요) : '))
        if num > 5 or num < 1:
            raise Not_1_5
    except ValueError:  ## 정수가 아님
        print('1에서 5사이의 보기를 골라주세요')
    except Not_1_5: ## 1~5가 아님
        print('1에서 5사이의 보기를 골라주세요')
    else:
        break
for i in range(1, 6):
    if num == i:
        my_drink = i*2

## 같이 대결할 인원 명수 입력받기 & 예외처리
class Not_1_3(Exception):
    pass

while True:
    try:
        pnum = int(input('🎉 초대할 사람은 몇명인가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
        if pnum > 3 or pnum < 1:
            raise Not_1_3
    except ValueError:  ## 정수가 아님
        print('1명부터 3명까지 선택이 가능합니다')
    except Not_1_3: ## 1~3이 아님
        print('1명부터 3명까지 선택이 가능합니다')
    else:
        break

## 랜덤으로 선택하기
## 이름과 주량이 랜덤으로 선택된다는 의미..??
## random.sample()로 각각 지정하는 것 말고 다른 좋은 방법?
# (영훈) sample 추출은 좋은데 업데이트를 딕셔너리에서 해야 해서 햇갈릴까봐 변수명을 변경했습니다.
names = random.sample(['승아', '지현', '혜영', '찬영', '세윤'], pnum)
drinks = random.sample(range(2,10), pnum)
penalty = [0] * pnum

players = {'이름' : names, '주량' : drinks, '벌주량': penalty}

for i in range(pnum):
    print(f"오늘 함께 취할 친구는 {players['이름'][i]}입니다! (치사량 : {players['주량'][i]})")

print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

## 딕셔너리 속 각 리스트 맨 앞에 내 이름과 주량 추가! pnum도 1 추가!
players['이름'].insert(0, my_name)
players['주량'].insert(0, my_drink)
players['벌주량'].insert(0, 0)
pnum += 1

## ----------------------------------------------여기서부터 전체반복----------------------------------------------
idx = 0
while True:
        ## while문 안에서 치사량에 도달하면 완전 종료 
        if 0 in players['주량']:
            i = players['주량'].index(0)
            print(f"{players['이름'][i]}(이)가 전사했습니다...")
            print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')
            break
        
        ## 아니면 게임 계속하기
        # (영훈) else를 빼면 코드 가독성이 높아질 것 같아요. 들여쓰기가 많으면 읽기 힘들더라구요.
        
        ## 리스트에 들어있는 순서대로 계속 돌아가기 위해 for문
        ## 더 좋은 방법..?
        # (영훈) 인덱스를 넘겨주기 위해서 for문 수정했습니다
            
        if 0 in players['주량']:
            break
        
        ## 플레이어 - 컴1 - 컴2 - 컴3 ... 순서로 게임 선택 반복!
        ## 인트로 & 술래 이름 게임 안에 넣을지 밖에 넣을지? (영훈) 인트로와 술래 이름은 각자 게임 안에 넣으면 좋을 것 같아요
        ## 게임 내에서의 순서는??? (영훈) 술래부터 시작하도록 idx를 매개변수로 주면 좋을 것 같아요
        #----------------------------------------------for문 반복--------------------------------------------------

        ## 현재까지 몇 잔 마셨는지, 치사량까지 몇 잔 남았는지 출력
        ## 여기서 현재까지 몇 잔 마셨는지 알기 위해서, 리스트를 따로 생성해서 전체 딕셔너리에 추가하고 함수 내에서
        ## 마신 사람의 리스트 +1 해서 조작하면 좋을 것 같습니다!
        for i in range(pnum):
            print(f"{players['이름'][i]}(은/는) 지금까지 {players['벌주량'][i]}! \
        치사량까지 {players['주량'][i]}")
        print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

        ## 게임 보기 출력
        print('오늘의 술게임')
        print('1. 지하철')
        print('2. 레코드판')
        print('3. 아파트')
        print('4. 업앤다운')
        print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

        print(f"{players['이름'][idx]}(이)가 ~ 좋아하는 ~ 랜덤 ~ 게임! 무슨 ~ 게임? 게임 ~~ 스타트!!! : ", end = '')
        
        ## 플레이어 게임 선택
        if idx == 0:
            class Not_1_4(Exception):
                pass

            while True:
                try:
                    gnum = int(input())
                    if gnum > 4 or gnum < 1:
                        raise Not_1_4
                except ValueError:  ## 정수가 아님
                    print('1에서 4 사이의 보기를 골라주세요')
                except Not_1_4: ## 1~4가 아님
                    print('1에서 4 사이의 보기를 골라주세요')
                else:
                    break

        ## 컴퓨터 게임 선택
        else:
            gnum = random.randint(1,4)
            print(f'{gnum}')
        
        print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

        ## 게임 실행
        # if gnum == 1:
        #     Subway(players)
        # elif gnum == 2:
        #     Record(players)
        # elif gnum == 3:
        #     Apartment(players)
        # else:
        #     UpAndDown(players)
        idx = (idx+1)%pnum