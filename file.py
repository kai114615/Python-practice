#儲存or寫入檔案語法1
# file=open("data.txt",mode="w",encoding="utf-8")  #開啟檔案
# file.write("hello哈囉\ntaiwan台灣")   #操作檔案，\n是換行的符號
# file.close()    #關閉檔案  
#重複執行，檔案內容被覆寫，並不會有兩個檔案



#儲存or寫入檔案語法2
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("4\n56\n7.3\n0.29")
#不需要file.close()指令的簡式語法




#讀取檔案語法
# ans=1
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:     #一行一行單獨讀取
#         ans=ans*float(line)
# #    data=file.read()
# print(ans)

#讀取json檔案
# with open("New document.json",mode="r") as file:
#     data=json.load(file)
# print(data)