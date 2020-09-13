#analisador lexico para HTML
import re
class AnalisadorLexicoCss:
    def __init__(self):
        pass
    linea = 0
    columna = 0
    counter = 0
    Errores = []
    Comentarios = []
    Bitacora = []

    reservadas = ['color','font','size','background','margin','top','bottom','text','align','position','hover','before','after','container','header','content',
                    'border','weight','padding','left','line','height','opacity','family','right','width','image','style','display','margin','float','clear','max','min',
                    'px','em','vh','vw','in','cm','mm','pt','pc','url','content']
    signos = {"PUNTOCOMA":';', "LLAVEA":'{', "LLAVEC":'}', "ParA":'\(', "ParC":'\)', "IGUAL":'=', "diagonal":'/', "dosPuntos":':', "asterisco":'\*'}
    signos2 = {"numeral":'#',"admiracion":'!',"porcentaje":'%',"pipe":'\|',"punto":'\.',"comillasDobles":'"',"guionMedio":'-', "coma":',',"gionBajo":'_'}
    comentario = { "diagonalDoble":'/',"comillasDoblesxd":'"'}
    #EXPRESIONES REGULARES PARA IMPLEMENTACIÓN DE ANÁLISIS LÉXICO

    def inic(self,text):
        global linea, columna, counter, Errores, Comentario
        linea = 1
        columna = 1
        listaTokens = []
        counter= AnalisadorLexicoCss.counter
        while counter < len(text):
            if text[counter]=='u' and text[counter+1]=='r' and text[counter+2]=='l':
                listaTokens.append(StateIdentifier(linea, columna, text, text[counter]))
                counter += 4
                listaTokens.append(StateUrl(linea, columna, text, ''))
                counter += 1
                columna += 1   
            elif re.search(r"[A-Za-z']", text[counter]): #CADENA
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
            elif text[counter]=='/' and text[counter+1]=='*':
                counter += 1
                AnalisadorLexicoCss.Comentarios.append(StateComent(linea, columna, text, ''))
                counter += 1
                columna += 1 
            else:
                #SIGNOS
                isSign = False
                for clave in AnalisadorLexicoCss.signos:
                    valor = AnalisadorLexicoCss.signos[clave]
                    if re.search(valor, text[counter]):
                        AnalisadorLexicoCss.Bitacora.append(['ESTADO SIGNO ',linea, columna, text[counter]]) #aca llenamos el vector de bitacora
                        listaTokens.append([linea, columna, clave, valor.replace('\\','')])
                        counter += 1
                        columna += 1
                        isSign = True
                        break
                    else:
                        for clave2 in AnalisadorLexicoCss.signos2:
                            valor2 = AnalisadorLexicoCss.signos2[clave2]
                            if re.search(valor2, text[counter]):
                                AnalisadorLexicoCss.Bitacora.append(['ESTADO SIGNO ',linea, columna,text[counter]]) #aca llenamos el vector de bitacora
                                listaTokens.append([linea, columna, clave2, valor2.replace('\\','')])
                                counter += 1
                                columna += 1
                                isSign = True
                                break

                if not isSign:
                    columna += 1
                    AnalisadorLexicoCss.Errores.append([linea, columna, text[counter]])
                    counter += 1
        return listaTokens

#[linea, columna, tipo, valor]

def StateIdentifier(line, column, text, word):
    global counter, columna
    counter += 1
    columna += 1
    if counter < len(text):
        if re.search(r"[a-zA-Z_0-9]", text[counter]):#CADENA
            return StateIdentifier(line, column, text, word + text[counter])
        else:
            AnalisadorLexicoCss.Bitacora.append(['ESTADO IDENTIFICADOR ',line, column, word]) #aca llenamos el vector de bitacora 
            return [line, column, 'Cadena', word]
            #agregar automata de identificador en el arbol, con el valor
    else:
        AnalisadorLexicoCss.Bitacora.append(['ESTADO IDENTIFICADOR ',line, column, word])#aca llenamos el vector de bitacora
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
            AnalisadorLexicoCss.Bitacora.append(['ESTADO NUMERO ENTERO',line, column, word])#aca llenamos el vector de biacora 
            return [line, column, 'integer', word]
            #agregar automata de numero en el arbol, con el valor
    else:
        AnalisadorLexicoCss.Bitacora.append(['ESTADO NUMERO ENTERO',line, column, word])#aca llenamos el vector de biacora 
        return [line, column, 'integer', word]

def StateDecimal(line, column, text, word):
    global counter, columna
    counter += 1
    columna += 1
    if counter < len(text):
        if re.search(r"[0-9]", text[counter]):#DECIMAL
            return StateDecimal(line, column, text, word + text[counter])
        else:
            AnalisadorLexicoCss.Bitacora.append(['ESTADO NUMERO DECIMAL ',line, column, word])#aca llenamos el vector de bitacora 
            return [line, column, 'decimal', word]
            #agregar automata de decimal en el arbol, con el valor
    else:
        AnalisadorLexicoCss.Bitacora.append(['ESTADO NUMERO DECIMAL ',line, column, word])#aca llenamos el vector de bitacora 
        return [line, column, 'decimal', word]

#si en el comentario no viene el cierre muere el programa, y si viene de ultimo
#tiene que venir al menos un espacio para la comprovacion que ahi termina el comentario 
def StateComent (line,column, text, word ):
    global counter, columna, linea
    pattern = '/\*'
    counter += 1
    # columna += 1 
    if counter < len(text):
        for match in re.findall (pattern, text):
            clave = text[counter] 
            clave2 = text[counter+1]
            if clave != '*' or clave2 != '/': # el delimitador para el comentario es solo el * (no el conjunto de */)
                if clave =="\n":
                    linea+=1
                    return StateComent(line, column, text, word + ' ')
                    
                else:
                    return StateComent(line, column, text, word + text[counter])
            else:
                AnalisadorLexicoCss.Bitacora.append(['ESTADO COMENTARIO ',line, column, word]) #aca llenamos el vector de bitacora
                return [line,column,'comentario',word]

def StateUrl (line,column, text, word ):
    global counter, columna, linea
    pattern = 'url'
    counter += 1
    columna += 1 
    if counter < len(text):
        for match in re.findall (pattern, text):
            clave = text[counter] 
            clave2 = text[counter+1]
            if clave != '"' or clave2 != ')': # el delimitador para el comentario es solo el * (no el conjunto de */)
                if clave =="\n":
                    linea+=1
                    return StateUrl(line, column, text, word + ' ')               
                else:
                    return StateUrl(line, column, text, word + text[counter])
            else:
                AnalisadorLexicoCss.Bitacora.append(['ESTADO URL ',line, column, word])#aca llenamos el vector de bitacora
                return [line,column,'URL',word]

def Reserved(TokenList):
    for token in TokenList:
        if token[2] == 'identificador':
            for reservada in AnalisadorLexicoCss.reservadas:
                palabra = r"^" + reservada + "$"
                if re.match(palabra, token[3], re.IGNORECASE):
                    token[2] = 'reservada'
                    break


nombre= 'entrada3' 
entrada = open(nombre +'.olc1')
contenido = entrada.read()
print(contenido)
hola= AnalisadorLexicoCss()
tokens = AnalisadorLexicoCss().inic(contenido)
Reserved(tokens)
for token in tokens:
    print(token)
print('ERRORES')
for error in AnalisadorLexicoCss.Errores:
    print(error)
print ('COMENTARIOS')
for coment in AnalisadorLexicoCss.Comentarios:
    print(coment) 
# print ('PATH')
# for pat in pathh: 
#     print (pat)
print ('BITACORA')
for bita in AnalisadorLexicoCss.Bitacora:
    print (bita)