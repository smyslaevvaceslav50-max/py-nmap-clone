import socket
def ports_scan(comman):
    p = []
    ports = [int(i) for i in comman[1:-1]]
    for i in ports:
        tup = [str(i) + "/tcp"]
        s = socket.socket()
        s.settimeout(2.0)
        result = s.connect_ex((comman[-1], i))
        if result == 0:
            tup.append("open")
        elif result == 111 or result == 10061:
            tup.append("closed")
        else:
            tup.append("filtered")
        s.close()
        tup.append(socket.getservbyport(i, "tcp"))
        p.append(tup)
    return p
while True:
    comand = input().split()
    if comand == ["close"]:
        break
    ci = comand[-1].split(".")
    if len(ci) == 4 and all(c.isdigit() and 0 <= int(c) <= 255 for c in ci):
        print("PORT".ljust(10), "STATE".ljust(10), "SERVICE".ljust(10), sep="")
        finall = ports_scan(comand)
        stroka = []
        for i in finall:
            aii = ""
            for s in i:
                aii += s.ljust(10)
            stroka.append(aii)
        print("\n".join(stroka))
    else:
        print("PORT".ljust(10), "STATE".ljust(10), "SERVICE".ljust(10), sep="")
        d = socket.gethostbyname(comand[-1])
        comand[-1] = d
        finall = ports_scan(comand)
        stroka = []
        for i in finall:
            aii = ""
            for s in i:
                aii += s.ljust(10)
            stroka.append(aii)
        print("\n".join(stroka))
