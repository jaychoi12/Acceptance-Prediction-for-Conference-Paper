from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import csv

display = Display(visible=0, size=(1024, 768)) 
display.start()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

path = '/home/jaychoi/utils/chromedriver'
driver = webdriver.Chrome(path, options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 60)

url = 'https://openreview.net/group?id=ICLR.cc/2017/conference'
driver.get(url)

first_paper = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="note_BkbY4psgg"]/div[1]/h2/a[1]')))

with open('output_2017.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['title', 'accept', 'abstract', 'tldr', 'keyword', 'code'])
    '//*[@id="note_BkbY4psgg"]'
    paperlist = driver.find_elements_by_xpath('//*[@id="notes"]/div')
    papernum = len(paperlist)
    parent_window = driver.current_window_handle
    for i in range(1,papernum+1):
        if len(driver.find_element_by_xpath('//*[@id="notes"]/div[%d]'%i).get_attribute("id")) < 5:
            continue
        ####### done so far #######
        driver.execute_script("window.open('https://openreview.net/forum?id=BkbY4psgg')") # child window
        all_windows =driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="note_BkbY4psgg"]/div[1]')))
        elementnum = len(driver.find_elements_by_xpath('//*[@id="note_BkbY4psgg"]/div'))
        title_path = '//*[@id="note_BkbY4psgg"]/div[1]/h2/a[1]'
        title = driver.find_element_by_xpath(title_path).text
        print(elementnum)
        print(title)
        break
        for j in range(1, elementnum+1):
            continue


        driver.close() # close child window
        driver.switch_to.window(parent_window)
        
        
driver.quit()     
        
'''        
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
'''
