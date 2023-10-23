#下載字體
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/u/0/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

# 新增字體
matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')

#設定中文字型及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Taipei Sans TC Beta'    #font.sans-serif無襯線字體
plt.rcParams['axes.unicode_minus'] = False



import pandas as pd
import matplotlib
import matplotlib.pyplot as plt, matplotlib.dates as mdates

url = 'https://data.epa.gov.tw/api/v2/aqx_p_203?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=monitordate%20desc&format=CSV'
df = pd.read_csv(url)
df1 = df[['sitename', 'itemname', 'itemunit', 'concentration', 'monitordate']]


#儲存
#sig在Win10中翻譯成「具有BOM的UTF-8」，後者沒有BOM，總之有BOM的比較好。這個方式通常都可以順順利利、平平安安的匯出檔案，這也是網路上最多人推薦的用法。
df1.to_csv('松山測站各監測項目每小時濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '細懸浮微粒')
df2 = df1[condition]
df2.to_csv('松山測站每小時PM2.5濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '二氧化氮')
df3 = df1[condition]
df3.to_csv('松山測站每小時NO2濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '懸浮微粒')
df4 = df1[condition]
df4.to_csv('松山測站每小時PM濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '臭氧')
df5 = df1[condition]
df5.to_csv('松山測站每小時O3濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '一氧化碳')
df6 = df1[condition]
df6.to_csv('松山測站每小時CO濃度.csv', encoding='utf-8-sig')

condition = (df1['itemname'] == '二氧化硫')
df7 = df1[condition]
df7.to_csv('松山測站每小時SO2濃度.csv', encoding='utf-8-sig')





#繪製圖表

newdate = pd.to_datetime(date)
df['concentration']=df['concentration'].astype(float)
ax = plt.gca()
fig1 = df2[['monitordate', 'concentration']]
fig1.plot(x='monitordate', y='concentration', figsize=(18,5), marker='o', linestyle='--', ax=ax)
# fig.gca().xaxis.set_major_formatter(mdates.DateFormatter(‘%Y-%m-%d’)) #設定x軸主刻度顯示格式（日期）
# fig.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14)) #設定x軸主刻度間距
df[['monitordate', 'concentration']].plot(x='monitordate', y='concentration', figsize=(10,5), marker='o', linestyle='--', ax=ax)
