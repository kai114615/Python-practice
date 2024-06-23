#氣象局網頁解析
import requests
from bs4 import BeautifulSoup
import datetime
from dateutil.relativedelta import relativedelta
d1=datetime.timedelta(days=1)
m1=relativedelta(months=1)
y1=relativedelta(years=1)

#建立下載日期清單
def daylist(st,ed,m):
    st=st.split("-")
    ed=ed.split("-")

    days = list()
    if m=="d":
        stday=datetime.date(int(st[0]),int(st[1]),int(st[2]))
        edday=datetime.date(int(ed[0]),int(ed[1]),int(ed[2]))
        today = stday
        while today<=edday:
            days.append(str(today))
            today += d1
    elif m=="m":
        stday=datetime.date(int(st[0]),int(st[1]),1)
        edday=datetime.date(int(ed[0]),int(ed[1]),1)
        today = stday
        while today<=edday:
            days.append(str(today)[:-3])
            today += m1
    else:
        stday=datetime.date(int(st[0]),1,1)
        edday=datetime.date(int(ed[0]),1,1)
        today = stday
        while today<=edday:
            days.append(str(today)[:-6])
            today += y1
    return days

print("中央氣象局觀測資料查詢系統資料下載器")
print("請先到觀測資料查詢系統(https://e-service.cwb.gov.tw)找尋你要下載的測站，分別選取起始和終止時間，然後複製網址到下面")

#輸入網址
f=0
while f==0:
    sturl=input("起始網址：")
    edurl=input("結束網址：")
    if sturl[:100] == edurl[:100]:
        f=1
        m=sturl[46:49]              #判斷是何種報表
        if m == "Day":
            print("這是日報表"); m="d"
            st = sturl[sturl.find("datepicker")+11:sturl.find("datepicker")+21]
            ed = edurl[sturl.find("datepicker")+11:sturl.find("datepicker")+21]
        elif m == "Mon":
            print("這是月報表"); m="m"
            st = sturl[sturl.find("datepicker")+11:sturl.find("datepicker")+18]
            ed = edurl[sturl.find("datepicker")+11:sturl.find("datepicker")+18]
        elif m == "Yea":
            print("這是年報表"); m="y"
            st = sturl[sturl.find("datepicker")+11:sturl.find("datepicker")+15]
            ed = edurl[sturl.find("datepicker")+11:sturl.find("datepicker")+15]
        else:
            print("這啥網址?")
            f=0
    else:
        print("不是同一測站不同時間的網址，請重新輸入")

days=daylist(st,ed,m)   #得到下載日期清單

#測站代號
station=sturl[sturl.find("station=")+8:sturl.find("station=")+14]
#url01-原始網址前後相同部分(中間插日期)
url0=sturl[:sturl.find("datepicker")+11]
url1=sturl[sturl.find("&altitude="):]

rows = list()
f=0
for d in days:
    print (d)
    url = url0 + d + url1
    html = requests.get(url)
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text,'html.parser') #用html格式拆解抓下的網頁
    table = sp.find('div', {'id':'hea_t'})
    trs = table.find_all('tr')[:2]  #抓測站名稱
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
    stname = rows[0][1]
    table = sp.find('table', {'id':'MyTable'})
    if f==0:
        trs = table.find_all('tr')[:3]  #標題是所有tr的前三列，用一次就好
        columns = list()
        for tr in trs:
            columns.append([th.text.replace('\n', '').replace('\xa0', '') for th in tr.find_all('th')])
        with open(station+'.csv',"w", encoding='big5') as f:
            f.write(stname+"\n")
            f.write("日期："+st+" to "+ed+"\n")
            for s in columns:
               s0=""
               for s1 in s:
                   s0 += "," + s1
               f.write(s0+"\n")
        f=1
    trs = table.find_all('tr')[3:]  #第4列以後是表格內容，都用td
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
    with open(station+'.csv',"a", encoding='big5') as f:
        for s in rows:
            s0=d
            for s1 in s:
                s0 += "," + s1
            f.write(s0+"\n")
print ("下載完成!")
