import requests
from bs4 import BeautifulSoup

url = 'https://blog.xuite.net/peter820615/IansbekerWeatherBureau'
r = requests.get(url)
print(r.text)




sp = BeautifulSoup(r.text, 'html.parser')
sp.body.text
sp.a.text