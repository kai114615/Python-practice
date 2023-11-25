#函式定義
def XY(n1,n2):
    sum=0
    for n in range(n1,n2):
        sum=sum+n
    print(sum)

XY(4,16)
XY(1,3)


#給定資料 
def avg(*ns): #加上*字表是可以無限或任意數量
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))
    
avg(2,7,0.6,4,1.5,-7,-2.64,5,6)  #用列表 
