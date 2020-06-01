from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

display = Display(visible=0, size=(1024, 768)) 
display.start()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

#path = '/home/jaychoi/utils/chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 30)
url = 'https://openreview.net/group?id=ICLR.cc/2020/Conference#accept-poster'

tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="accept-poster"]/ul')))

xpath = '//*[@id="accept-poster"]/ul/li[2]/h4/a[1]'
paper_title = driver.find_element_by_xpath(xpath)
paper_title.get_attribute()

print(paper_title.text)
driver.quit()
