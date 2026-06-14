Temp=input()
if Temp[0] in ['C']:
    F=eval(Temp[1:])*1.8+32#原来要全部字符串只要保留：
    print("F{:.2f}".format(F))
elif Temp[0] in ['F']:
    C=(eval(Temp[1:])-32)/1.8
    print("C{:.2f}".format(C))
