Temp=input()
if Temp[-1] in ['C','c']:
    F=eval(Temp[0:-1])*1.8+32#这个eval也没记下来，公式也抄错了
    print("{:.2f}F".format(F))#第一次，这里错了，没有加双引号
elif Temp[-1] in ['F','f']:
    C=(eval(Temp[0:-1])-32)/1.8
    print("{:.2f}C".format(C))#第二次，这里错了，用成了逗号，应该是点
else:
    print("输入格式错误")
