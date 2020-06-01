from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv

display = Display(visible=0, size=(1024, 768)) 
display.start()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

#path = '/home/jaychoi/utils/chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 60)

url = 'https://openreview.net/group?id=ICLR.cc/2020/Conference#accept-poster'
driver.get(url)

tab = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="accept-poster"]/ul')))

with open('/tmp/output.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['title', 'accept', 'abstract', 'tldr', 'keyword', 'code'])
    paperlist = '//*[@id="accept-poster"]/ul/li'
    papernum = len(driver.find_elements_by_xpath(paperlist))
    for i in range(1,papernum+1):
        unordered_stack = {}
        elementnum = len(driver.find_elements_by_xpath('//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li'%i))
        for j in range(1,elementnum+1):
        xpath_a = '//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li[2]'%i
        abstract = driver.find_element_by_xpath(xpath_a)
        xpath_t = '//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li[1]'%i
        tl_dr = driver.find_element_by_xpath(xpath_t)
        xpath_k = '//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li[3]'%i
        keywords = driver.find_element_by_xpath(xpath_k)
        

driver.quit()
