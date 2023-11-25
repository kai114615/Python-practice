# 讀取遠端資料
# COVID-19各國家地區累積病例數與死亡數
# https://data.gov.tw/dataset/120449
import requests
url = 'https://od.cdc.gov.tw/eic/covid19/covid19_global_cases_and_deaths.csv'
r = requests.get(url)
r.encoding = "utf-8"    #文字的編碼設定
r

#print(r.status_code)  #回傳網頁的狀態碼，200代表正常
#print(r.text)

with open('covid-19.csv', 'w') as f:
    f.write(r.text)



