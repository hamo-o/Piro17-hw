## 짜다보니 수도코드가아니라 그냥 짜게 되었습미다,, 
## 많이 부족하니까 더 효율적인 코드 아이디어 있으시면 마구마구 바꿔주세요!!

## import : 모듈 추가
import random

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

while True:
    try:
        my_drink = int(input('당신의 치사량은 얼마만큼인가요?(1 ~ 5 보기를 선택해주세요) : '))
        if my_drink > 5 or my_drink < 1:
            raise Not_1_5
    except ValueError:  ## 정수가 아님
        print('1에서 5사이의 보기를 골라주세요')
    except Not_1_5: ## 1~5가 아님
        print('1에서 5사이의 보기를 골라주세요')
    else:
        break

## 같이 대결할 인원 명수 입력받기 & 예외처리
class Not_1_3(Exception):
    pass

while True:
    try:
        pnum = int(input('초대할 사람은 몇명인가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
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
players_name = random.sample(['승아', '지현', '혜영', '찬영', '세윤'], pnum)
players_drink = random.sample(list(range(2,10)), pnum)

players = {'이름' : players_name, '주량' : players_drink}

for i in range(len(players_name)):
    print(f'오늘 함께 취할 친구는 {players_name[i]}입니다! (치사량 : {players_drink[i]})')

print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

## 각 리스트에 내 이름과 주량 추가!
## 결국 리스트 맨 마지막에 플레이어가 오게 되니까
## 미니게임 함수 내에서는 인덱스 -1로 줘서 진행하면 될 것 같슴니다!
players_name.append(my_name)
players_drink.append(my_drink)

## ----------------------------------------------여기서부터 전체반복----------------------------------------------

while True:
        ## while문 안에서 치사량에 도달하면 완전 종료 
        if 0 in players_drink:
            num = players_drink.index(0)
            print(f'{players_name[num]}(이)가 전사했습니다...')
            print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')
            break
        
        ## 아니면 게임 계속하기
        else:
        ## 리스트에 들어있는 순서대로 계속 돌아가기 위해 for문
        ## 더 좋은 방법..?
            for player in players_name:
                
                ## for문 안에서 치사량 도달하면 for문 밖으로 나오기
                if 0 in players_drink:
                    break
                
                ## 플레이어 - 컴1 - 컴2 - 컴3 ... 순서로 게임 선택 반복!
                ## 인트로 & 술래 이름 게임 안에 넣을지 밖에 넣을지?
                ## 게임 내에서의 순서는???
                else: #----------------------------------------------for문 반복--------------------------------------------------

                ## 현재까지 몇 잔 마셨는지, 치사량까지 몇 잔 남았는지 출력
                ## 여기서 현재까지 몇 잔 마셨는지 알기 위해서, 리스트를 따로 생성해서 전체 딕셔너리에 추가하고 함수 내에서
                ## 마신 사람의 리스트 +1 해서 조작하면 좋을 것 같습니다!
                    for i in range(len(players_name)):
                        print(f'{players_name[i]}(은/는) 지금까지 (새로 들어갈 리스트)! \
                    치사량까지 : players_drink[i] - 새로만들리스트[i]')
                    print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

                    ## 게임 보기 출력
                    print('오늘의 술게임')
                    print('1. 지하철')
                    print('2. 레코드')
                    print('3. 아파트')
                    print('4. 업앤다운')
                    print('ıllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllıllııllııllıllııllıllı')

                    print(f'{player}(이)가 ~ 좋아하는 ~ 랜덤 ~ 게임! 무슨 ~ 게임? 게임 ~~ 스타트!!! : ', end = '')
                    
                    ## 플레이어 게임 선택
                    if player == my_name:
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