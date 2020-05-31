from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

display = Display(visible=0, size=(1024, 768)) 
display.start()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

path = '/home/jaychoi/utils/chromedriver' 
driver = webdriver.Chrome(path, options=options)
wait = WebDriverWait(driver, 30)

url = 'https://openreview.net/group?id=ICLR.cc/2020/Conference#accept-poster'
driver.get(url)

tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="accept-poster"]/ul')))

xpath = '//*[@id="accept-poster"]/ul/li[2]/h4/a[1]'
paper_title = driver.find_element_by_xpath(xpath)

print(paper_title.text)
driver.quit()
