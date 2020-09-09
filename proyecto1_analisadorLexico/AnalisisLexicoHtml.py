#analisador lexico para HTML

#EXPRESIONES REGULARES PARA IMPLEMENTACIÓN DE ANÁLISIS LÉXICO

import re

linea = 0
columna = 0
counter = 0

Errores = []
Comentarios = []
pathh =''
reservadas = ['html','head','body','h1','h2', 'h3', 'h4', 'h5', 'h6', 'div', 'table', 'title', 'img', 'ol', 'ul', 'li', 'th', 'tr', 'td', 'caption', 'col', 'thead', 'tfoot', 'colgroup', 'tbody']

signos = {"PUNTOCOMA":';', "LLAVEA":'{', "LLAVEC":'}', "PARA":'\(', "PARC":'\)', "IGUAL":'=', "diagonal":'/', "signoMayorQue":'>', "signoMenorQue":'<', "dosPuntos":':', "Arroba":'@'}
signos2 = {"corcheteA":'\[',"corcheteC":']',"numeral":'#',"interrogacionA":'!',"porcentaje":'%',"pipe":'\|',"punto":'\.',"comillasDobles":'"',"guion":'-',"dolar":'\$'}
comentario = { "diagonalDoble":'/',"comillasDoblesxd":'"'}
 # hay problemas con el asterisco *

def inic(text):
    global linea, columna, counter, Errores,pathh
    linea = 1
    columna = 1
    listaTokens = []

    while counter < len(text):
        if re.search(r"[A-Za-z\']", text[counter]): #CADENA
            listaTokens.append(StateIdentifier(linea, columna, text, text[counter]))
        elif re.search(r"[0-9]", text[counter]): #NUMERO
            listaTokens.append(StateNumber(linea, columna, text, text[counter]))
        elif re.search(r"[\n]", text[counter]):#SALTO DE LINEA
            counter += 1
            linea += 1
            columna = 1 
        elif re.search(r"[ \t]", text[counter]):#ESPACIOS Y TABULACIONES
            counter += 1
            columna += 1 
        else:
            # SIGNOS
            isSign = False
            for clave in signos:
                valor = signos[clave]
                if re.search(valor, text[counter]):
                    listaTokens.append([linea, columna, clave, valor.replace('\\','')])
                    counter += 1
                    columna += 1
                    isSign = True
                    break
                else:
                    for clave2 in signos2:
                        valor2 = signos2[clave2]
                        if re.search(valor2, text[counter]):
                            listaTokens.append([linea, columna, clave2, valor2.replace('\\','')])
                            counter += 1
                            columna += 1
                            isSign = True
                            break
                        else: #ESTE ES PARA COMENTARIOS UNILINIEA 
                            for clave3 in comentario:
                                valor3 = comentario[clave3]
                                if re.search(valor3,text[counter]):
                                    if re.search(valor3,text[counter +1]):
                                        # Comentarios.append([linea, columna, clave3, valor3.replace('\\','')])
                                        Comentarios.append(StateComent(linea, columna, text, text[counter]))
                                        counter += 1
                                        columna += 1
                                        isSign = True
                                break 
 

            if not isSign:
                columna += 1
                Errores.append([linea, columna, text[counter]])
                counter += 1
    return listaTokens

#[linea, columna, tipo, valor]


#--------------------------------- ESTADOS---------------------------------

def StateIdentifier(line, column, text, word):
    global counter, columna
    counter += 1
    columna += 1
    if counter < len(text):
        if re.search(r"[a-zA-Z_0-9]", text[counter]):#CADENA
            return StateIdentifier(line, column, text, word + text[counter])
        else:
            return [line, column, 'Cadena', word]
            #agregar automata de identificador en el arbol, con el valor
    else:
        return [line, column, 'cadena', word]
    
def StateNumber(line, column, text, word):
    global counter, columna
    counter += 1
    columna += 1
    if counter < len(text):
        if re.search(r"[0-9]", text[counter]):#ENTERO
            return StateNumber(line, column, text, word + text[counter])
        elif re.search(r"\.", text[counter]):#DECIMAL
            return StateDecimal(line, column, text, word + text[counter])
        else:
            return [line, column, 'integer', word]
            #agregar automata de numero en el arbol, con el valor
    else:
        return [line, column, 'integer', word]

def StateDecimal(line, column, text, word):
    global counter, columna
    counter += 1
    columna += 1
    if counter < len(text):
        if re.search(r"[0-9]", text[counter]):#DECIMAL
            return StateDecimal(line, column, text, word + text[counter])
        else:
            return [line, column, 'decimal', word]
            #agregar automata de decimal en el arbol, con el valor
    else:
        return [line, column, 'decimal', word]

def StateComent (line, column, text, word):
    global counter, columna
    pattern = '//'
    counter += 1
    columna += 1
    if counter < len(text):
        if re.findall (pattern, text): #comentario unilinea
            return StateComent(line, column, text, word + text[counter])
        else:
            print ("hola")
            return [line,column,'comentarioUnilinea',word]
            


def Reserved(TokenList):
    for token in TokenList:
        if token[2] == 'identificador':
            for reservada in reservadas:
                palabra = r"^" + reservada + "$"
                if re.match(palabra, token[3], re.IGNORECASE):
                    token[2] = 'reservada'
                    break



                
nombre= 'entrada2' 
entrada = open(nombre +'.olc1')
contenido = entrada.read()
print(contenido)
tokens = inic(contenido)
Reserved(tokens)
for token in tokens:
    print(token)
print('ERRORES')
for error in Errores:
    print(error)
print ('COMENTARIOS')
for coment in Comentarios:
    print(coment) 
print ('PATH')
for pat in pathh: 
    print (pat)