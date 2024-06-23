import requests
import json
import os
import datetime as dt
import pandas as pd

zone = dt.timedelta(hours=8)
tw_zone = dt.timezone(zone)
tw_now = dt.datetime.now(tw_zone)
day_from = tw_now.strftime('%Y.%m.%d')
time_from = tw_now.strftime('%H%M')

try:
    url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=rdec-key-123-45678-011121314'
    r = requests.get(url)
    data_json = r.json()
    cdj = data_json['records']['Station']
except Exception as e:
    print(e)

# 建立雨量總表資料串列
data_list = []
obt_list = []


try:
    for i in cdj:
        county_town = i['GeoInfo']['CountyName']+i['GeoInfo']['TownName']
        station_name = i['StationName']
        id = i['StationId']
        now_rainfall = float(i['RainfallElement']['Now']['Precipitation'])
        yd_rainfall = float(i['RainfallElement']['Past2days']
                            ['Precipitation']-now_rainfall)
        bd_rainfall = float(i['RainfallElement']['Past3days']['Precipitation'] - i['RainfallElement']['Past2days']['Precipitation'])
        obstime = i['ObsTime']['DateTime'][:10] + str(' ')+i['ObsTime']['DateTime'][11:16]

        data = {
            '行政區': county_town,
            '測站名稱': station_name,
            '測站代碼': id,
            '截至目前累積雨量': now_rainfall,
            '昨日累積雨量': yd_rainfall,
            '前日累積雨量': bd_rainfall
        }
        data_list.append(data)  # 爬下來的雨量站裝入雨量總表的[]中
    obt = {'資料時間': obstime}
except Exception as e:
    print(e)

try:
    # 局本部重點監控路段參考雨量站清單
    thb_id_list = ['466940',  # 基隆
                   'C0A930',  # 三和
                   'C0A530',  # 坪林
                   'C0U760',  # 東澳
                   'C1U840',  # 東澳嶺
                   'C0S790',  # 金崙
                   'C0A570',  # 桶後
                   '21C070',  # 巴陵
                   '21U110',  # 池端
                   '81F860',  # 松茂
                   'C0U720',  # 南山
                   'C1F9W0',  # 德基
                   'C0F860',  # 梨山
                   'C1T810',  # 慈恩
                   'C0I010',  # 廬山
                   'A0Z080',  # 合歡山
                   '467530',  # 阿里山
                   'C2V250',  # 甲仙
                   'C0S750',  # 向陽
                   'C0H9A0',  # 神木村
                   '81V830',  # 那瑪夏國中
                   'C0T9H0',  # 加路蘭山
                   'C0T9I0'  # 豐濱
                   ]

    thb_rfdata = []  # 建立局本部雨量校驗表資料串列
    for i in range(len(thb_id_list)):
        for data in data_list:
            if data['測站代碼'] == thb_id_list[i]:
                thb_rfdata.append(data)

except Exception as e:
    print(e)

try:
    # 北分局重點監控路段參考雨量站清單
    thb_north_id_list = ['L1A820',  # 石碇(十三股)
                         'C0A530',  # 坪林-碧湖(坪林)
                         'C0A930',  # 金山(三和)
                         'C0B010',  # 七堵(現場監測)
                         '466940',  # 碧砂漁港(基隆)
                         'C0A950',  # 瑞濱-鼻頭(鼻頭角)
                         'C0A970',  # 貢寮卯澳(三貂角)
                         'C0A890',  # 龍門橋(雙溪)
                         'C0AC60',  # 三峽(三峽)
                         'C0A570',  # 烏來(桶後)
                         '01C570',  # 桃園迴龍-龜山(龍壽社區)
                         '21C080',  # 羅浮-巴陵(高義)
                         '21C070',  # 巴陵-西村(巴陵)
                         '01A210',  # 新峰(大豹)
                         'C0AD10',  # 八里(八里)
                         'C0C590',  # 觀音(觀音)
                         '01C400',  # 溪州(石門後池)
                         'C0D700',  # 關西(關西)
                         ]

    thb_north_rfdata = []  # 建立北分局雨量校驗表資料串列
    for i in range(len(thb_north_id_list)):
        for data in data_list:
            if data['測站代碼'] == thb_north_id_list[i]:
                thb_north_rfdata.append(data)
except Exception as e:
    print(e)

try:
    # 東分局重點監控路段參考雨量站清單
    thb_east_id_list = ['C1U840',  # 東澳嶺
                        'C0U760',  # 東澳
                        'C0UA60',  # 樟樹山
                        'C1U850',  # 觀音海岸
                        'C0T9D0',  # 和中
                        'C0Z310',  # 清水斷崖
                        'C0T790',  # 大禹嶺
                        'C1T810',  # 慈恩
                        'C1T830',  # 布洛灣
                        'C1S850',  # 豐南
                        '21U110',  # 池端
                        '01U060',  # 梵梵(2)
                        'C1U500',  # 牛鬥
                        'C0U720',  # 南山
                        'C1U920',  # 思源
                        'C0U520',  # 雙連埤
                        'C0T9H0',  # 加路蘭山
                        'C0T9I0'  # 豐濱
                        ]

    thb_east_rfdata = []  # 建立北分局雨量校驗表資料串列
    for i in range(len(thb_east_id_list)):
        for data in data_list:
            if data['測站代碼'] == thb_east_id_list[i]:
                thb_east_rfdata.append(data)
except Exception as e:
    print(e)

# 將各雨量資料表存於各df{}中
df = pd.DataFrame(data_list)
thb_rf_df = pd.DataFrame(thb_rfdata)
thb_north_rf_df = pd.DataFrame(thb_north_rfdata)
thb_east_rf_df = pd.DataFrame(thb_east_rfdata)

# 總雨量表依"昨日累積雨量"欄位由大至小排序
sort_df = df.sort_values(['昨日累積雨量'], ascending=False)

try:
    # 建立存放資料夾，並判斷是否存在及後續處置
    path = os.getcwd()
    if not os.path.exists(str(day_from) + ' 雨量資料'):
        os.mkdir(str(day_from) + ' 雨量資料')
    else:
        print(f"資料夾已存在")

    # 輸出成各CSV雨量表
    sort_df.to_csv(path + '/' + str(day_from) + ' 雨量資料/' + str(time_from) + ' 雨量總表.csv',  # 加上時間戳記的檔名
                   encoding='utf-8-sig',  # 編碼格式
                   index=False  # 表頭索引值
                   )
    thb_rf_df.to_csv(path + '/' + str(day_from) + ' 雨量資料/' + str(time_from) + ' 局本部重點監控路段雨量.csv',  # 加上時間戳記的檔名
                     encoding='utf-8-sig',  # 編碼格式
                     index=False  # 表頭索引值
                     )
    thb_north_rf_df.to_csv(path + '/' + str(day_from) + ' 雨量資料/' + str(time_from) + ' 北分局重點監控路段雨量.csv',  # 加上時間戳記的檔名
                           encoding='utf-8-sig',  # 編碼格式
                           index=False  # 表頭索引值
                           )
    thb_east_rf_df.to_csv(path + '/' + str(day_from) + ' 雨量資料/' + str(time_from) + ' 東分局重點監控路段雨量.csv',  # 加上時間戳記的檔名
                          encoding='utf-8-sig',  # 編碼格式
                          index=False  # 表頭索引值
                          )
except Exception as e:
    print('失敗', e)
finally:
    print(f"總測站數:{len(sort_df)} 局本部測站數:{len(thb_rf_df)}/{len(thb_id_list)} 北分局測站數:{len(thb_north_rf_df)}/{len(thb_north_id_list)} 東分局測站數:{len(thb_east_rf_df)}/{len(thb_east_id_list)}")
    print(f"總雨量表 累積雨量 本日最大值:{max(sort_df['截至目前累積雨量'])} 最小值:{min(sort_df['截至目前累積雨量'])}")
    print('-'*50)
    print(f"局本部 累積雨量 本日最大值:{max(thb_rf_df['截至目前累積雨量'])} 昨日最大值:{max(thb_rf_df['昨日累積雨量'])} 前日最大值:{max(thb_rf_df['前日累積雨量'])}")
    print(f"北分局 累積雨量 本日最大值:{max(thb_north_rf_df['截至目前累積雨量'])} 昨日最大值:{max(thb_north_rf_df['昨日累積雨量'])} 前日最大值:{max(thb_north_rf_df['前日累積雨量'])}")
    print(f"東分局 累積雨量 本日最大值:{max(thb_east_rf_df['截至目前累積雨量'])} 昨日最大值:{max(thb_east_rf_df['昨日累積雨量'])} 前日最大值:{max(thb_east_rf_df['前日累積雨量'])}")
    print('-'*50)

input('按Enter鍵退出程式')
