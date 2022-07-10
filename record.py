# 레코드판 게임
# 이 게임의 치명적 단점.. --> 벅스에서 제공하는 곡 표기 그대로 적어야 함 (게임 진행 시 아래 곡 리스트 참고해주세요)
# 청하 : 벌써 12시, Love U, Drive, Roller Coaster, Killing me, Bad Boy, Snapping, BB, Chica, Bicycle
# 블랙핑크 : Lovesick Girls, 불장난, 마지막처럼, 휘파람, How You Like That, STAY, Pretty Savage, 붐바야
# 소녀시대 : Lion Heart, PARTY, Holiday, Gee, Kissing You, Mr.Mr., I GOT A BOY, The Boys

import requests
from bs4 import BeautifulSoup as bs
import random
import time

# players = {'이름':["영훈", "병우", "선희", "현영"],'주량':[5, 3, 5, 2], '벌주량':[0,0,0,0]} # 나중에 삭제

#musics = []

def crawl(singer):
    list = []
    url = f"https://music.bugs.co.kr/search/track?q={singer}&flac_only=false&target=ARTIST_TRACK_ALBUM&page=1&sort=P"
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    play_lists = soup.select("#DEFAULT0 > table > tbody > tr")
    for play_list in play_lists:
        list.append(play_list.select_one(".title a").get("title"))
    return list

def music_setting():
    musics = []
    singers = ["청하", "블랙핑크","소녀시대"]
    for singer in singers:
        musics.append(crawl(singer))
    return musics

def asciiArt():
    print('''.______       _______   ______   ______   .______       _______       _______      ___      .___  ___.  _______  __   __
|   _  \     |   ____| /      | /  __  \  |   _  \     |       \     /  _____|    /   \     |   \/   | |   ____||  | |  |
|  |_)  |    |  |__   |  ,----'|  |  |  | |  |_)  |    |  .--.  |   |  |  __     /  ^  \    |  \  /  | |  |__   |  | |  |
|      /     |   __|  |  |     |  |  |  | |      /     |  |  |  |   |  | |_ |   /  /_\  \   |  |\/|  | |   __|  |  | |  |
|  |\  \----.|  |____ |  `----.|  `--'  | |  |\  \----.|  '--'  |   |  |__| |  /  _____  \  |  |  |  | |  |____ |__| |__|
| _| `._____||_______| \______| \______/  | _| `._____||_______/     \______| /__/     \__\ |__|  |__| |_______|(__) (__)

''')


def record(players, idx): # 메인 함수
    musics = music_setting()
    asciiArt()
    print(f"{players['이름'][idx]}의 차례입니다!")
    check = False
    # 입력받기
    while True:
        if idx == 0: # 스타터가 사람인 경우
            song = input('레코드판~ 레코드판~ 삐끼삐끼~~ : ')
            for i in range(len(musics)):
                for j in range(len(musics[i])):
                    if song == musics[i][j]:
                        singer_index = i
                        check = True
                        musics[singer_index].remove(song)
                        idx = (idx+1)%len(players['이름'])
                        break
                if check == True:
                    break
            if check == True:
                break
        else: # 스타터가 컴퓨터인 경우
            singer_index = random.randint(0, len(musics)-1)
            ply_random_idx = random.randint(0, len(musics[singer_index])-1)
            ply = musics[singer_index][ply_random_idx]
            print(f"레코드판~ 레코드판~ 삐끼삐끼~~ : {ply}")
            musics[singer_index].remove(ply)
            idx = (idx+1)%len(players['이름'])
            break

    # 게임 진행
    while True:
        if idx == 0: # 입력 받아야 함
            time.sleep(1)
            song = input(f"????(기대기대*^^*)???? {players['이름'][idx]} : ")
            if song in musics[singer_index]:
                musics[singer_index].remove(song)
                print("올~ㅋ")
            else:
                print(players['이름'][idx], "바보샷~ 바보샷~")
                players['주량'][idx] -= 1
                players['벌주량'][idx] += 1
                return players        
        else: # 랜덤 할당
            time.sleep(1)
            result = random.randint(1,10)
            song_random = random.randint(0, len(musics[singer_index])-1)
            if 1 <= result <= 7: # 맞추는 경우
                print(f"????(기대기대*^^*)???? {players['이름'][idx]} : {musics[singer_index][song_random]}")
                print("올~ㅋ")
                musics[singer_index].remove(musics[singer_index][song_random])
            else: # 틀리는 경우
                print(f"????(기대기대*^^*)???? {players['이름'][idx]} : 모르겠당^!^")
                print(players['이름'][idx], "바보샷~ 바보샷~")
                players['주량'][idx] -= 1
                players['벌주량'][idx] += 1
                return players 
        idx = (idx+1)%len(players['이름'])


# if __name__ == '__main__':
#     record(players,0)
#     print(players)
