# x = 54
# y = 66.8
# z = "YEAR"
# print(x, y, z)


# 華氏攝氏轉換


c = input("請輸入攝氏溫度:")
F = int(c)*(9/5)+32
print(F)

f = input("請輸入華氏溫度:")
C = (int(f)-32)*(5/9)
# print("%.2f" % C)
print(f"換算的攝氏溫度是{C:.4f}")
