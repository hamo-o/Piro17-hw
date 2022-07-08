num = 0

class Not123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

while True:
    try:       
        k = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
        if k != 1 and k != 2 and k != 3:
            raise Not123
        else:
         break
    except ValueError:
        print('정수를 입력하세요')
    except Not123 as e:
        print(e)

for num in range(k):
    print('playerA : {0}'.format(num + 1))