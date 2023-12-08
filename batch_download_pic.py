import os
import requests
import time

path = os.getcwd()
# path = os.chdir('指定的路徑')

local_year = time.strftime("%Y", time.localtime())
local_month = time.strftime("%m", time.localtime())
local_day = time.strftime("%d", time.localtime())

#設定下載的年份與月份
download_year = str(input('請輸入西元年:')) #請自行設定
download_month = str(input('請輸入月份(2月=02):'))  #請自行設定
download_day = int(input('請輸入下載天數或至幾號:')) #有幾天，亦請自行設定

if not os.path.exists(str(download_month) + '月CWB每日雨量'):
    os.mkdir(str(download_month) + '月CWB每日雨量')
else:
    print(f"資料夾已存在，圖片將存入中")

try:
    for i in range(1,download_day+1): #設定下載幾張
        pic_list = requests.get(f"http://140.137.32.27/cat/rain24/{download_year}/{download_month}/{download_year}{download_month}{i:02}_2400.cwbrain.rainda2.jpg")  #下載圖片之網址
        with open(path + '/' + str(download_month) + '月CWB每日雨量/' + str(download_year) + str(download_month) + f'{i:02}' + '.png', 'wb') as f:  #圖片檔名及類型設定
            f.write(pic_list.content)
except Exception as e:
    print('下載錯誤', e)
finally:
    print("下載完畢")
    print(f"圖片張數:{i}張")
