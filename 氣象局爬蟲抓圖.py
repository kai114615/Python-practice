import requests
url = 'https://www.cwb.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/LCC_VIS_TRGB_2750.jpg'
r = requests.get(url)

with open('LCC_VIS_TRGB_2750.jpg', 'wb') as f:
    f.write(r.content)



!wget -O taiwan_radar.png https://www.cwb.gov.tw/Data/radar/CV1_3600.png