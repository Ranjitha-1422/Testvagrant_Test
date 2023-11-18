def func(GST):
    res = max(GST)
    return res
def shopping(tup):
    for i in tup:
        if i==1:
            up = 1100
            quan = 1
        elif i==2:
            up = 900
            quan = 3
        elif i==3:
            up = 200
            quan = 3
        else:
            up = 100
            quan = 2
        lst = []
        lst.append(up)
        for i in lst:
            if i>=500:
                Amnt = (5/100)*quan
    return Amnt
GST = [18,12,28,0]
Max_gst = func(GST)
print(Max_gst)
tup = [wal,umb,cig,hon]
Total_amnt = shopping(tup)
print(Total_amnt)
