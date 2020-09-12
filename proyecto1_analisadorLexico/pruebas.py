
# counter =0



# print (counter)
# counter +=1
# print (counter)

# import re

# text = "/*fadf" 
# pattern = ""

# for match in re.findall(pattern, text):
#     print("si entro")
# print ("no entro")

import re

text = '/*abba /* aabbb/*ba */ aaaa /*'


    # for palabra in text:
#         if palabra != "*":
#             palabraGuardar += palabra           
        
#     print (palabraGuardar)

# #  for tamanio in text:
# #                 palabraComentario = text[tamanio]
# #                 if palabraComentario != '\n':
# #                     word + palabraComentario
# #             return [line,column,'comentarioUnilinea',word]


nombre= 'entrada2' 
entrada = open(nombre +'.olc1')
contenido = entrada.read()
# print(contenido)

# word = ''

# for i in contenido:
#     word +=i
#     print (word)

# cesar = "cesdar"
# cesar2 = "caro"
# if cesar != "cesar" and cesar2=="caro":
#     print ('si pasa')
# else:
#     print("no pasa")
print(text[0]+text[1])
pattern = '/\*'
for match in re.findall(pattern, text[0]+text[1]):
    print(match)
    print('si entro')
    # print ('entro')

#     print('Found {!r}'.format(match))
# palabraGuardar = ''

# if re.findall(pattern, text):
#     print ('entro')

counter =0
print (counter +2)

counter -=1

print (counter)