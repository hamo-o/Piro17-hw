num = 0
flag = 0

class Not123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

while True:
    while True:
        try:       
            a = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
            if a != 1 and a != 2 and a != 3:
                raise Not123
            else:
                break
        except ValueError:
            print('정수를 입력하세요')
        except Not123 as e:
            print(e)

    for i in range(a):
        if num == 31:
            break
        else:
            flag = 0
            print('playerA : {0}'.format(num + 1))
            num += 1
    
    if num == 31:
        if flag == 1:
            print('playerA win!')
            break
        else:
            print('playerB win!')
            break
        
    while True:
        try:       
            b = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
            if b != 1 and b != 2 and b != 3:
                raise Not123
            else:
                break
        except ValueError:
            print('정수를 입력하세요')
        except Not123 as e:
            print(e)

    for i in range(b):
        if num == 31:
            break
        else:
            flag = 1
            print('playerB : {0}'.format(num + 1))
            num += 1
        
    if num != 31:
        pass
    elif flag == 1:
        print('playerA win!')
        break
    else:
        print('playerB win!')
        break
