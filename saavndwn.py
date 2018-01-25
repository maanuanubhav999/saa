from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

dr=webdriver.Chrome()

dr.get("http://en.savefrom.net/1-how-to-download-youtube-video/")

usr= "https://www.saavn.com/p/radio/english-featured-station/Workout"

sfurl=dr.find_element_by_id('sf_url')
sfurl.send_keys(usr)

sfsubmit=dr.find_element_by_id('sf_submit')
sfsubmit.submit()


dwn=WebDriverWait(dr, 30).until(dr.find_element_by_class_name('def-btn-box').click())
