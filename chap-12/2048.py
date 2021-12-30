
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')

while True:
    toElem = browser.find_element_by_tag_name('html')
    toElem.send_keys(Keys.UP)
    toElem.send_keys(Keys.LEFT)
    toElem.send_keys(Keys.RIGHT)
    toElem.send_keys(Keys.DOWN)
