#while 迴圈
#n=1
#while n<=77777:
#    print(n)
#    n=3*n

#for 迴圈
x=1
sum=0
for x in range(1,10):   # range(1,10) 與 [1,2,3,4,5,6,7,8,9] 相同
    x=(x+1)/(x**2)
    sum=sum+x           #n代1、n代2、n代3 .....到n代9的結果加總
    print(x)
print(sum)
