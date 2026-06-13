shuzi="零一二三四五六七八九"#居然真的是这样表示字符串
a=input()#不能放在这里，因为要是字符串才能识别，而不是数字
for i in a:#末尾要加：
    print(shuzi[int(i)],end="")
