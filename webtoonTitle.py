from bs4 import BeautifulSoup
from pprint import pprint
import requests

# requests 모듈 : 파이썬에서 HTTP 요청을 보내는 모듈

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close() # requests.close()가 뭐하는 애지..? 

# 요일별 웹툰목록 한 줄씩 다 가져오기
week = soup.findAll('div', {'class': 'col_inner'})

# pprint(week)
# pprint(week[1])

# 요일별 웹툰 타이틀 리스트
week_title_list = []

for w in week:
  day = w.findAll('a', {'class':'title'})
  # pprint(day)

  title_list = [t.text for t in day]
  # pprint(title_list)
  week_title_list.append(title_list)

pprint(week_title_list)
pprint(len(week_title_list))