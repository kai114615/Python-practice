#BMI值計算
# weight = float(input("請輸入體重(KG):"))
# high = int(input("請輸入身高(CM):"))
# BMI = weight/(high/100)**2
# print(f"妳的BMI值為{BMI:.2f}")



#判別奇偶數
# n = int(input("請輸入一個正整數:"))
# if n%2 ==0:
#     print(f"{n}是偶數")
# else:
#     print(f"{n}是奇數")

#判斷是否為閏年
year = int(input("請輸入西元年份:"))
if year%100 == 0 and year%400 == 0:
    print(f"西元{year}是閏年")
elif year%100 != 0 and year%4 == 0:
    print(f"西元{year}是閏年")
else:
    print(f"西元{year}不是潤年")