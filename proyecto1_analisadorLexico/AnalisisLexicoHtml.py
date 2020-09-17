#analisador lexico para HTML

#EXPRESIONES REGULARES PARA IMPLEMENTACIÓN DE ANÁLISIS LÉXICO

import re

class AnalisisLexicoHtml:
    def __init__(self):
        pass
    linea = 0
    columna = 0
    counter = 0

    Errores = []
    Comentarios = []
    pathh =''
    recorrido =[]
    reservadas = ['html','head','body','h1','h2', 'h3', 'h4', 'h5', 'h6', 'div', 'table', 'title', 'img', 'ol', 'ul', 'li', 'th', 'tr', 'td', 'caption', 'col', 'thead', 'tfoot', 'colgroup', 'tbody','alt']
    signos = {"PUNTOCOMA":';', "LLAVEA":'{', "LLAVEC":'}', "PARA":'\(', "PARC":'\)', "IGUAL":'=', "diagonal":'/', "signoMayorQue":'>', "signoMenorQue":'<', "dosPuntos":':'}
    signos2 = {"corcheteA":'\[',"corcheteC":']',"admiracion":'!',"porcentaje":'%',"pipe":'\|',"punto":'\.',"comillasDobles":'"',"guion":'-'}
    comentario = { "diagonalDoble":'/',"comillasDoblesxd":'"'}
     # hay problemas con el asterisco *

    def inic(self, text):
        global linea, columna, counter, Errores,pathh
        linea = 1
        columna = 1
        listaTokens = []
        counter = AnalisisLexicoHtml.counter
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
                isSign = False
                for clave in AnalisisLexicoHtml.signos:
                    valor = AnalisisLexicoHtml.signos[clave]
                    if re.search(valor, text[counter]):
                        listaTokens.append([linea, columna, clave, valor.replace('\\','')])
                        counter += 1
                        columna += 1
                        isSign = True
                        break
                    else:
                        for clave2 in AnalisisLexicoHtml.signos2:
                            valor2 = AnalisisLexicoHtml.signos2[clave2]
                            if re.search(valor2, text[counter]):
                                listaTokens.append([linea, columna, clave2, valor2.replace('\\','')])
                                counter += 1
                                columna += 1
                                isSign = True
                                break
                            
                            else: #ESTE ES PARA COMENTARIOS UNILINIEA 
                                for clave3 in AnalisisLexicoHtml.comentario:
                                    valor3 = AnalisisLexicoHtml.comentario[clave3]
                                    if re.search(valor3, text[counter]):
                                        if re.search(valor3, text[counter +1]):
                                            AnalisisLexicoHtml.Comentarios.append(StateComent(linea, columna, text, ''))
                                            counter += 1
                                            columna += 1
                                            isSign = True
                                    break 
                                

                if not isSign:
                    columna += 1
                    AnalisisLexicoHtml.Errores.append([linea, columna, text[counter]])
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
    palabraContador =counter
    palabraContador = palabraContador + 1
    if counter < len(text):
        if re.findall (pattern, text): #comentario unilinea
            if text[palabraContador]!= "\n": #se recorre el texto siguiente al // para guardar todo el comentario
                return StateComent(line, column, text, word + text[palabraContador])
            else:
                return [line,column,'comentarioUnilinea',word]
        else:
            return [line,column,'comentarioUnilinea',word]
        
            


def Reserved(TokenList):
    for token in TokenList:
        if token[2] == 'Cadena':
            for reservada in AnalisisLexicoHtml.reservadas:
                palabra = r"^" + reservada + "$"
                if re.match(palabra, token[3], re.IGNORECASE):
                    token[2] = 'reservada'
                    break
                
# nombre= 'entrada.html' 
# entrada = open(nombre)
# contenido = entrada.read()
# print(contenido)
# tokens = AnalisisLexicoHtml().inic(contenido)
# Reserved(tokens)
# for token in tokens:
#     print(token)
# print('ERRORES')
# for error in AnalisisLexicoHtml.Errores:
#     print(error)
# print ('COMENTARIOS')
# for coment in AnalisisLexicoHtml.Comentarios:
#     print(coment) 
# print ('PATH')
# pathh= AnalisisLexicoHtml.Comentarios[0]
# pathh[3]
# print (pathh[3].replace('PATHW:',' '))