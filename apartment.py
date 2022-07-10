from random import *
import copy
from sys import exec_prefix
#####인트로 그림 및 멘트 & 시작 여부 묻기
##사용자 이름 받기
#user = input('사용자의 이름을 입력해주세요')
player = {'이름':['영훈', '병우', '선희', '현영'], '주량':[1, 3, 5, 2]}
# player['이름'] .append(user)
##본인 주량 선택(보기 중에서 선택 & 예외처리)
##초대할 명 수 고르기 (사람 및 주량은 랜덤)
##Howmany = input('몇명을 초대할까요? (2~4명)')
#--------------------------------------------------#
#현재까지 몇잔 마셨는지, 치사량까지 몇잔 남았는지
for i in range(len(player['이름'])):
  print(player['이름'][i] ," :", player['주량'][i] )
#게임 리스트 (게임 끝날 때마다 2개 반복)
#무슨 게임~ 게임스타트~
#--------------------------------------------------#

def apartment(cur_player, Howmany):
  
  print('--------- 아파트 아스키 문자 ------------')
  print(f'{cur_player} 님이 아파트 게임을 선택했어요!')
  
  while True:
    try:
      floor = int(input('아파트 몇층? : '))
      if floor < 0:
        print('정수로 입력해주세요!',end='\n\n')
      else:
        break
    except:
      print('정수로 입력해주세요!',end='\n\n')
  
  # player_double 는 player들을 2번씩 넣은것 (손이 2개니까)
  player_double = copy.deepcopy(player['이름'])
  player_double.extend(player['이름'])
  # player_shuffle 는 player_double의 순서를 섞은것
  shuffle(player_double)
  
  share = floor // (Howmany*2)
  remainder = floor % (Howmany*2)

  if remainder > 0:
    for i in player_double[remainder-1::-1]:
      print("-"*10, i, "-"*10)
  
  if share > 0:  
    for i in range(share):
      for j in player_double[::-1]:
        print("-"*10, j,"-"*10)  

  print()

  try:
    loser_index = player['이름'].index(player_double[remainder-1])
    player['주량'][loser_index] -= 1
  except:
    print('??')

  print(f"{player['이름'][loser_index]} 님이 걸리셨어요! ")

apartment('용빈',4)

for i in range(len(player['이름'])):
  print(player['이름'][i] ," :", player['주량'][i] )