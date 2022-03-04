#!python3

import json

#x = '{ "nome": "Mirco", "cognome": "Bisoffi", "eta": 22}'
x = open("prova.json")
y = json.loads(x)

print(y["eta"])

