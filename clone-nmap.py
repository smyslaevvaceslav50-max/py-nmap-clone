import socket
def ports_scan(ip_addres):
    p = []
    ports = [21, 22, 23, 25, 53, 80, 139, 443, 445]
    for i in ports:
        tup = [str(i) + "/tcp"]
        s = socket.socket()
        s.settimeout(2.0)
        result = s.connect_ex((ip_addres, i))
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
dom_ip = input()
ci = dom_ip.split(".")
if len(ci) == 4 and all(c.isdigit() and 0 <= int(c) <= 255 for c in ci):
    print("PORT STATE SERVICE")
    finall = ports_scan(dom_ip)
    for i in finall:
        print(" ".join(i))
else:
    print("PORT STATE SERVICE")
    dom_ip = socket.gethostbyname(dom_ip)
    finall = ports_scan(dom_ip)
    for i in finall:
        print(" ".join(i))
