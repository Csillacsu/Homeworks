'''
CSV olvasás-írás

1) Készíts egy csv file-t az alábbi szöveges tartalommal:

Gondűző, borocska, mellett
Vígan, illan, életem,
Gondűző, borocska, mellett,
Sors, hatalmad, nevetem,
És, mit, ámultok, ha mondom,
Hogy, csak, a, bor, istene,
Akit, én, imádok, aki,
E, kebelnek, mindene

2) Készíts egy másik csv file-t, amibe kiíratod a fenti file minden sorának 2. elemét. Az első sort ne vedd figyelembe.
'''

import csv

with open('petofi.csv', 'a', encoding="UTF-8") as pet:
    pet.write(
        "Gondűző, borocska, mellett \nVígan, illan, életem,\nGondűző, borocska, mellett,\nSors, hatalmad, nevetem,\nÉs, mit, ámultok, ha mondom, \nHogy, csak, a, bor, istene, \nAkit, én, imádok, aki,\nE, kebelnek, mindene")


with open('petofi.csv', 'r', encoding="UTF-8") as p_file:
    with open('res.csv', 'w', encoding="UTF-8") as res_file:
        next(p_file)
        file_table = csv.reader(p_file, delimiter=',')
        for row in file_table:
            res_file.write(row[1])
            res_file.write("\n")
