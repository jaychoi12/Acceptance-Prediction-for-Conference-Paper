from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys


display = Display(visible=0, size=(1024, 768)) 
display.start()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

path = '/home/jaychoi/utils/chromedriver' 
driver = webdriver.Chrome(path, options=options)

url = 'https://openreview.net/group?id=ICLR.cc/2020/Conference'
driver.get(url)

tab = driver.find_element_by_xpath('//*[@id="notes"]/div/ul/li[3]/a')
driver.execute_script("arguments[0].click();", tab)


driver.implicitly_wait(3)

xpath = '//*[@id="accept-spotlight"]'
#xpath = '//*[@id="accept-poster"]/ul/li[1]/h4/a[1]'
#xpath = '//*[@id="accept-poster"]/ul/li[1]/h4/a[1]/text()'
#xpath = '//*[@id="accept-poster"]/ul'
paper_title = driver.find_element_by_xpath(xpath)

print(paper_title.getId())
driver.quit()
