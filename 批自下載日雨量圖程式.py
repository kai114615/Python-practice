import os
import requests
import time

path = os.getcwd()
# path = os.chdir(rf'D:/台灣整合/各駐點資料/111~112年度 公路總局/')

local_year = time.strftime("%Y", time.localtime())
local_month = time.strftime("%m", time.localtime())
local_day = time.strftime("%d", time.localtime())

#設定下載的年份與月份
download_year = str(input('請輸入西元年(2003-現在):')) #請自行設定
download_month = str(input('請輸入月份(2月=02):'))  #請自行設定
download_day = int(input('請輸入下載天數或至幾號:')) #有幾天，亦請自行設定

# 自訂下載函式
def download_files(download_year, download_month, download_day):
    for i in range(1,download_day+1): #設定下載幾張
            pic_list = requests.get(f"http://140.137.32.27/cat/rain24/{download_year}/{download_month}/{download_year}{download_month}{i:02}_2400.cwbrain.rainda2.jpg")  #下載圖片之網址
            with open(str(download_month) + '月CWA每日雨量/' + str(download_year) + str(download_month) + f'{i:02}' + '.png', 'wb') as f:  #圖片檔名及類型設定
                f.write(pic_list.content)

# 自訂顯示狀態
def shown_files():
    print(f"資料夾已存在")
    print('檔案內容有:', os.listdir(str(download_month) + '月CWA每日雨量'))

# 自訂完成狀態
def finish_status():
    print("下載完畢")
    print(f"圖片張數:{len(os.listdir(str(download_month) + '月CWA每日雨量'))}張")



if os.path.exists(str(download_month) + '月CWA每日雨量'):
    if len(os.listdir(str(download_month) + '月CWA每日雨量')) >= int(download_day):
        shown_files()
    else:
        if str('Y') == str(input('是否要覆蓋檔案? Y or N:')):
            try:
                download_files(download_year, download_month, download_day)
            except Exception as e:
                print('下載錯誤', e)
            finish_status()
        else:
            shown_files()

else:
    os.mkdir(str(download_month) + '月CWA每日雨量')

    try:
        download_files(download_year, download_month, download_day)
    except Exception as e:
        print('下載錯誤', e)

    finish_status()
    
input('按Enter鍵退出程式')
