var1=["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]
var2=["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached-WR:87"]
var3=var1+var2
ERR="ERROR"
INF="INFO"
WRN="WARNING"
# for elem in var3:
#     print(elem.split())
#     #mesaj1=(elem.split("-")[0]) #cum facusem initial cu slice, 0:1 printa si parantezele, asa cu index a apelat direct doar elementul
#
#     mesaj2=(elem.split("-" or ":")[1:2] )#and elem.split(":")[1:2])
#     cod=elem.split(":")[-1]
#     print(f"{mesaj1}")
#     print("Mesaj:", mesaj2)
#     print("Cod:", cod)

for s in var3:
    tip=s.split("-")[0]
    #daca pun tip=s.split("-")[0:1] dispare complet, ERR si restul, de ce?
    #anterior, cand am facut slice a redat valoarea cu [], am crezut ca va fi la fel...
    if tip=="ERR":
        print("ERROR")
    elif tip=="INF":
        print("INF0")
    elif tip=="WRN":
        print("WARNING")
    # print(f"Mesaj: {s.split("-")[1]}")
    print(f"Mesaj:", s.split("-")[1])
    #s este string
    print(f"Cod: {s.split("-")[2].split(":")[1]}\n")