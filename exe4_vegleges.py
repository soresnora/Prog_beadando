def exe4(string,kerdes):
    if kerdes=="pig":
        print(engtopig(string))
    if kerdes=="eng":
        print(pigtoeng(string))


def engtopig(string):
    tordel = string.split()
    mondat=''
    for i in tordel:
        szavak=i[1:]+i[0] + "ay"
        mondat+=szavak
        mondat+=' '
    valasz=str.capitalize(mondat)
    return valasz


def pigtoeng(string):
    tordel=string.split()
    mondat = ''
    for i in tordel:
        szavak=i[-3]+i[0:-3]
        mondat+=szavak
        mondat+=' '
    valasz=str.capitalize(mondat)
    return valasz

kerdes=input("Milyen nyelvre fordít? eng/ pig")
mit=input("Szöveg: ")
#The quick brown fox
#Hetay uickqay rownbay oxfay
exe4(mit,kerdes)