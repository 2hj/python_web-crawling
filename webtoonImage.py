from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
# 정규표현식 : re모듈
# os모듈 : 파일관리 관련 모듈
from urllib.request import urlretrieve

# 저장 폴더 생성
try:
  if not (os.path.isdir('image')):
    # os.path.isdir : 이미 디렉토리가 있는지 검사
    # os.path.join : 현재 경로를 계산하여 입력으로 들어온 텍스트를 합하여 새로운 경로를 만듦
    # os.makedirs : 입력으로 들어온 경로로 폴더 생성
    os.makedirs(os.path.join('image'))
    # for i in range(1, 8):
    #   if not (os.path.isdir('image/'+i)):
    #     os.makedirs(os.path.join('image/'+i))

except OSError as e:
  if e.errno != errno.EEXIST:
    print("폴더 생성 실패!")
    exit()

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

week_toon_list = soup.findAll('div', {'class':'col_inner'})

# 요일별로 웹툰 리스트 담기
# 리스트는 총 7개
toon_list = []
for week_toon in week_toon_list:
  toon_list.append(week_toon.findAll('li'))
# pprint(len(toon_list))

# folder_num = 0
for toons in toon_list:
  # folder_num += 1
  for li in toons:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    # print(title, img_src)
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    # urlretrieve(img_src, './image/'+folder_num+'/'+title+'.jpg')
    urlretrieve(img_src, './image/'+title+'.jpg')

