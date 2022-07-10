from random import *
import copy

players = {'이름':['영훈', '병우', '선희', '현영'], '주량':[1, 3, 5, 2],'벌주량': [0,0,0,0]}
pnum=4

idx = 0
# idx=3

def apartment(cur_player, Howmany):
  
  print("~"*120)
  print("""
          _______                    __                         __        _______                       
        |   _   |.-----.---.-.----.|  |_.--------.-----.-----.|  |_     |     __|.---.-.--------.-----.
        |       ||  _  |  _  |   _||   _|        |  -__|     ||   _|    |    |  ||  _  |        |  -__|
        |___|___||   __|___._|__|  |____|__|__|__|_____|__|__||____|    |_______||___._|__|__|__|_____|
                |__|                                                                                  
    """)
  print("~"*120)

  print(f'{cur_player} 님이 아파트 게임을 선택했어요!😀')
  print("~"*10, "아~파트 아파트 아~파트 아파트🏢 ", "~"*10)
  
  while True:
    if idx ==0:
      try:
        floor = int(input('아파트 몇층? : '))
        if floor < 0:
          print('정수로 입력해야쥐~😏',end='\n\n')
        else:
          break
      except:
        print('정수로 입력해야쥐~😏',end='\n\n')
    else:
      floor = randint(2,20)
      print('아파트 몇 층? : ', floor)
      break
    
  print()
  # player_double 는 player들을 2번씩 넣은것 (손이 2개니까)
  player_double = copy.deepcopy(players['이름'])
  player_double.extend(players['이름'])
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

  loser_index = players['이름'].index(player_double[remainder-1])
  players['주량'][loser_index] -= 1
  players['벌주량'][loser_index] += 1
  # print(player)

  print(f"{players['이름'][loser_index]} 님이 걸리셨어요! 😜")
  print("마셔마셔~ 먹고죽어~ 😈")

apartment(players['이름'][idx],pnum)
