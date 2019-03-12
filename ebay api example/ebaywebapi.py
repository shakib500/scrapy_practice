from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

ID_APP = 'SafinMah-webapiex-PRD-516e557a4-8ab3b078'

Keywords = input('what are you searching for? (ex: white piano)\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')