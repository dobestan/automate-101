from selenium import webdriver


naver_username = "YOUR_USERNAME"
naver_password = "YOUR_PASSWORD"


driver = webdriver.Firefox()
driver.get("https://nid.naver.com/nidlogin.login")

driver.implicitly_wait(10)


driver.find_element_by_css_selector('input[name="id"]').send_keys(naver_username)
driver.find_element_by_css_selector('input[name="pw"]').send_keys(naver_password)

driver.find_element_by_css_selector('input.int_jogin').click()
