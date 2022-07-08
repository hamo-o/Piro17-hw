num = 0

class Not123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

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

while(num < a):
    print('playerA : {0}'.format(num + 1))
    num += 1
    
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

while(num - a < b):
    print('playerB : {0}'.format(num + 1))
    num += 1