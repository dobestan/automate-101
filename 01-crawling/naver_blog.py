import lxml.html
import requests


# 네이버 키워드 검색 후, 상위 블로그 리스트 크롤링하기
# 부제: "내가 만약 직방의 마케터라면?"

keywords = [
    '신사동 원룸',
    '신사역 오피스텔',
    '신사역 월세',
    '신사역 전세',
]

for keyword in keywords:
    query = keyword.replace(' ', '+')
    response = requests.get("https://search.naver.com/search.naver?query={query}".format(query=query))
    assert response.status_code is 200


    dom = lxml.html.fromstring(response.content)

    blog_post_elements = dom.cssselect('li.sh_blog_top')

    for blog_post_element in blog_post_elements:
        title = blog_post_element.cssselect('a.sh_blog_title')[0].attrib.get('title')
        blog_name = blog_post_element.cssselect('a.txt84')[0].text
        url = blog_post_element.cssselect('a.sh_blog_title')[0].attrib.get('href')
        print((keyword, title, blog_name, url))
