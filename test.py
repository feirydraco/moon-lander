import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime
import cv2
import base64
from PIL import Image
import numpy as np

def turn_left():
    actions.send_keys(Keys.LEFT).perform()

def turn_right():
    actions.send_keys(Keys.RIGHT).perform()



options = Options()
options.add_argument("window-size=640,480")

# options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', options=options)  # Optional argument, if not specified will search path.
driver.get('http://moonlander.seb.ly/')

actions = ActionChains(driver)

main_page = driver.find_element_by_tag_name("body")
main_page.click()


while True:
    altitude = driver.find_element_by_xpath("//div[@class='infoBox'][10]")
    hSpeed = driver.find_element_by_xpath("//div[@class='infoBox'][12]")
    vSpeed = driver.find_element_by_xpath("//div[@class='infoBox'][11]")
    time = driver.find_element_by_xpath("//div[@class='infoBox'][5]")

    img = driver.get_screenshot_as_png()

    nparr = np.fromstring(img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    

    # cv2.imshow("test", np.array(img))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    print(altitude.text, hSpeed.text, vSpeed.text, datetime.strptime(time.text, '%M:%S'))


time.sleep(20)
driver.quit()