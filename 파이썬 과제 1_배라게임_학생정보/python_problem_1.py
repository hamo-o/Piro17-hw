from random import randint

num = 0

class Not123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

class End(Exception):
    pass

def brGame(player):
    global num
    
    if player == p:
        while True:
            try:       
                k = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                if k != 1 and k != 2 and k != 3:
                    raise Not123
            except ValueError:
                print('정수를 입력하세요')
            except Not123 as e:
                print(e)
            else:
                break
    else:
        k = randint(1,3)

    for i in range(k):
        if num == 31:
            break
        else:
            print('{0} : {1}'.format(player, num + 1))
            num += 1
            
    if num == 31:
        if player == c:
            print('player win!')
        else:
            print('computer win!')
        raise End
            
c = 'computer'
p = 'player'

while True:
    try:
        brGame(c)
        brGame(p)
    except End:
        break

