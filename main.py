#Tokens
token_dec = "1236567890"
token_hex = "ABCDEF"
token_alf_mai = "GHIJKLMNOPQRSTUVWXYZ"
token_alf_min = "abcdefghijklmnopqrstuvwxyz"

global estado, palavra
estado = 0
palavra = ""

def ShowState():
    print("estado: ", estado, "lista: ", lista[i])

with open("ex1.txt", "r") as code:
    arquivo = code.readlines()
    lista = []
    for linha in arquivo:
        line = linha.strip('').replace(' ', '')
        for i in line:
            lista.append(i)

i=0
while (True):
    if i==len(lista):
        break
    #ShowState()
    if estado == 0 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 1
    elif estado == 0 and lista[i] in token_alf_mai:
        estado = 8
    elif estado == 0 and lista[i] == '"':
        estado = 14
    elif estado == 0 and lista[i] == "<":
        estado = 17
    elif estado == 0 and lista[i] == "'":
        estado = 20
    elif estado == 0 and lista[i] == "#":
        estado = 27
    elif estado == 0 and (lista[i] == "("):
        estado = 29
    elif estado == 0 and (lista[i] == ")"):
        estado = 30
    elif estado == 0 and (lista[i] == ","):
        estado = 31
    elif estado == 0 and lista[i] in token_alf_min:
        estado = 32
    elif estado == 0 and lista[i] == "!":
        estado = 41
    elif estado == 0 and lista[i] == "=":
        estado = 42
    elif estado == 0 and lista[i] == ">":
        estado = 43
    elif estado == 0 and lista[i] == ":":
        estado = 44
    elif estado == 0 and lista[i] == "~":
        estado = 45
    elif estado == 0 and lista[i] == "+":
        estado = 46
    elif estado == 0 and lista[i] == "-":
        estado = 47
    elif estado == 0 and lista[i] == "*":
        estado = 48
    elif estado == 0 and lista[i] == "/":
        estado = 49
    elif estado == 0 and lista[i] == "&":
        estado = 50
    elif estado == 0 and lista[i] == "|":
        estado = 51
    
    if estado == 1 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 1
    elif estado == 1 and lista[i] == ".":
        estado = 2
    elif estado == 1 and lista[i] == "e":
        estado = 4
    elif estado == 1 and (lista[i] not in token_hex and lista[i] not in token_dec):
        estado = 7
    elif estado == 1 and lista[i] == "$":
        estado = 9
    
    if estado == 2 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 3

    if estado == 3 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 3
    elif estado == 3 and lista[i] == "e":
        estado = 4
    elif estado == 3 and (lista[i] not in token_hex and lista[i] not in token_dec):
        estado = 7
    
    if estado == 4 and lista[i] == "-":
        estado = 5
    elif estado == 4 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 6
    
    if estado == 5 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 6

    if estado == 6 and (lista[i] not in token_hex and lista[i] not in token_dec):
        estado = 7
    
    if estado == 7:
        print("TK_NUMERO")
        estado = 0
    
    if estado == 8 and lista[i] == "$":
        estado = 9

    if estado == 9 and lista[i] in token_dec:
        estado = 10

    if estado == 10 and lista[i] in token_dec:
        estado = 10
    elif estado == 10 and lista[i] == ".":
        estado = 11

    if estado == 11 and lista[i] in token_dec:
        estado = 12

    if estado == 12 and lista[i] in token_dec:
        estado = 13

    if estado == 13:
        print("TK_MOEDA")
        estado = 0

    if estado == 14 and (lista[i] in token_dec or lista[i] in token_alf_mai or lista[i] in token_alf_min):
        estado = 15

    if estado == 15 and (lista[i] in token_dec or lista[i] in token_alf_mai or lista[i] in token_alf_min):
        estado = 15
    elif estado == 15 and lista[i] == '"':
        estado = 16

    if estado == 16:
        print("TK_CADEIA")
        estado = 0

    if estado == 17:
        if lista[i] in token_alf_min:
            estado = 18
        if lista[i] == "=":
            print("TK_MENOR_IGUAL")
            estado = 0
        #elif lista[i] not in token_alf_min or lista[i] != "=":
        #    print("TK_MENOR")
        #    estado = 0

    if estado == 18 and (lista[i] in token_alf_min or lista[i] in token_dec):
        estado = 18
    if estado == 18 and lista[i] == ">":
        estado = 19

    if estado == 19:
        print("TK_ID")
        estado = 0

    if estado == 20 and lista[i] == "'":
        estado = 21

    if estado == 21 and lista[i] == "'":
        estado = 22

    if estado == 22 and lista[i] != "'":
        estado = 23

    if estado == 23 and lista[i] != "'":
        estado = 23
    elif estado == 23 and lista[i] == "'":
        estado = 24

    if estado == 24 and lista[i] == "'":
        estado = 25

    if estado == 25 and lista[i] == "'":
        estado = 26

    if estado == 26:
        print("TK_COMMENT_BLK")
        estado = 0

    if estado == 27 and lista[i] != "\n":
        estado = 27
    elif estado == 27 and lista[i] == "\n":
        estado = 28

    if estado == 28:
        print("TK_COMMENT_LN")
        estado = 0

    if estado == 29:
        print("TK_DLMT_ABRE")
        estado = 0
    
    if estado == 30:
        print("TK_DLMT_FECHA")
        estado = 0

    if estado == 31:
        print("TK_DLMT_VIRG")
        estado = 0

    if estado == 32:
        if lista[i] in token_alf_min or lista[i] == "_":
            palavra = palavra + (lista[i])
        else:
            estado = 0
            i-=1

        if palavra == "programa":
            estado = 33
        elif palavra == "fim_programa":
            estado = 34
        elif  palavra == "se":
            estado = 35
        elif palavra == "senao":
            estado = 36
        elif palavra == "entao":
            estado = 37
        elif palavra == "imprima":
            estado = 38
        elif palavra == "leia":
            estado = 39
        elif palavra == "enquanto":
            estado = 40

    if estado == 33:
        print("TK_PROGRAMA")
        palavra = ""
        estado = 0

    if estado == 34:
        print("TK_FIM_PROGRAMA")
        palavra = ""
        estado = 0

    if estado == 35:
        print("TK_SE")
        palavra = ""
        estado = 0

    if estado == 36:
        print("TK_SENAO")
        palavra = ""
        estado = 0

    if estado == 37:
        print("TK_ENTAO")
        palavra = ""
        estado = 0

    if estado == 38:
        print("TK_IMPRIMA")
        palavra = ""
        estado = 0

    if estado == 39:
        print("TK_LEIA")
        palavra = ""
        estado = 0

    if estado == 40:
        print("TK_ENQUANTO")
        palavra = ""
        estado = 0

    if estado == 41 and lista[i] == "=":
        print("TK_DIFERENTE")
        estado = 0

    if estado == 42:
        print("TK_IGUAL")
        estado = 0

    if estado == 43:
        if lista[i] == "=":
            print("TK_MAIOR_IGUAL")
            estado = 0
        #else:
        #    print("TK_MAIOR")
        #    estado = 0

    if estado == 44 and lista[i] == "=":
        print("TK_ATRIBUIÇÃO")
        estado = 0

    if estado == 45:
        print("TK_NEGAÇÃO")
        estado = 0

    if estado == 46:
        print("TK_ADIÇÃO")
        estado = 0

    if estado == 47:
        print("TK_SUBTRAÇÃO")
        estado = 0

    if estado == 48:
        print("TK_MULTIPLICAÇÃO")
        estado = 0

    if estado == 49:
        print("TK_DIVISÃO")
        estado = 0
        
    if estado == 50:
        print("TK_CONJUNÇÃO")
        estado = 0

    if estado == 51:
        print("TK_DISJUNÇÃO")
        estado = 0

    i+=1

code.close()