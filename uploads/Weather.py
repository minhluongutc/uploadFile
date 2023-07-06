

from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
    headers = requests.utils.default_headers()
    url = 'https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Y7_MFhVBxPY'
    req = requests.get(url, headers)
    s = BeautifulSoup(req.content, 'html.parser')
    
    '''
    ngay = s.find(id='seven-day-forecast')
    dubao = ngay.find_all(class_='tombstone-container')
    tonight = dubao[0]
    img = tonight.find('img')
    mota = img['title']
    print(mota)s
    tags = s.find(id='current_conditions_detail')
    tags = s.find_all('tr')
    for i in tags:
        name = i.find('b').text
        td = i.find_all('td')
        value = td[1].text
        print('{}:{}'.format(name, value))
    '''
    
    
    '''dem so anh trong trang web'''  
    img=  s.findAll('img')
    print('Tong so anh',len(img))
    
    ''''''
    ngay = s.find(id='seven-day-forecast')
    dubao = ngay.find_all(class_='tombstone-container')
    d = []
    for i in range(len(dubao)):
        period = dubao[i].find(class_='period-name').get_text()
        shortdesc = dubao[i].find(class_='short-desc').get_text()
        temp = dubao[i].find(class_='temp').get_text()
        img = dubao[i].find('img')['title']
        d.append((period, shortdesc, temp, img))
    for i in range(len(d)):
        print(d[i])