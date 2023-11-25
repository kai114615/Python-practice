#四則運算
y=float(input("請輸入數字一:"))
z=float(input("請輸入數字二:"))
#print(y*z)
op=input("請輸入四則運算+, -, *, / ^ : ")  #op為選擇指令
if op=="+":
    print(y+z)
elif op=="-":
    print(y-z)
elif op=="*":
    print(y*z)
elif op=="/":
    print(y/z)
elif op=="^":
    print(y**z)    
else:
    print("無效的運算")