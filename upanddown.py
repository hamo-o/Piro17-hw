
        
def UpAndDown(p, start):
    from random import randint
    
    class NotInRange(Exception):
        pass
    
    answer = randint(1,50)
    min_num = 1
    max_num = 50
    
    print("~"*120)
    print('''
      ___           ___                  ___           ___          _____                  _____          ___           ___           ___     
     /__/\         /  /\                /  /\         /__/\        /  /::\                /  /::\        /  /\         /__/\         /__/\    
     \  \:\       /  /::\              /  /::\        \  \:\      /  /:/\:\              /  /:/\:\      /  /::\       _\_ \:\        \  \:\   
      \  \:\     /  /:/\:\            /  /:/\:\        \  \:\    /  /:/  \:\            /  /:/  \:\    /  /:/\:\     /__/\ \:\        \  \:\  
  ___  \  \:\   /  /:/~/:/           /  /:/~/::\   _____\__\:\  /__/:/ \__\:|          /__/:/ \__\:|  /  /:/  \:\   _\_ \:\ \:\   _____\__\:\ 
 /__/\  \__\:\ /__/:/ /:/           /__/:/ /:/\:\ /__/::::::::\ \  \:\ /  /:/          \  \:\ /  /:/ /__/:/ \__\:\ /__/\ \:\ \:\ /__/::::::::\\
 \  \:\ /  /:/ \  \:\/:/            \  \:\/:/__\/ \  \:\~~\~~\/  \  \:\  /:/            \  \:\  /:/  \  \:\ /  /:/ \  \:\ \:\/:/ \  \:\~~\~~\/
  \  \:\  /:/   \  \::/              \  \::/       \  \:\  ~~~    \  \:\/:/              \  \:\/:/    \  \:\  /:/   \  \:\ \::/   \  \:\  ~~~ 
   \  \:\/:/     \  \:\               \  \:\        \  \:\         \  \::/                \  \::/      \  \:\/:/     \  \:\/:/     \  \:\     
    \  \::/       \  \:\               \  \:\        \  \:\         \__\/                  \__\/        \  \::/       \  \::/       \  \:\    
     \__\/         \__\/                \__\/         \__\/                                              \__\/         \__\/         \__\/    ''')
    print("~"*120)
    print(f"{p['이름'][start]} 님이 UP&DOWN 게임을 선택했어요!😀")
    print("~"*10,"소주병 뚜껑의 숫자를 맞혀 주세요!", "~"*10)
    
    i = start
    while True:
        
            player = p['이름'][i]

            if i == 0: ## 내 차례
            ########## 플레이어 숫자 입력 ##############
                while True:
                    try:
                        mynum = int(input(f"{min_num}부터 {max_num}까지의 숫자 중 하나를 골라주세요! "))
                        if mynum < min_num or mynum > max_num:
                            raise NotInRange
                    except ValueError:
                        print(f'{min_num}부터 {max_num}사이의 숫자를 골라주세요')
                    except NotInRange:
                        print(f'{min_num}부터 {max_num}사이의 숫자를 골라주세요')
                    else:
                        break
                    print()
            else:   ## 컴퓨터 차례
                mynum = randint(min_num, max_num)
            
            print(f'{player}님은 {mynum}(을/를) 골랐습니다')
            
            if answer > mynum: ## 정답이 외친 숫자보다 크다면
                print('⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️UP!⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️')
                min_num = mynum + 1
            elif answer < mynum: ## 정답이 외친 숫자보다 작다면
                print('⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️DOWN!⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️')
                max_num = mynum - 1
            else: ## 정답이라면
                print()
                print(f'아 누가 술을 마셔 ~~~ {player}(이)가 술을 마셔 {player[0]} ! {player[1]} ! 원 ~~~ 샷 !')
                print()
                break
            print()
            
            i = (i + 1) % len(p['이름'])
    
    p['주량'][i] -= 1
    p['벌주량'][i] += 1
    
    return p


if __name__ == '__main__':
    # 딕셔너리 임시 지정
    players = {'이름': ['영훈', '병우', '현영', '선희'],
                '주량': [1, 1, 1, 1],
                '벌주량': [0, 0, 0, 0]}
    idx = 2
    players = UpAndDown(players, idx)
    print()
    print(players)