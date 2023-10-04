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

def PrintSomatorio():
    "+-------------------------------+----------+\n"
    "|TOKEN\t\t\t\t|  QTD USO |\n"
    "+-------------------------------+----------+\n"
    "|TK_NUMERO\t\t\t|      ", TK_NUMERO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MOEDA\t\t\t|      ", TK_MOEDA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_CADEIA\t\t\t|      ", TK_CADEIA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MENOR_IGUAL\t\t\t|      ", TK_MENOR_IGUAL, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MENOR\t\t\t|      ", TK_MENOR, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_ID\t\t\t\t|      ", TK_ID, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_COMMENT_BLK\t\t\t|      ", TK_COMMENT_BLK, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_COMMENT_LN\t\t\t|      ", TK_COMMENT_LN, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DLMT_ABRE\t\t\t|      ", TK_DLMT_ABRE, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DLMT_FECHA\t\t\t|      ", TK_DLMT_FECHA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DLMT_VIRG\t\t\t|      ", TK_DLMT_VIRG, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_PROGRAMA\t\t\t|      ", TK_PROGRAMA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_FIM_PROGRAMA\t\t|      ", TK_FIM_PROGRAMA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_SE\t\t\t\t|      ", TK_SE, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_SENAO\t\t\t|      ", TK_SENAO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_ENTAO\t\t\t|      ", TK_ENTAO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_IMPRIMA\t\t\t|      ", TK_IMPRIMA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_LEIA\t\t\t|      ", TK_LEIA, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_ENQUANTO\t\t\t|      ", TK_ENQUANTO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DIFERENTE\t\t\t|      ", TK_DIFERENTE, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_IGUAL\t\t\t|      ", TK_IGUAL, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MAIOR_IGUAL\t\t\t|      ", TK_MAIOR_IGUAL, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MAIOR\t\t\t|      ", TK_MAIOR, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_ATRIBUIÇÃO\t\t\t|      ", TK_ATRIBUIÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_NEGAÇÃO\t\t\t|      ", TK_NEGAÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_ADIÇÃO\t\t\t|      ", TK_ADIÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_SUBTRAÇÃO\t\t\t|      ", TK_SUBTRAÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_MULTIPLICAÇÃO\t\t|      ", TK_MULTIPLICAÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DIVISÃO\t\t\t|      ", TK_DIVISÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_CONJUNÇÃO\t\t\t|      ", TK_CONJUNÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TK_DISJUNÇÃO\t\t\t|      ", TK_DISJUNÇÃO, " |\n"
    "+-------------------------------+----------+\n"
    "|TOTAL DE TOKENS\t\t|      ", TK_TOTAL, "|\n"
    "+-------------------------------+----------+\n"
    return string