#pruebas de analisadores lexico
class AnalisadorPrueba:
#VECTOR DE TOKENS
    Tokens = []
#vector de columnas
    Columnas =[]
#vector de filas
    Filas = []
#vector de columnas para erroes
    ColErrores = []
#vector fila pra errores 
    FilErrores = []
#vector de errores
    TokensErrores = []
#contador de tokens
    Ultimo = ''
#contador de errores
    ContadorErrores = '' 
#vector para descripcion 
    Descripcion = []
#constador para descripcion
    ContadorDescripcion = 0 
#vector para labras reservadas (o un diccionario en este caso, para mas facil)
    PalabrasReservadas = {}
#contador de filas
    filas = 0
#contador de columnas 
    columnas = 0


#constructor
    def __init__(self):
        Ultimo=0
        ContadorErrores = 0
        filas = 1
        columnas = 1
    
# global Ultimo,ContadorErrores,ContadorDescripcion,filas, columnas, Tokens, Columnas,Filas,ColErrores,FilErrores,TokensErrores

#FUNCION PARA LIMPIAR EL ARCHIVO DE ENTRADA
    def limpiar (self, archivoEntrada):
        print (archivoEntrada)
        cadenaLimpia = ""
        archivoEntrada.replace("    ", " ")
        for I in archivoEntrada:
            if I != '\n':
            #     pass     
            # elif I != '\n':
                cadenaLimpia +=I
                # print(cadenaLimpia)
        return cadenaLimpia

hola = AnalisadorPrueba
# hola.limpiar("111","hola \t mundo \t cesar \nsalto")

nombre= 'entrada' 
entrada = open('entrada2.olc1')
contenido = entrada.read()
print(hola.limpiar("111",contenido))
