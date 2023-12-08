import os
import datetime as dt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# 爬蟲基本相關設定
ervice = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.cwa.gov.tw/V8/C/P/Rainfall/Rainfall_10Min_County.html')

# 開始計時
start = dt.datetime.now()

# 等待雨量表顯示並點擊"前二日"來做大至小排序
locator = (By.ID, 'Rainfall_MOD')
driver_wait = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(locator), '找無元素')
b2dsort = driver.find_element(By.ID, 'before')
b2dsort.click()

datas = driver.find_elements(By.XPATH, '//*[@id="Rainfall_MOD"]/tr')

# 建立資料串列
station_data = []
region_data = []
today_data = []
yesterday_data = []
before_data = []


try:
    # 將雨量表格爬下來
    for data in datas:
        station = data.find_element(
            By.XPATH, './th').text
        region = data.find_element(
            By.XPATH, './td[1]').text
        today = data.find_element(
            By.XPATH, './td[8]').text
        yesterday = data.find_element(
            By.XPATH, './td[9]').text
        before = data.find_element(
            By.XPATH, './td[10]').text

        # 修正雨量值非零之數值
        if (today == '-') or (today == 'X'):
            today = float(0)
        if (yesterday == '-') or (yesterday == 'X'):
            yesterday = float(0)
        if (before == '-') or (before == 'X'):
            before = float(0)

        # 爬下來的雨量站裝入各自的[]中
        station_data.append(station)
        region_data.append(region)
        today_data.append(today)
        yesterday_data.append(yesterday)
        before_data.append(before)
except Exception as e:
    print('失敗', e)

driver.quit()

# 將list轉換成浮點數字
td = list(map(float, today_data))
yd = list(map(float, yesterday_data))
bd = list(map(float, before_data))


#算出前日與昨日的日累積雨量，並輸出成list
yd_rainfall = []
bd_rainfall = []
for i in range(len(td)):
    yd_rf = yd[i]-td[i]  #昨日累積雨量
    bd_rf = bd[i]-yd[i]  #前日累積雨量

    yd_rainfall.append(yd_rf)
    bd_rainfall.append(bd_rf)



#將雨量值存於df{}中
df_rainfall = pd.DataFrame({'測站名稱':station_data,
                            '行政區':region_data,
                            '本日累積(mm)':td,
                            '昨日累積雨量(mm)':yd_rainfall,
                            '前日累積雨量(mm)':bd_rainfall
                            })

zone = dt.timedelta(hours=8)
tw_zone = dt.timezone(zone)
tw_now = dt.datetime.now(tw_zone)
time_from = tw_now.strftime('%Y.%m.%d-%H%M')

try:
    # 建立存放資料夾，並判斷是否存在及後續處置
    path = os.getcwd()
    new_path = os.path.join(path, r'雨量資料')
    if not os.path.exists('雨量資料'):
        os.mkdir('雨量資料')
    else:
        print(f"資料夾已存在 檔案大小:{os.path.getsize(new_path)}")

    # 輸出成CSV表
    df_rainfall.to_csv(path + '/雨量資料/' + str(time_from) + ' 雨量資料.csv',  #加上時間戳記的檔名
                       encoding='utf-8-sig',  #編碼格式
                       index=False  #表頭索引值
                       )
    # 計時結束
    end = dt.datetime.now()

except Exception as e:
    print('失敗', e)
finally:
    print(f"測站數:{len(station_data)}\n測站地點筆數:{len(region_data)}")
    print(f"本日雨量值筆數:{len(td)}，最大值為:{max(td)}，最小值為:{min(td)}")
    print(f"前1日雨量值筆數:{len(yd_rainfall)}，最大值為:{max(yd_rainfall)}，最小值為:{min(yd_rainfall)}")
    print(f"前2日雨量值筆數:{len(bd_rainfall)}，最大值為:{max(bd_rainfall)}，最小值為:{min(bd_rainfall)}")
    print(f"運行時間:{end - start}")
    print('儲存完畢')