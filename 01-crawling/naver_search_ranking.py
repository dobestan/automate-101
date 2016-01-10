import lxml.html
import requests


# 네이버 실시간 검색어 크롤링하기

response = requests.get("http://www.naver.com/")
assert response.status_code is 200

dom = lxml.html.fromstring(response.content)

ranking_elements = dom.cssselect('ol#realrank li')

for ranking_element in ranking_elements[:-1]:
    ranking_title_element = ranking_element.cssselect('a')[0]
    print(ranking_title_element.text)
