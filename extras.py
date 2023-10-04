# Tokens
TOKEN_DEC = "0123656789"
TOKEN_HEX = "ABCDEF"
TOKEN_ALF_MAI = "GHIJKLMNOPQRSTUVWXYZ"
TOKEN_ALF_MIN = "abcdefghijklmnopqrstuvwxyz"

# Contadores
TK_NUMERO = 0
TK_MOEDA = 0
TK_CADEIA = 0
TK_MENOR_IGUAL = 0
TK_MENOR = 0
TK_ID = 0
TK_COMMENT_BLK = 0
TK_COMMENT_LN = 0
TK_DLMT_ABRE = 0
TK_DLMT_FECHA = 0
TK_DLMT_VIRG = 0
TK_PROGRAMA = 0
TK_FIM_PROGRAMA = 0
TK_SE = 0
TK_SENAO = 0
TK_ENTAO = 0
TK_IMPRIMA = 0
TK_LEIA = 0
TK_ENQUANTO = 0
TK_DIFERENTE = 0
TK_IGUAL = 0
TK_MAIOR_IGUAL = 0
TK_MAIOR = 0
TK_ATRIBUIÇÃO = 0
TK_NEGAÇÃO = 0
TK_ADIÇÃO = 0
TK_SUBTRAÇÃO = 0
TK_MULTIPLICAÇÃO = 0
TK_DIVISÃO = 0
TK_CONJUNÇÃO = 0
TK_DISJUNÇÃO = 0
TK_TOTAL = 0

# Arquivo
arquivo = "ex1.txt"

def PrintResults():
    print("+-------------------------------+----------+")
    print("|TOKEN\t\t\t\t|  QTD USO |")
    print("+-------------------------------+----------+")
    print("|TK_NUMERO\t\t\t|      ", TK_NUMERO, " |")
    print("+-------------------------------+----------+")
    print("|TK_MOEDA\t\t\t|      ", TK_MOEDA, " |")
    print("+-------------------------------+----------+")
    print("|TK_CADEIA\t\t\t|      ", TK_CADEIA, " |")
    print("+-------------------------------+----------+")
    print("|TK_MENOR_IGUAL\t\t\t|      ", TK_MENOR_IGUAL, " |")
    print("+-------------------------------+----------+")
    print("|TK_MENOR\t\t\t|      ", TK_MENOR, " |")
    print("+-------------------------------+----------+")
    print("|TK_ID\t\t\t\t|      ", TK_ID, " |")
    print("+-------------------------------+----------+")
    print("|TK_COMMENT_BLK\t\t\t|      ", TK_COMMENT_BLK, " |")
    print("+-------------------------------+----------+")
    print("|TK_COMMENT_LN\t\t\t|      ", TK_COMMENT_LN, " |")
    print("+-------------------------------+----------+")
    print("|TK_DLMT_ABRE\t\t\t|      ", TK_DLMT_ABRE, " |")
    print("+-------------------------------+----------+")
    print("|TK_DLMT_FECHA\t\t\t|      ", TK_DLMT_FECHA, " |")
    print("+-------------------------------+----------+")
    print("|TK_DLMT_VIRG\t\t\t|      ", TK_DLMT_VIRG, " |")
    print("+-------------------------------+----------+")
    print("|TK_PROGRAMA\t\t\t|      ", TK_PROGRAMA, " |")
    print("+-------------------------------+----------+")
    print("|TK_FIM_PROGRAMA\t\t|      ", TK_FIM_PROGRAMA, " |")
    print("+-------------------------------+----------+")
    print("|TK_SE\t\t\t\t|      ", TK_SE, " |")
    print("+-------------------------------+----------+")
    print("|TK_SENAO\t\t\t|      ", TK_SENAO, " |")
    print("+-------------------------------+----------+")
    print("|TK_ENTAO\t\t\t|      ", TK_ENTAO, " |")
    print("+-------------------------------+----------+")
    print("|TK_IMPRIMA\t\t\t|      ", TK_IMPRIMA, " |")
    print("+-------------------------------+----------+")
    print("|TK_LEIA\t\t\t|      ", TK_LEIA, " |")
    print("+-------------------------------+----------+")
    print("|TK_ENQUANTO\t\t\t|      ", TK_ENQUANTO, " |")
    print("+-------------------------------+----------+")
    print("|TK_DIFERENTE\t\t\t|      ", TK_DIFERENTE, " |")
    print("+-------------------------------+----------+")
    print("|TK_IGUAL\t\t\t|      ", TK_IGUAL, " |")
    print("+-------------------------------+----------+")
    print("|TK_MAIOR_IGUAL\t\t\t|      ", TK_MAIOR_IGUAL, " |")
    print("+-------------------------------+----------+")
    print("|TK_MAIOR\t\t\t|      ", TK_MAIOR, " |")
    print("+-------------------------------+----------+")
    print("|TK_ATRIBUIÇÃO\t\t\t|      ", TK_ATRIBUIÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_NEGAÇÃO\t\t\t|      ", TK_NEGAÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_ADIÇÃO\t\t\t|      ", TK_ADIÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_SUBTRAÇÃO\t\t\t|      ", TK_SUBTRAÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_MULTIPLICAÇÃO\t\t|      ", TK_MULTIPLICAÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_DIVISÃO\t\t\t|      ", TK_DIVISÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_CONJUNÇÃO\t\t\t|      ", TK_CONJUNÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TK_DISJUNÇÃO\t\t\t|      ", TK_DISJUNÇÃO, " |")
    print("+-------------------------------+----------+")
    print("|TOTAL DE TOKENS\t\t|      ", TK_TOTAL, "|")
    print("+-------------------------------+----------+")