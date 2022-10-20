_str = input('Ingresa la cadena: ')
_type = input('Ingresa el tipo: ')

vocales = 'aeiou'
contarv = 0
contaro = 0

_str = _str.lower()
_str = _str.replace(' ','')

for v in _str:
    if v in vocales and _type == 'vowels':
        contarv += 1
    elif v not in vocales: 
        contaro += 1


if _type == 'vowels':
    print(contarv)
else:
    print(contaro)
