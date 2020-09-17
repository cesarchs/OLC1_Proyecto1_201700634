import re
class AnalisisLexicoCalcu:
    def __init__(self):
        pass
    linea = 0
    columna = 0 
    counter = 0 
    tokens = []
    ErroresLex = []
    signos ={"parentesisA":'\(',"parentesisC":'\)',"suma":'\+',"resta":'\-',"multiplicacion":'\*',"divicion":'/',"aceptacion":'\#'}

    def inicio (self, text):
        global linea,columna, counter
        linea =1
        columna = 1
        listaTokens = []
        counter= AnalisisLexicoCalcu.counter
        while counter < len(text):
                
            if re.search(r"[0-9]",text[counter]):
                listaTokens.append(StateNumber(linea,columna,text,text[counter]))

            elif re.search(r"[\n]", text[counter]):#SALTO DE LINEA
                counter += 1
                linea += 1
                columna = 1 

            elif re.search(r"[ \t]", text[counter]):#ESPACIOS Y TABULACIONES
                counter += 1
                columna += 1 

            else:
                Signo = False
                for clave in AnalisisLexicoCalcu.signos:
                    valor = AnalisisLexicoCalcu.signos[clave]
                    if re.search(valor, text[counter]):
                        listaTokens.append([linea, columna, clave, valor.replace('\\','')])
                        counter += 1
                        columna += 1
                        Signo = True
                        break

                if not Signo:
                    columna += 1
                    AnalisisLexicoCalcu.ErroresLex.append([linea,columna,text[counter]])
                    counter += 1
        return listaTokens

#---------------------------- ESTADOS ------------------------

def StateNumber (line,column,text, dato):
    global counter, columna
    counter +=1
    columna +=1
    if counter < len(text):
        if re.search(r"[0-9]",text[counter]):
            return StateNumber(line,column,text, dato + text[counter])
        else:
            return[line,column,"numero",dato]
    else:
        return[line,column,"numero", dato]



#---------------------sintactico -------------------------------

class AnalisisSintactico:
    def __init__(self):
        pass
    Carro = 0
    CarroToken = ''
    ListaEntrada =[]

    def parseador (self, listaEntrada2):
        global Carro,CarroToken
        listaEntrada = listaEntrada2
        CarroToken = listaEntrada[0]
        carro=0
        E 

def E():
    global CarroToken,Carro
    T
    EP 
def EP():
    global CarroToken,Carro
    if CarroToken[2]== 'suma':
        emparejar('suma')
        T 
        EP 
    elif CarroToken[2]== 'resta':
        emparejar ('resta')
        T 
        EP 
def T():
    global CarroToken,Carro
    F 
    TP 
def TP():
    global CarroToken,Carro
    if CarroToken[2]=='multiplicacion':
        emparejar('multiplicacion')
        F 
        TP 
    elif CarroToken[2]=='divicion':
        emparejar('divicion')
        F 
        TP 
def F():
    global CarroToken,Carro
    if CarroToken[2]=='parentesisA':
        emparejar('parentesisA')
        E
        emparejar('parentesisC')
    else:
        emparejar('numero')
def emparejar (tipo):
    global CarroToken,Carro
    if tipo == CarroToken[2]:
        print ('error se esperaba otro simbolo')
    if CarroToken[2] != 'ultimo':
        AnalisisSintactico.Carro +=1



# nombre= 'entrada6' 
# entrada = open(nombre +'.olc1')
# contenido = entrada.read()
# print(contenido)
# hola= AnalisisLexicoCalcu()
# tokens = AnalisisLexicoCalcu().inicio(contenido)
# # Reserved(tokens)
# hola2 = AnalisisSintactico()
# hola2.parseador(tokens)

# for token in tokens:
#     print(token)
# print('ERRORES')
# for error in AnalisisLexicoCalcu.ErroresLex:
#     print(error)









##################################################################################
#[linea, columna, tipo, valor]
import re

class AnalisadorLexico:
    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.counter = 0

        self.Errores = []

        self.signos = {"MAS":'\+',"MENOS":'\-', "POR":'\*',"DIV":'/', "PARA":'\(', "PARC":'\)'}

    def inic(self, text):
        self.linea = 1
        self.columna = 1
        listaTokens = []

        while self.counter < len(text):
            if re.search(r"[0-9]", text[self.counter]): #NUMERO
                listaTokens.append(self.StateNumber(self.linea, self.columna, text, text[self.counter]))
            elif re.search(r"[\n]", text[self.counter]):#SALTO DE LINEA
                self.counter += 1
                self.linea += 1
                self.columna = 1 
            elif re.search(r"[ \t]", text[self.counter]):#ESPACIOS Y TABULACIONES
                self.counter += 1
                self.columna += 1 
            else:
                #SIGNOS
                isSign = False
                for clave in self.signos:
                    valor = self.signos[clave]
                    if re.search(valor, text[self.counter]):
                        listaTokens.append([self.linea, self.columna, clave, valor.replace('\\','')])
                        self.counter += 1
                        self.columna += 1
                        isSign = True
                        break
                if not isSign:
                    self.columna += 1
                    self.Errores.append([self.linea, self.columna, text[self.counter]])
                    self.counter += 1
        return listaTokens



    
    def StateNumber(self, line, column, text, word):
        self.counter += 1
        self.columna += 1
        if self.counter < len(text):
            if re.search(r"[0-9]", text[self.counter]):#ENTERO
                return self.StateNumber(line, column, text, word + text[self.counter])
            else:
                return [line, column, 'NUMERIC', word]
        else:
            return [line, column, 'NUMERIC', word]

    def analisarM(self, entrada):
        tokens = self.inic(entrada)
        return tokens
##############################################################################
#-------------------------------analisis sintactico---------------------------------------
class sintac:
    def __init__(self):
        self.counter = 0
        self.tabla = { 
            'E' : { 'PARA' : "XT", 'NUMERIC' : "XT" }, 
            'X' : { 'MAS' : "XT+", 'PARC' : None, '$' : None }, #X = E
            'T' : { 'PARA' : "ZF", 'NUMERIC' : "ZF" },
            'Z' : { 'POR' : "ZF*", 'MAS' : None, 'PARC' : None, '$' : None }, #Z = T'
            'F' : { 'PARA' : ")E(", 'NUMERIC' : "i" } #NUMERIC = i
            }
        self.pila = ['$','E'] #INICIALMENTE, TIENE EL EOF Y LA PRODUCCION INICIAL
        self.Errores = []


    def obtenerMatrix(self, produccion, token):
        try:
            return self.tabla[produccion][token]
        except:#AQUI SE MANEJARIAN LOS ERRORES
            print("ERROR SINTACTICO")
            return "MALO"
    
    def pushear(self, producciones):
        lista = list(producciones)
        for l in lista:
            if l == "(":
                self.pila.append('PARA')
            elif l == ")":
                self.pila.append('PARC')
            elif l == "i":
                self.pila.append('NUMERIC')
            elif l == "+":
                self.pila.append('MAS')
            elif l == "*":
                self.pila.append('POR')
            elif l == "/":
                self.pila.append('DIV')
            elif l == "-":
                self.pila.append('MENOS')
            else:
                self.pila.append(l)

    def parse(self,tokens):
        tokens.append([0,0,'$',0])
        while len(self.pila) -1 >= 0:
            self.counter = len(self.pila) -1
            var1 = self.pila[self.counter]  #ULTIMO VALOR DE LA PILA, HASTA ARRIBA
            var2 = tokens[0][2]             #PRIMER TOKEN, TIPO DE TOKEN
            if var1 == var2:
                if var1 == "$":
                    return True
                elif var1 == "NUMERIC" or var1 == "PARA" or var1 == "PARC" or var1 == "MAS" or var1 == "POR"or var1 == "DIV"or var1 == "MENOS":
                    self.pila.pop()
                    del tokens[0]

            else:
                self.pila.pop() #SACA EL ULTIMO ELEMENTO DE LA PILA, HASTA ARRIBA
                val = self.obtenerMatrix(var1, var2)
                
                if val == "MALO":
                    return False
                elif val != None:
                    self.pushear(val)

entrada = open('entrada6.olc1')
contenido = entrada.read()
lexico = AnalisadorLexico()
tokens = lexico.analisarM(contenido)
for token in tokens:
    print(token)
parser = sintac()
parseoCorrecto = parser.parse(tokens)
if parseoCorrecto:
    print("Analisis Sintactico Correcto.")
else:
    print("Analisis Sintactico Incorrecto.")