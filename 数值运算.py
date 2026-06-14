a=input()
b=0
m=0
n=0
h=0
p=0
for i in a:
    if i=="+":
        h=1
    elif i=="-":
        h=2
    elif i=="*":
        h=3
    elif i=="/":
        h=4
    else:
        if b==0:
            if i==" ":
                b=1
            else:
                m=m*10+eval(i)
        else:
            if i==" ":
                continue
            else:
                n=n*10+eval(i)
if h==1:
    p=m+n
elif h==2:
    p=m-n
elif h==3:
    p=m*n
else:
    p=m/n
print("{:.2f}".format(p))#这个错了好多
s = input()
print("{:.2f}".format(eval(s)))
