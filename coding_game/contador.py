_str = input('Ingresa la cadena: ')
_type = input('Ingresa el tipo: ')

vocales = 'aeiou'

_str = _str.replace(' ','').lower()

vocal = [v for v in _str if v in vocales]

if _type == 'vowels':
    print(len(vocal))
else:
    print(len(_str) - len(vocal))