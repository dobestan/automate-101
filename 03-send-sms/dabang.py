from selenium import webdriver


# 다방에서 공인중개사 연락처 가져오기
# 부제: 하나씩 보면서 연락하기 귀찮아. 전체 연락처를 가져와보자.

driver = webdriver.Firefox()
driver.get("""http://www.dabangapp.com/search#/search?type=subway&id=446&filters={"deposit-range":[0,999999],"price-range":[0,999999],"room-type":[0,1,2,3,4,5],"location":[[127.00468076340508,37.50362345510044],[127.03536523453545,37.52894892024945]]}&position={"center":[127.02002299897026,37.51628726200644],"zoom":15}""")
driver.implicitly_wait(10)


# 세부 페이지를 크롤링할 새로운 브라우저를 키자.
new_driver = webdriver.Firefox()

room_elements = driver.find_elements_by_css_selector('ul.items li.item')

f = open('다방_신사역_공인중개사_연락처.csv', 'w')

# 여기서는 샘플로 5개만 데이터를 가져오자.
for room_element in room_elements[:5]:
    room_detail_page_url = room_element.find_element_by_css_selector('a').get_attribute('href')

    new_driver.get(room_detail_page_url)
    new_driver.implicitly_wait(10)

    new_driver.find_element_by_css_selector('div.contact-view-button-wrap button').click()
    phonenumber = new_driver.find_element_by_css_selector('div.agent-profile-wrap span.number').text.replace('-', '')

    print(phonenumber)
    f.write(phonenumber + '\n') 


driver.quit()
new_driver.quit()

f.close()
