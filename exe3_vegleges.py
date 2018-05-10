def exe3(szoveg):
    max = -1
    for m in szoveg:
        if len(m) > max:
            max = len(m)
    print((max+4)*'*')
    for k in szoveg:
        k += (max-len(k))*' '
        print("{} {} {}".format('*',k,'*'))
    print((max+4)*'*')


szov = ["Hello", "World", "in", "a", "frame"]
exe3(szov)