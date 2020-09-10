
counter =0



print (counter)
counter +=1
print (counter)

import re

text = 'abbaaabbbbaaaaa' 
pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))



#  for tamanio in text:
#                 palabraComentario = text[tamanio]
#                 if palabraComentario != '\n':
#                     word + palabraComentario
#             return [line,column,'comentarioUnilinea',word]


nombre= 'entrada2' 
entrada = open(nombre +'.olc1')
contenido = entrada.read()
print(contenido)

word = ''

for i in contenido:
    word +=i
    print (word)