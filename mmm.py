#模組的載入
# import sys as S #又稱為的語法，具有替代性
# print(S.platform) #系統位元
# print(S.maxsize) #整數最大值
# print(S.maxunicode)
# print(S.path) #模組的搜尋路徑

# import geo #geo是你當初命名的檔案名稱
# result1=geo.D(2,7,11,5.5)
# result2=geo.S(2,7,11,5.5)
# print(result1)
# print(result2)



import sys
sys.path.append("AAA")  #請python增加此搜尋路徑
print(sys.path)

import geo
result=geo.D(4,7,150,26)
print(result)

