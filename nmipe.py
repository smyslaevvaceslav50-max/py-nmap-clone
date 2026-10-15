import json
import urllib.request
import urllib.error
import socket
d = {}
flag = True
folders = ["/admin", "/login", "/secret", "/backup.sql", "/config.json", "/.env", "/db.sqlite", "/uploads", "/images", "/robots.txt", "/api", "/dev", "/test", "/wp-admin", "/old"]
ports = ["22", "53", "80", "443", "3389"]
domen = input()
_, dom = domen.split("//")
ip = socket.gethostbyname(dom)
d["IP"] = f"IP: {ip}"
for i in folders:
    try:
        number_url = urllib.request.urlopen(domen + i)
        d[i] = f"Open! {i}(200)"
    except urllib.error.HTTPError as e:
        if e.code == 403:
            d[i] = f"Close! {i}(403)"
        else:
            d[i] = f"{i}(404)"
    except Exception:
        print("ERROR")
        flag = False
        break
for i in ports:
    s = socket.socket()
    s.settimeout(2.0)
    if s.connect_ex((ip, int(i))) == 0:
        d[i] = f"Порт открыт: {i}"
    else:
        d[i] = f"Порт закрыт: {i}"
    s.close()
if flag:
    with open("domen.json", "w", encoding="utf-8") as file:
        json.dump(d, file)
    print("Write")
    while True:
        command = input()
        if command == "open":
            with open("domen.json", encoding="utf-8") as file:
                dict1 = json.load(file)
                print("Full infa domen")
                for i in dict1:
                    print(dict1[i])
        elif command == "close":
            break
        else:
            print("WRONG COMMAND AGAIN WRITE")