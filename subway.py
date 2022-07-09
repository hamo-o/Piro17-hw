import requests
from bs4 import BeautifulSoup as bs

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

print(stations)
print(len(stations))