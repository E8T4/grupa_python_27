from pip._internal.commands import index

list1=[4,5,10,20,30,100,500,999,1000]
print(len(list1)// 2)
index=len(list1)//2
print(list1[index])

list2=[0,1,2,50,100,100,100,2,2,2,9,10,99]
print(list2)
#putem schimba un element din lista folosind [] si punand indexul elementului in ele
list2[3]=100
print(list2)
#Dictionare
#ordinea este garantata de lista, nu este garanta de dictionar
persoana ={
    "key": "valoare",
    "nume": "Ovidiu",
    "inaltime": "1.85m",
    "varsta": 27,
    "cetatean_roman": True,
    "bolnav": False,
    "greutate": 75.7,
}
print(persoana)

dict2 ={'key': 'valoare', 'nume': 'Ovidiu', 'inaltime': '1.85m', 'varsta': 27, 'cetatean_roman': True, 'bolnav': False, 'greutate': 75.7}
#fast lookup
print(persoana["key"])
print(persoana["varsta"])
persoana["inaltime"]="3m"
persoana["CNP"]="23523222232"

#seturi:
#cutie de bomboane, toate diferite.
#curly brackets, squigly brackets
elemset={3,6,10,9,8,100,3}
print(elemset)
list2 = [0,1,2,50,100,100,100,100,2,2,2,9,10,99]
list2_no_duplicates=set(list2)
print(list2_no_duplicates)
#pentru un set, aceeasi actiune are 0(1)

#tuplu - odata puse elementele, nu mai pot fi schimbate. Este tot o lista dar imutabila
coordinates=(0,10)
coordinates3d=(0,15,-5)
print(coordinates[1])

#Metode
# catel ="Spot"
# catel.latra("cioara")
# catel.mananca("peste")
# catel.miroase("adrian")
# catel.musca("adrian")
#obiect.actiune / functie/metoda (parametri)

lista5=[7,8,100,99]
lista5.append(-50)
print(lista5)
lista5.pop(1)
print(lista5)
lista5.reverse()
print(lista5)

#set-urile nu au indecsi
set2={7,6,8,8,10,90,100}
set2.add(-5)
set2.remove(90)

#chei de dictionare
dict_2={
    "key": "value",
    1: "one",
    3.14: "PI",
    True:False,
    (2,3): "coordinates",

}

print("End of file")