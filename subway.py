# 지하철게임 함수 정의
def subwayGame(dict, idx):
    # 3호선 위키백과 크롤링
    url = "https://ko.wikipedia.org/wiki/%EC%88%98%EB%8F%84%EA%B6%8C_%EC%A0%84%EC%B2%A0_3%ED%98%B8%EC%84%A0"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    # 역 이름을 담을 빈 리스트
    stations = []

    # 대화역만 따로 append
    line3_stations = soup.select(".wikitable > tbody> tr > td:nth-child(3) > a")
    stations.append(line3_stations[0].text)

    # 나머지 3호선 역 append
    line3_stations = soup.select(".wikitable > tbody> tr > td:nth-child(2) > a")

    for line3_station in line3_stations:
        stations.append(line3_station.text)

    # 역 이름 속 () 삭제
    for i in range(len(stations)):
        for j in range(len(stations[i])):
            if stations[i][j] == '(':
                stations[i] = stations[i][:j]
                break

    # 게임시작 노래 출력
    print("""     _______. __    __  .______   ____    __    ____      ___      ____    ____      _______      ___      .___  ___.  _______
    /       ||  |  |  | |   _  \  \   \  /  \  /   /     /   \     \   \  /   /     /  _____|    /   \     |   \/   | |   ____|
   |   (----`|  |  |  | |  |_)  |  \   \/    \/   /     /  ^  \     \   \/   /     |  |  __     /  ^  \    |  \  /  | |  |__
    \   \    |  |  |  | |   _  <    \            /     /  /_\  \     \_    _/      |  | |_ |   /  /_\  \   |  |\/|  | |   __|
.----)   |   |  `--'  | |  |_)  |    \    /\    /     /  _____  \      |  |        |  |__| |  /  _____  \  |  |  |  | |  |____
|_______/     \______/  |______/      \__/  \__/     /__/     \__\     |__|         \______| /__/     \__\ |__|  |__| |_______|

""")
    print('-'*130)
    time.sleep(1)
    print("~"*10+"🚇 지하철~ 지하철 지하철지하철지하철"+"~"*10)
    time.sleep(1)
    print("~"*10+"🚨 몇호선~ 몇호선 몇호선몇호선몇호선"+"~"*10)
    time.sleep(1)
    print("3호선!!!\n")
    time.sleep(1)

    # 지하철 게임 시작!
    while True:
        player_name = dict['이름'][idx]
        # 플레이어일 경우 (플레이어의 idx는 0이라고 가정)
        if idx == 0:
            print(f"\n{player_name}님 차례입니다.")
            answer = input("3호선 역 '이름'을 입력해주세요! (*주의* '이름'만 입력할 것) : ")
            try:
                stations.remove(answer)
            except:
                print("\n🤣 땡땡땡땡!!!! 술이 들어간다 쭉쭉쭉쭉죽~ 🤮")
                dict["주량"][idx] -= 1
                dict['벌주량'][idx] += 1
                break
        # 컴퓨터일 경우
        else:
            print(f"\n{player_name}님 차례입니다.")
            time.sleep(1)
            answer = random.choice(stations)
            # 30% 확률로 컴퓨터는 오답을 입력
            if random.random() > 0.7:
                answer += '역'
            print(f"3호선 역 '이름'을 입력해주세요! (*주의* '이름'만 입력할 것) : {answer}")
            time.sleep(1)
            try:
                stations.remove(answer)
            except:
                print("\n🤣 땡땡땡땡!!!! 술이 들어간다 쭉쭉쭉쭉죽~ 🤮")
                dict["주량"][idx] -= 1
                dict['벌주량'][idx] += 1
                break
        idx = (idx+1)%len(dict['이름'])
    return dict

# 테스트 코드
if __name__ == '__main__':
    # 필요한 모듈 불러오기
    import requests
    from bs4 import BeautifulSoup as bs
    import random
    import time
    # 딕셔너리 임시 지정
    players = {'이름': ['영훈', '병우', '현영', '선희'],
                '주량': [1, 1, 1, 1],
                '벌주량': [0, 0, 0, 0]}
    idx = 2
    players = subwayGame(players, idx)
    print()
    print(players)