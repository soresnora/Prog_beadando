def exe11():
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            sz = i*j
            if str(sz)==str(sz)[::-1]:
                palind=sz
                x1=i
                x2=j
                return '{}*{}={}'.format(x1,x2,palind)

print(exe11())