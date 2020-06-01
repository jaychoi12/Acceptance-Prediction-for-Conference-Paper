import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#ua = UserAgent()

driver = webdriver.Chrome(ChromeDriverManager().install())
'''
search_list = ['2020','2019','2018','2017','2013']
objectlist = []
for year in search_list:
    if year == '2013':
        url = "https://openreview.net/group?id=ICLR.cc/" + year
    elif year == '2017':
        url = "https://openreview.net/group?id=ICLR.cc/" + year + "/conference"
    else:
        url = "https://openreview.net/group?id=ICLR.cc/" + year + "/Conference"
    #html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}).content
    bsObject = BeautifulSoup(html, "html.parser")
    objectlist.append(bsObject)
    '''
driver.get("https://openreview.net/group?id=ICLR.cc/2020/Conference")
html = driver.page_source

#soup = BeautifulSoup(html, 'html.parser')
#v = soup.select('html > body > div.container > div.row > div.col-xs-12 > main > #group-container > #notes > div.tabs-container')
nav = driver.find_element_by_css_selector('html > body > div.container > div.row > div.col-xs-12 > main > #group-container > #notes > div.tabs-container > ul')

#searchlist = ['#accept-poster', '#accept-spotlight','#accept-talk','#reject']

'''
web = objectlist[0]
body = web.find('body',{'class':'group'})
content = body.find('main',{'id':'content'})
print(content)
#row = body.find('div',{'class':'row'})

previous = body
path = ['row','col-xs-12','group-container','notes','tabs-container']
for step in path:
    current = previous.find('div',{'class': step })
    print('------')
    print(current)
    if step == 'col-xs-12':
        current = current.find('main',{'id':'content'})
    previous = current
print(current)
'''