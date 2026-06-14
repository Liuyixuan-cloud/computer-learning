a=input()
m=1
if a=="0":
    print("Hello World")
elif eval(a)>0:
    for i in "Hello World":
        if m%2==0:
            print(i)
        if m%2==1:
            print(i,end="")
        m=m+1#要把这个放在这里
else:
    for i in "Hello World":#据说这里不能有""
        print(i)
