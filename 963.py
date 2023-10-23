#break 迴圈
# n=0
# while n<15:
    # if n==10:
        # break #如果是True 執行此程式碼，意謂結束迴圈
    # n=n+1
# print(n) #最終結果的n

#continue 迴圈
# n=0
# for x in [0,1,2,3,4,5,6,7]:
    # if x**2<=30:
        # continue #如果是True 執行此程式碼，意謂繼續迴圈，直到False結束迴圈
    # print(x)
    # n=n+1
# print(n)

#else 迴圈
# sum=0
# for x in range(4,14):
    # x=x/(x+1)
    # print(x)
    # sum=sum+x
# else:
    # print(sum)    

#練習
n=input("請輸入任意正整數:")
n=int(n)
x=n**(1/2)
if x//1==x:
    print("平方根為:",x)
else:
    print("沒有正整數根")

