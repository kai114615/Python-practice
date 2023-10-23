#網路連接
# import urllib.request
# src="https://www.cwb.gov.tw/V8/C/"
# with urllib.request.urlopen(src) as response:
#     data=response.read().decode("utf-8")  #取得該網站的原始碼
# print(data)

#串接、擷取公開資料
import urllib.request
import json
src="https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314"
with urllib.request.urlopen(src) as response:
    data=json.load(response)  #取得該網站的原始碼
print(data)