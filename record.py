# 레코드판 게임
# 이 게임의 치명적 단점.. --> 벅스에서 제공하는 곡 표기 그대로 적어야 함 (게임 진행 시 아래 곡 리스트 참고해주세요)
# 청하 : 벌써 12시, Love U, Drive, Roller Coaster, Killing me, Bad Boy, Snapping, BB, Chica, Bicycle
# 블랙핑크 : Lovesick Girls, 불장난, 마지막처럼, 휘파람, How You Like That, STAY, Pretty Savage, 붐바야
# 소녀시대 : Lion Heart, PARTY, Holiday, Gee, Kissing You, Mr.Mr., I GOT A BOY, The Boys

import requests
from bs4 import BeautifulSoup as bs

import random

players = {'이름':["영훈", "병우", "선희", "현영"],'주량':[5, 3, 5, 2]} # 나중에 삭제

musics = []

def crawl(singer, musics):
    list = []
    url = f"https://music.bugs.co.kr/search/track?q={singer}&flac_only=false&target=ARTIST_TRACK_ALBUM&page=1&sort=P"
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    play_lists = soup.select("#DEFAULT0 > table > tbody > tr")
    for play_list in play_lists:
        list.append(play_list.select_one(".title a").get("title"))
    musics.append(list)

def music_setting(musics):
    singers = ["청하", "블랙핑크","소녀시대", "샤이니"]
    for singer in singers:
        crawl(singer, musics)
    return musics


def record(musics, players, me): # 메인 함수
    music_setting(musics)
    print(f'{me}의 차례입니다!')
    check = False
    # 입력받기
    while True:
        song = input('레코드판~ 레코드판~ 삐끼삐끼~~ : ')
        for i in range(len(musics)):
            for j in range(len(musics[i])):
                if song == musics[i][j]:
                    singer_index = i
                    check = True
                    musics[singer_index].remove(song)
                    break
            if check == True:
                break
        if check == True:
            break
    # 게임 진행
    while True:
        for i in range(len(players['이름'])):
            if players['이름'][i] == me: # 입력 받아야 함
                song = input(f"????(기대기대*^^*)???? {players['이름'][i]} : ")
                if song in musics[singer_index]:
                    musics[singer_index].remove(song)
                    print("올~ㅋ")
                else:
                    print(players['이름'][i], "바보샷~ 바보샷~")
                    players['주량'][i] -= 1
                    return players        
            else: # 랜덤 할당
                result = random.randint(1,10)
                song_random = random.randint(0, len(musics[singer_index]))
                if 1 <= result <= 7: # 맞추는 경우
                    print(f"????(기대기대*^^*)???? {players['이름'][i]} : {musics[singer_index][song_random]}")
                    print("올~ㅋ")
                    musics[singer_index].remove(musics[singer_index][song_random])
                else: # 틀리는 경우
                    print(f"????(기대기대*^^*)???? {players['이름'][i]} : 모르겠당^!^")
                    print(players['이름'][i], "바보샷~ 바보샷~")
                    players['주량'][i] -= 1
                    return players 

record(musics,players,"선희")
print(players)






