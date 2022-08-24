#함수 이름은 변경 가능합니다.

class student:  
    def __init__(self, name, mid_score, fin_score, grade):
        self.name = name
        self.mid_score = mid_score
        self.fin_score = fin_score
        self.grade = grade
    
    def calgrade(self):
        grade = (self.mid_score + self.fin_score) / 2
        if grade >= 90:
            self.grade = 'A'
        elif grade >= 80:
            self.grade = 'B'
        elif grade >= 70:
            self.grade = 'C'
        else:
            self.grade = 'D'

##############  menu 1
from posixpath import split

def Menu1(n, m, f):
    students.append(student(n, m, f, 'undefined'))
#     #사전에 학생 정보 저장하는 코딩 

# ##############  menu 21
def Menu2():
    for i in range(len(students)):
        students[i].calgrade()
#     #학점 부여 하는 코딩

# ##############  menu 3
def Menu3():
    print('-'*30)
    print('name','mid','final','grade', sep = '   ')
    print('-'*30)

    for i in range(len(students)):
        print(f'{students[i].name}'.ljust(6), f'{students[i].mid_score}'.ljust(5),
f'{students[i].fin_score}'.ljust(7), f'{students[i].grade}'.ljust(5))
#     #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
students = []

class ExistName(Exception):
    pass

class NotInt(Exception):
    pass

class NotInList(Exception):
    pass

class NotGraded(Exception):
    pass

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        try:
            name, mid_score, final_score = input('Enter name mid-score final-score : ').split()

            if not mid_score.isnumeric() or not final_score.isnumeric():
                raise NotInt
            
            for i in range(len(students)):
                if name == students[i].name:
                    raise ExistName
                
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        except ValueError:
            print('Num of data is not 3!')
        except ExistName:
            print('Already exist name!')
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        except NotInt:
            print('Score is not positive integer!')
        else:
            Menu1(name, int(mid_score), int(final_score))

    elif choice == "2" :
        try:
            if len(students) == 0:
                raise NotInList

    #예외사항 처리(저장된 학생 정보의 유무)
        except NotInList:
            print('No student data!')
    #예외사항이 아닌 경우 2번 함수 호출
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3" :
        try:
            if len(students) == 0:
                raise NotInList
            
            for i in range(len(students)):
                if students[i].grade == 'undefined':
                    raise NotGraded
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        except NotInList:
            print('No student data!')
        except NotGraded:
            print("There is a student who didn't get grade.")
    #     #예외사항이 아닌 경우 3번 함수 호출
        else:
            Menu3()

    elif choice == "4" :
        try:
            if len(students) == 0:
                raise NotInList
    #     #예외사항 처리(저장된 학생 정보의 유무)
        except NotInList:
            print('No student data!')
    #     #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        else:
            flag = 0
            name = input('Enter the name to delete : ')
            for i in range(len(students)):
                if name == students[i].name:
                    Menu4(i)
                    print(f"{name} student information is deleted.")
                    flag = 1
                    break
            if flag == 0:
                print("Not exist name!")
                
    #     #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
    #     #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print('Exit Program!')
        #반복문 종료
        break

    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
