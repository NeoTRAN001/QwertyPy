print('V and V: ', 5 < 10 and 7 < 90)
print('V or  F: ', 5 > 10 or 7 < 90)
print('not V: ', not 9 == 10)

tabla_verdad = """
_________________________________________
|           Tabla de Verdad             |
|_______________________________________|
| Valor1 | Valor2 | and  | or   | not   |
|========|========|======|======|=======|
|  True  |  True  | %s |%s  | %s |
|________|________|______|______|_______|
|  False |  True  | %s| %s | %s  |
|________|________|______|______|_______|
|  True  |  False | %s| %s | %s |
|________|________|______|______|_______|
|  False |  False | %s| %s| %s  |
|________|________|______|______|_______|
""" % (True  and True,  True  or True,  not True,
	   False and True,  False or True,  not False,
	   True  and False, True  or False, not True,
	   False and False, False or False, not False)

print(tabla_verdad)