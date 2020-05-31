from urllib.request import urlopen
from bs4 import BeautifulSoup

search_list = ['2020','2019','2018','2017','2013']
objectlist = []
for year in search_list:
    if year == '2013':
        url = "https://openreview.net/group?id=ICLR.cc/" + year
    elif year == '2017':
        url = "https://openreview.net/group?id=ICLR.cc/" + year + "/conference"
    else:
        url = "https://openreview.net/group?id=ICLR.cc/" + year + "/Conference"
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    objectlist.append(bsObject)

web = objectlist[0]
body = web.find('body',{'class':'group'})
content = body.find('div',{'id':'group-container'})
print(content)
#row = body.find('div',{'class':'row'})
'''
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