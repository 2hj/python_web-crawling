from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'detail_box'}) 
# bs4 객체
# find(태그, {속성: 속성값}) : 해당 부분만 추려옴. 처음 매칭된 1개만 가져옴
# findAll(태그, {속성: 속성값}) : 해당되는 모든 것을 리스트로 반환
# find, findAll 모두 태그만으로도 추출 가능
# pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

# 미세먼지
fine_dust = data2[0].find('span', {'class':'num'}).text
print(fine_dust)

# 초미세먼지
ultra_fine_dust = data2[1].find('span', {'class':'num'}).text
print(ultra_fine_dust)