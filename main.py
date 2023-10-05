import extras

TK_LINHA = 1
TK_COLUNA = 0
TOKEN_INDEX = ""
LEXEMA = ""

def ler_arquivo(arq: str) -> list:
    with open(arq, "r") as code:
        arquivo = code.readlines()
        lista = []
        for linha in arquivo:
            line = linha.replace(" ", "")
            for i in line:
                lista.append(i)

    return lista

def Print_Index(LEXEMA):
    if LEXEMA == "":
        return ('''
|     |     |{0:^20}|{1:^20}|
+-----+-----+--------------------+--------------------+'''.format(TOKEN_INDEX, ""))
    else:
        return ('''
|     |     |{0:^20}|{1:^20}|
+-----+-----+--------------------+--------------------+'''.format(TOKEN_INDEX, LEXEMA))

tokens_index = open("Tokens_Index.txt", "w", encoding='utf-8')
tokens_index.write ('''+-----+-----+--------------------+--------------------+
|{0:^5}|{1:^5}|{2:^20}|{3:^20}|
+-----+-----+--------------------+--------------------+'''.format("LIN", "COL", "TOKEN", "LEXEMA"))
        
if __name__ == "__main__":
    lista = ler_arquivo(extras.arquivo)

    estado, i = 0, 0
    while i < len(lista):
        token = lista[i]
        #print(TK_LINHA, TK_COLUNA)
        #if(lista[i] == "\n"):
        #    TK_COLUNA = 0
        #    TK_LINHA = TK_LINHA + 1
        #elif(lista[i] != "\n"):
        #    print(lista[i])
        #    TK_COLUNA = TK_COLUNA + 1
        match estado:
            case 0:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 1
                elif token in extras.TOKEN_ALF_MAI:
                    estado = 8
                elif token == '"':
                    estado = 14
                elif token == "<":
                    LEXEMA = LEXEMA + (token)
                    estado = 17
                elif token == "'":
                    estado = 20
                elif token == "#":
                    estado = 27
                elif token == "(":
                    estado = 29
                elif token == ")":
                    estado = 30
                elif token == ",":
                    estado = 31
                elif token in extras.TOKEN_ALF_MIN:
                    estado = 32
                elif token == "!":
                    estado = 41
                elif token == "=":
                    estado = 42
                elif token == ">":
                    estado = 43
                elif token == ":":
                    estado = 44
                elif token == "~":
                    estado = 45
                elif token == "+":
                    estado = 46
                elif token == "-":
                    estado = 47
                elif token == "*":
                    estado = 48
                elif token == "/":
                    estado = 49
                elif token == "&":
                    estado = 50
                elif token == "|":
                    estado = 51
            case 1:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 1
                elif token == ".":
                    estado = 2
                elif token == "e":
                    estado = 4
                elif token == "$":
                    estado = 9
                else:
                    estado = 7
            case 2:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 3
            case 3:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 3
                elif token == "e":
                    estado = 4
                else:
                    estado = 7
            case 4:
                if token == "-":
                    estado = 5
                elif token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 6
            case 5:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 6
            case 6:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 6
                else:
                    estado = 7
            case 7:
                #print("TK_NUMERO")
                TOKEN_INDEX = "TK_NUMERO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_NUMERO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 8:
                if token == "$":
                    estado = 9
            case 9:
                if token in extras.TOKEN_DEC:
                    estado = 10
            case 10:
                if token in extras.TOKEN_DEC:
                    estado = 10
                elif token == ".":
                    estado = 11
            case 11:
                if token in extras.TOKEN_DEC:
                    estado = 12
            case 12:
                if token in extras.TOKEN_DEC:
                    estado = 13
            case 13:
                #print("TK_MOEDA")
                TOKEN_INDEX = "TK_MOEDA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_MOEDA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 14:
                if token in extras.TOKEN_DEC + extras.TOKEN_ALF_MAI + extras.TOKEN_ALF_MIN:
                    estado = 15
            case 15:
                if token in extras.TOKEN_DEC + extras.TOKEN_ALF_MAI + extras.TOKEN_ALF_MIN:
                    estado = 15
                elif token == '"':
                    estado = 16
            case 16:
                #print("TK_CADEIA")
                TOKEN_INDEX = "TK_CADEIA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_CADEIA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 17:
                if token in extras.TOKEN_ALF_MIN:
                    LEXEMA = LEXEMA + (token)
                    estado = 18
                elif token == "=":
                    #print("TK_MENOR_IGUAL")
                    TOKEN_INDEX = "TK_MENOR_IGUAL"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_MENOR_IGUAL += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
                else:
                    #print("TK_MENOR")
                    TOKEN_INDEX = "TK_MENOR"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_MENOR += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 18:
                if token in extras.TOKEN_ALF_MIN + extras.TOKEN_DEC:
                    LEXEMA = LEXEMA + (token)
                    estado = 18
                elif token == ">":
                    LEXEMA = LEXEMA + (token)
                    estado = 19
                    i -= 1
            case 19:
                #print("TK_ID")
                TOKEN_INDEX = "TK_ID"
                tokens_index.write(Print_Index(LEXEMA))
                LEXEMA = ""
                extras.TK_ID += 1
                extras.TK_TOTAL +=1
                estado = 0
                #i -= 1
            case 20:
                if token == "'":
                    estado = 21
            case 21:
                if token == "'":
                    estado = 22
            case 22:
                if token != "'":
                    estado = 23
            case 23:
                if token != "'":
                    estado = 23
                elif token == "'":
                    estado = 24
            case 24:
                if token == "'":
                    estado = 25
            case 25:
                if token == "'":
                    estado = 26
            case 26:
                #print("TK_COMMENT_BLK")
                TOKEN_INDEX = "TK_COMMENT_BLK"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_COMMENT_BLK += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 27:
                if token != "\n":
                    estado = 27
                elif token == "\n":
                    estado = 28
            case 28:
                #print("TK_COMMENT_LN")
                TOKEN_INDEX = "TK_COMMENT_LN"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_COMMENT_LN += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 29:
                #print("TK_DLMT_ABRE")
                TOKEN_INDEX = "TK_DLMT_ABRE"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_DLMT_ABRE += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 30:
                #print("TK_DLMT_FECHA")
                TOKEN_INDEX = "TK_DLMT_FECHA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_DLMT_FECHA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 31:
                #print("TK_DLMT_VIRG")
                TOKEN_INDEX = "TK_DLMT_VIRG"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_DLMT_VIRG += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 32:
                palavra = ""

                for new_token in lista[i - 1 :]:
                    if new_token in extras.TOKEN_ALF_MIN + "_":
                        palavra = palavra + (new_token)
                    else:
                        estado = 0
                        i -= 1
                        break

                if palavra in [
                    "programa",
                    "fim_programa",
                    "se",
                    "senao",
                    "entao",
                    "imprima",
                    "leia",
                    "enquanto",
                ]:
                    if palavra == "programa":
                        estado = 33
                    elif palavra == "fim_programa":
                        estado = 34
                    elif palavra == "se":
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
                    i += len(palavra) - 1
            case 33:
                #print("TK_PROGRAMA")
                TOKEN_INDEX = "TK_PROGRAMA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_PROGRAMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 34:
                #print("TK_FIM_PROGRAMA")
                TOKEN_INDEX = "TK_FIM_PROGRAMA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_FIM_PROGRAMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 35:
                #print("TK_SE")
                TOKEN_INDEX = "TK_SE"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_SE += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 36:
                #print("TK_SENAO")
                TOKEN_INDEX = "TK_SENAO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_SENAO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 37:
                #print("TK_ENTAO")
                TOKEN_INDEX = "TK_ENTAO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_ENTAO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 38:
                #print("TK_IMPRIMA")
                TOKEN_INDEX = "TK_IMPRIMA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_IMPRIMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 39:
                #print("TK_LEIA")
                TOKEN_INDEX = "TK_LEIA"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_LEIA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 40:
                #print("TK_ENQUANTO")
                TOKEN_INDEX = "TK_ENQUANTO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_ENQUANTO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 41:
                if token == "=":
                    #print("TK_DIFERENTE")    
                    TOKEN_INDEX = "TK_DIFERENTE"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_DIFERENTE += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 42:
                if i + 1 < len(lista):
                    if lista[i + 1] not in ["<", ">"]:
                        #print("TK_IGUAL")        
                        TOKEN_INDEX = "TK_IGUAL"
                        tokens_index.write(Print_Index(LEXEMA))
                        extras.TK_IGUAL += 1
                        extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 43:
                estado = 0
                #i -= 1
                if token == "=":
                    #print("TK_MAIOR_IGUAL")    
                    TOKEN_INDEX = "TK_MAIOR_IGUAL"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_MAIOR_IGUAL += 1
                    extras.TK_TOTAL +=1
                else:
                    #print("TK_MAIOR")    
                    TOKEN_INDEX = "TK_MAIOR"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_MAIOR += 1
                    extras.TK_TOTAL +=1
            case 44:
                if token == "=":
                    #print("TK_ATRIBUIÇÃO")    
                    TOKEN_INDEX = "TK_ATRIBUIÇÃO"
                    tokens_index.write(Print_Index(LEXEMA))
                    extras.TK_ATRIBUIÇÃO += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 45:
                #print("TK_NEGAÇÃO")
                TOKEN_INDEX = "TK_NEGAÇÃO",{" "}*7
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_NEGAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 46:
                #print("TK_ADIÇÃO")
                TOKEN_INDEX = "TK_ADIÇÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_ADIÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 47:
                #print("TK_SUBTRAÇÃO")
                TOKEN_INDEX = "TK_SUBTRAÇÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_SUBTRAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 48:
                #print("TK_MULTIPLICAÇÃO")
                TOKEN_INDEX = "TK_MULTIPLICAÇÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_MULTIPLICAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 49:
                #print("TK_DIVISÃO")
                TOKEN_INDEX = "TK_DIVISÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_DIVISÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 50:
                #print("TK_CONJUNÇÃO")
                TOKEN_INDEX = "TK_CONJUNÇÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_CONJUNÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 51:
                #print("TK_DISJUNÇÃO")
                TOKEN_INDEX = "TK_DISJUNÇÃO"
                tokens_index.write(Print_Index(LEXEMA))
                extras.TK_DISJUNÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
        i += 1

    tokens_index.close()
    
    somatorio = extras.PrintSomatorio()
    with open("Tokens_Somatorio.txt", "w", encoding='utf-8') as tokens_somatorio:
        tokens_somatorio.write(str(somatorio))
