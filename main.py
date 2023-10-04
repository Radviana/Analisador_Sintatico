import extras

def ler_arquivo(arq: str) -> list:
    with open(arq, "r") as code:
        arquivo = code.readlines()
        lista = []
        for linha in arquivo:
            line = linha.replace(" ", "")
            for i in line:
                lista.append(i)

    return lista

if __name__ == "__main__":
    lista = ler_arquivo(extras.arquivo)

    estado, i = 0, 0
    while i < len(lista):
        token = lista[i]
        match estado:
            case 0:
                if token in extras.TOKEN_HEX + extras.TOKEN_DEC:
                    estado = 1
                elif token in extras.TOKEN_ALF_MAI:
                    estado = 8
                elif token == '"':
                    estado = 14
                elif token == "<":
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
                #print("extras.")
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
                extras.TK_CADEIA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 17:
                if token in extras.TOKEN_ALF_MIN:
                    estado = 18
                elif token == "=":
                    #print("TK_MENOR_IGUAL")
                    extras.TK_MENOR_IGUAL += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
                else:
                    #print("TK_MENOR")
                    extras.TK_MENOR += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 18:
                if token in extras.TOKEN_ALF_MIN + extras.TOKEN_DEC:
                    estado = 18
                elif token == ">":
                    estado = 19
                    i -= 1
            case 19:
                #print("TK_ID")
                extras.TK_ID += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
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
                extras.TK_COMMENT_LN += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 29:
                #print("TK_DLMT_ABRE")
                extras.TK_DLMT_ABRE += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 30:
                #print("TK_DLMT_FECHA")
                extras.TK_DLMT_FECHA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 31:
                #print("TK_DLMT_VIRG")
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
                extras.TK_PROGRAMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 34:
                #print("TK_FIM_PROGRAMA")
                extras.TK_FIM_PROGRAMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 35:
                #print("TK_SE")
                extras.TK_SE += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 36:
                #print("TK_SENAO")
                extras.TK_SENAO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 37:
                #print("TK_ENTAO")
                extras.TK_ENTAO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 38:
                #print("TK_IMPRIMA")
                extras.TK_IMPRIMA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 39:
                #print("TK_LEIA")
                extras.TK_LEIA += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 40:
                #print("TK_ENQUANTO")
                extras.TK_ENQUANTO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 41:
                if token == "=":
                    #print("TK_DIFERENTE")
                    extras.TK_DIFERENTE += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 42:
                if i + 1 < len(lista):
                    if lista[i + 1] not in ["<", ">"]:
                        #print("TK_IGUAL")
                        extras.TK_IGUAL += 1
                        extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 43:
                estado = 0
                i -= 1
                if token == "=":
                    #print("TK_MAIOR_IGUAL")
                    extras.TK_MAIOR_IGUAL += 1
                    extras.TK_TOTAL +=1
                else:
                    #print("TK_MAIOR")
                    extras.TK_MAIOR += 1
                    extras.TK_TOTAL +=1
            case 44:
                if token == "=":
                    #print("TK_ATRIBUIÇÃO")
                    extras.TK_ATRIBUIÇÃO += 1
                    extras.TK_TOTAL +=1
                    estado = 0
                    i -= 1
            case 45:
                #print("TK_NEGAÇÃO")
                extras.TK_NEGAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 46:
                #print("TK_ADIÇÃO")
                extras.TK_ADIÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 47:
                #print("TK_SUBTRAÇÃO")
                extras.TK_SUBTRAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 48:
                #print("TK_MULTIPLICAÇÃO")
                extras.TK_MULTIPLICAÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 49:
                #print("TK_DIVISÃO")
                extras.TK_DIVISÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 50:
                #print("TK_CONJUNÇÃO")
                extras.TK_CONJUNÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
            case 51:
                #print("TK_DISJUNÇÃO")
                extras.TK_DISJUNÇÃO += 1
                extras.TK_TOTAL +=1
                estado = 0
                i -= 1
        i += 1

    somatorio = extras.PrintSomatorio()
    with open("Somatorio_Tokens.txt", "w") as somatorio_tokens:
        somatorio_tokens.write(str(somatorio))