import requests

url = 'https://img.youtube.com/vi/qo3H-VgXmHE/sddefault.jpg'
r = requests.get(url)

with open('ng-girl.jpg', 'wb') as f:   #二進位用wb
    f.write(r.content)    #二進位用content

