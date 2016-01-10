from selenium import webdriver


# 직방 컨텐츠 가져오기
# 부제: "신사역에 집을 구하고 싶다"

driver = webdriver.Firefox()
driver.get("https://www.zigbang.com/search/map?lat=37.52412796020508&lng=127.02295684814453&zoom=5")

driver.implicitly_wait(30)


room_elements = driver.find_elements_by_css_selector('div#premium-special-map-list div.list-item')

for room_element in room_elements:
    price = room_element.find_element_by_css_selector('div.i-tit strong').get_attribute('innerHTML')
    floor = room_element.find_element_by_css_selector('div.i-tit b').get_attribute('innerHTML')
    info = room_element.find_element_by_css_selector('p.i-info').get_attribute('innerHTML')
    text = room_element.find_element_by_css_selector('p.i-txt').get_attribute('innerHTML')
    print((price, floor, info, text))


driver.quit()
