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

with open('output_acceptposter.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['title', 'accept', 'abstract', 'tldr', 'keyword', 'code'])
    
    #set_order = {'title':0, 'accept':1, 'abstract':2, 'tldr':3, 'keyword':4, 'code':5}
    paperlist = '//*[@id="accept-poster"]/ul/li'
    papernum = len(driver.find_elements_by_xpath(paperlist))
    for i in range(1,papernum+1):
        tsvrow = [None]*6
        elementnum = len(driver.find_elements_by_xpath('//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li'%i))
        for j in range(1,elementnum+1):
            title_path = '//*[@id="accept-poster"]/ul/li[%d]/h4/a[1]'%i
            title = driver.find_element_by_xpath(title_path).get_attribute("textContent")
            tsvrow[0] = title
            
            key_path = '//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li[%d]/strong'%(i,j)
            key = driver.find_element_by_xpath(key_path).get_attribute("textContent")
            content_path = '//*[@id="accept-poster"]/ul/li[%d]/div[@class="collapse"]/div/ul/li[%d]/span'%(i,j)
            content = driver.find_element_by_xpath(content_path).get_attribute("textContent")
            if key == 'TL;DR:':
                tsvrow[3] = content
            elif key == 'Abstract:':
                tsvrow[2] = content
            elif key == 'Keywords:':
                tsvrow[4] = content
            elif key == 'Code:':
                tsvrow[5] = content
            else:
                continue
            tsvrow[1] = '1' #accept

        #have stacked elements for paper i
        #need to stack in the tsv file in order
        #print("stack ",unordered_stack)
        #for key,content in unordered_stack.items():

        #print("row ",tsvrow)
        tsv_writer.writerow(tsvrow)
            
        
driver.quit()
