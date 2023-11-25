#隨機模組
#隨機選取
# import random
# data=random.choice([2,7,5,9,14,0.4,55,21,7])
# print(data)

# #抽樣多筆
# import random
# data=random.sample([2,7,5,9,14,0.4,55,21,7],3)
# print(data)

# import random
# data=random.uniform(2.2,3.5)   #2.2~3.5之間的隨機亂數
# print(data)

#常態分布之隨機亂數(平均147，標準差16)
# import random
# data=int(random.normalvariate(147,2))
# print(data)

#統計模組
import statistics

data=statistics.mean([14,29,33,14,25,17,16,3,97])  #計算平均數
print(data)
print(format(data,'.3f'))   #顯示至小數點後3位數

data=statistics.median([14,29,33,14,25,17,16,3,97])  #計算中位數
print(data)

data=statistics.stdev([14,29,33,14,25,17,16,3,97])  #計算標準差
print(format(data,'.2f'))