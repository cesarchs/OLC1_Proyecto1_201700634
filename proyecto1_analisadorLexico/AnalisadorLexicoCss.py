    #analisador lexico para HTML
import re
class AnalisadorLexicoCss:
    def __init__(self):
        pass
    linea = 0
    columna = 0
    counter = 0

    Errores = []
    Comentario = []

    reservadas = ['html','head','body','h1','h2', 'h3', 'h4', 'h5', 'h6', 'div', 'table', 'title', 'img', 'ol', 'ul', 'li', 'th', 'tr', 'td', 'caption', 'col', 'thead', 'tfoot', 'colgroup', 'tbody']

    signos = {"PUNTOCOMA":';', "LLAVEA":'{', "LLAVEC":'}', "PARA":'\(', "PARC":'\)', "IGUAL":'=', "diagonal":'/', "signoMayorQue":'>', "signoMenorQue":'<', "dosPuntos":':', "Arroba":'@'}
    signos2 = {"corcheteA":'\[',"corcheteC":']',"numeral":'#',"interrogacionA":'!',"porcentaje":'%',"pipe":'\|',"punto":'\.',"comillasDobles":'"',"guion":'-',"dolar":'\$'}
    comentario = { "diagonalDoble":'//',"comillasDobles":'"'}
    # hay problemas con el asterisco *
    #EXPRESIONES REGULARES PARA IMPLEMENTACIÓN DE ANÁLISIS LÉXICO

    def inic(self,text):
        global linea, columna, counter, Errores, Comentario
        linea = 1
        columna = 1
        listaTokens = []
        counter= AnalisadorLexicoCss.counter
        while counter < len(text):
            if re.search(r"[A-Za-z]", text[counter]): #CADENA
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
                #SIGNOS
                isSign = False
                for clave in AnalisadorLexicoCss.signos:
                    valor = AnalisadorLexicoCss.signos[clave]
                    if re.search(valor, text[counter]):
                        listaTokens.append([linea, columna, clave, valor.replace('\\','')])
                        counter += 1
                        columna += 1
                        isSign = True
                        break
                    else:
                        for clave2 in AnalisadorLexicoCss.signos2:
                            valor2 = AnalisadorLexicoCss.signos2[clave2]
                            if re.search(valor2, text[counter]):
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

def Reserved(TokenList):
    for token in TokenList:
        if token[2] == 'identificador':
            for reservada in AnalisadorLexicoCss.reservadas:
                palabra = r"^" + reservada + "$"
                if re.match(palabra, token[3], re.IGNORECASE):
                    token[2] = 'reservada'
                    break
nombre= 'entrada' 
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