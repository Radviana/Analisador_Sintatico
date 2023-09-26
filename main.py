#Tokens
token_dec = "1236567890"
token_hex = "ABCDEF"
token_alf_mai = "GHIJKLMNOPQRSTUVWXYZ"
token_alf_min = "abcdefghijklmnopqrstuvwxyz"
token_programa = "programa"
token_fim_programa = "fim_programa"
token_se = "se"
token_senao = "senao"
token_entao = "entao"
token_imprima = "imprima"
token_leia = "leia"
token_enquanto = "enquanto"

global estado, palavra
estado = 0
palavra = ""

def ShowState():
    print("estado: ", estado, "lista: ", lista[i])

with open("ex1.cic", "r") as code:
    arquivo = code.readlines()
    lista = []
    for linha in arquivo:
        line = linha.strip('').replace(' ', '')
        for i in line:
            lista.append(i)

for i in range(len(lista)):
    ShowState()
    if estado == 0 and (lista[i] in token_hex or lista[i] in token_dec):
        estado = 1
    elif estado == 0 and lista[i] in token_alf_mai:
        estado = 8
    elif estado == 0 and lista[i] == '"':
        estado = 14
    elif estado == 0 and lista[i] == '<':
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
        palavra = palavra + (lista[i])
        estado = 32
    
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

    if estado == 17 and lista[i] in token_alf_min:
        estado = 18

    if estado == 18 and (lista[i] in token_alf_min or lista[i] in token_dec):
        estado = 18
    if estado == 18 and lista[i] == '>':
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

    if estado == 32 and (lista[i] in token_alf_min or lista[i] == "_"):
        palavra = palavra + (lista[i])
    elif estado == 32 and palavra == "programa":
        estado = 33
    elif estado == 32 and palavra == "fim_programa":
        estado = 34
    elif estado == 32 and palavra == "se":
        estado = 35
    elif estado == 32 and palavra == "senao":
        estado = 36
    elif estado == 32 and palavra == "entao":
        estado = 37
    elif estado == 32 and palavra == "imprima":
        estado = 38
    elif estado == 32 and palavra == "leia":
        estado = 39
    elif estado == 32 and palavra == "enquanto":
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

code.close()