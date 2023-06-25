# ESTE CODIGO IMPLEMENTA UM ANALIZADOR LEXICO PARA O EXEMPLO DE FRAGMENTO DE LINGUAGEM APRESENTADO EM SALA DE AULA (VEJA OS SLIDES DA AULA 4: ANALISE LEXICA: PARTE 2)
# E PODERA SER UTILIZADO COMO PONTO DE PARTIDA PARA IMPLEMENTACAO DO ANALISADOR LEXICO PARA LINGUAGEM ADOTADA NO TRABALHO PROPOSTO.


#NOME TOKENS
PROGRAM = 251
BEGIN = 252
END = 253
ASSIGNMENT = 254
OPARIT = 255
IF = 256
THEN = 257
ELSE = 258
RELOP = 259
ID = 260
NUM = 261

#token_atributoS
LT = 262 # <
LE = 263 # <=
EQ = 264 # ==
NE = 265 # <>
GT = 266 # >
GE = 267 # >=
PLUS = 268 # +
MINUS = 269 # -
DIV = 270 # /
TIMES = 271 # *
PARENTHESES_L = 272 # (
PARENTHESES_R = 273 # )
DOT = 274 # .
SEMICOLON = 275 # ;
COMMA = 276 # ,

class token:
    def __init__(self, token_nome, token_atributo):
        self.token_nome = token_nome
        self.token_atributo = token_atributo        
        

status = 0
partida = 0
contador_leitura = 0
simbolo = ''


def ler_arquivo(fileName):

    file = open(fileName, "r")
    if file == None: 
        return None

    simbolo = ''
    while True:
        char = file.read(1)     
        if not char:
            break
        simbolo = simbolo + char
    return simbolo


def falhar(status):
    partida = 0
    if status == 0:
        partida = 10
  
    if status == 10:
        partida = 13

    if status == 13:
        partida = 36

    if status == 36:
        partida = 41

    if status == 41:
        partida = 62
    
    if status == 100:
        print("Erro encontrado no código")
        print("Erro do compilador")
        exit()

    return partida


def proximo_token(simbolo, partida):
    contador_leitura = 0
    status = partida
    programa_nome = ''
    nome_num = ''
    Token = token(None,None)
    while contador_leitura < len(simbolo):
        #print('caracter lido:', simbolo[contador_leitura])
        if status == 0:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            elif(c == '<'):
                status = 1
            elif(c == '='):
                status = 5
            elif(c == '>'):
                status = 6
            elif(c == ':'):
                status = 7
            else: 
                status = falhar(status)

        if status == 1:
            contador_leitura += 1
            c = simbolo[contador_leitura]

            if(c == '='):
                status = 2
            elif(c == '>'):
                status = 3
            else:
                status = 4

        if status == 2:
            contador_leitura += 1
            print("<relop, LE>")
            Token.token_nome = RELOP
            Token.token_atributo = LE
            status = 0

        if status == 3:
            contador_leitura += 1
            print("<relop, NE>")
            Token.token_nome = RELOP
            Token.token_atributo = NE
            status = 0

        if status == 4:
            contador_leitura += 1
            print("<relop, LT>")
            Token.token_nome = RELOP
            Token.token_atributo = LT
            status = 0

        if status == 5:
            contador_leitura += 1
            print("<relop, EQ>")
            Token.token_nome = RELOP
            Token.token_atributo = EQ

        if status == 6:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == '=':
                status = 8
            else:
                status = 9

        if status == 7:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == '=':
                contador_leitura += 1
                print("<:=, >")
                Token.token_nome = ASSIGNMENT
                Token.token_atributo = ':='
                status = 0
            else:
                status = 32

        if status == 8:
            contador_leitura += 1
            print("<relop, GE>")
            Token.token_nome = RELOP
            Token.token_atributo = GE
            status = 0
            

        if status == 9:
            contador_leitura += 1
            print("<relop, GT>")
            Token.token_nome = RELOP
            Token.token_atributo = GT
            status = 0
        
        if status == 10:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            else:
                if c == '(':
                    status = 11
                elif c == ')':
                    status = 12
                else:
                    status = falhar(status)

        if status == 11:
            contador_leitura += 1
            print("<(, >")
            Token.token_nome = RELOP
            Token.token_atributo = PARENTHESES_L
            status = 0
        
        if status == 12:
            contador_leitura += 1
            print("<), >")
            Token.token_nome = RELOP
            Token.token_atributo = PARENTHESES_R
            status = 0
        
        if status == 13:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            else:
                if c == '.':
                    status = 14
                elif c == ';':
                    status = 15
                elif c == ',':
                    status = 16
                elif c == 'p': # cheacando se sera escrito 'program'
                    status = 17
                elif c == 'b': # cheacando se sera escrito 'begin'
                    status = 24
                elif c.isnumeric(): # checando numeros
                    status = 31
                elif c == 'i': # cheacando se sera escrito 'if' ou 'int'
                    status = 32
                elif c == 'v': # cheacando se sera escrito 'var'
                    status = 44
                elif c == 'e': # cheacando se sera escrito 'end' ou 'else'
                    status = 47
                elif c == 't': # cheacando se sera escrito 'then'
                    status = 53
                elif c == 'w': # cheacando se sera escrito 'while'
                    status = 57
                elif c == 'd': # checando se sera escrito 'do'
                    status = 35
                else:
                    status = falhar(status)

        if status == 14:
            contador_leitura += 1
            print("<., >")
            Token.token_nome = RELOP
            Token.token_atributo = DOT
            status = 0
        
        if status == 15:
            contador_leitura += 1
            print("<;, >")
            Token.token_nome = RELOP
            Token.token_atributo = SEMICOLON
            status = 0
        
        if status == 16:
            contador_leitura += 1
            print("<,>")
            Token.token_nome = RELOP
            Token.token_atributo = COMMA
            status = 0
        
        if status == 17:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'r':
                status = 18
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 18:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'o':
                status = 19
            else:
                contador_leitura = contador_leitura - 1
                status = 62
            
        if status == 19:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'g':
                status = 20
            else:
                contador_leitura = contador_leitura - 1
                status = 62
            
        if status == 20:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'r':
                status = 21
            else:
                contador_leitura = contador_leitura - 1
                status = 62
            
        if status == 21:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'a':
                status = 22
            else:
                contador_leitura = contador_leitura - 1
                status = 62
            
        if status == 22:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'm':
                status = 23
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 23:    
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print("<program, >")
                Token.token_nome = RELOP
                Token.token_atributo = PROGRAM
                status = 0
            else:
                status = 32
            
        if status == 24:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'e':
                status = 25
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 25:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'g':
                status = 26
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 26:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'i':
                status = 27
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 27:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'n':
                status = 28
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 28:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ' or c == '\n':
                print("<begin, >")
                Token.token_nome = RELOP
                Token.token_atributo = BEGIN
                status = 0
            else:
                contador_leitura = contador_leitura - 1
                status = 62

        if status == 31:
            nome_num = nome_num + simbolo[contador_leitura]
            contador_leitura += 1
            if simbolo[contador_leitura].isnumeric():
                status = 31
            else:
                print('<num, ' + nome_num + '>')
                nome_num = ''
                status = 0
    
        if status == 32:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'f':
                status = 33
            elif c == 'n':
                status = 34
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 33:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<if, >')
                status = 0
                contador_leitura += 1
            else:
                status = 100
        
        if status == 34:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 't':
                print('<int, >')
                status = 0
                contador_leitura += 1
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 35:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'o':
                status = 43
            else:
                contador_leitura = contador_leitura - 1
                status = 40
            
        if status == 36:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            elif(c == '+'):
                status = 37
            elif(c == '-'):
                status = 38
            elif(c =='*'):
                status = 39
            elif(c == 'd'): #div
                status = 40
            else:
                status = falhar(status)

        if status == 37:
            contador_leitura += 1
            print("<oparit, +>")
            Token.token_nome = OPARIT
            Token.token_atributo = PLUS
            status = 0
        
        if status == 38:
            contador_leitura += 1
            print("<oparit, ->")
            Token.token_nome = OPARIT
            Token.token_atributo = MINUS
            status = 0
        
        if status == 39:
            contador_leitura += 1
            print("<oparit, *>")
            Token.token_nome = OPARIT
            Token.token_atributo = TIMES
            status = 0
        
        if status == 40:
            contador_leitura += 1
            if simbolo[contador_leitura] == 'i':
                contador_leitura += 1
                if simbolo[contador_leitura] == 'v':
                    contador_leitura += 1
                    if simbolo[contador_leitura] == ' ':
                        print("<oparit, div>")
                    else:
                        contador_leitura = contador_leitura - 3
                        status = 62
                else:
                    contador_leitura = contador_leitura - 2
                    status = 62
            else:
                contador_leitura = contador_leitura - 1
                status = 62
            Token.token_nome = OPARIT
            Token.token_atributo = DIV
            status = 0
        
        if status == 41:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            else:
                status = falhar(status)
                Token.token_nome = -1
                Token.token_atributo = -1
        
        if status == 43:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<do, >')
                status = 0
            else:
                status = 62
        
        if status == 44:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'a':
                status = 45
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 45:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'r':
                status = 46
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 46:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<var, >')
                status = 0
            else:
                status = 62
                
        if status == 47:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'n':
                status = 48
            elif c == 'l':
                status = 50
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 48:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'd':
                status = 49
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 49:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ' or c == '\n' or c == '.':
                print('<end, >')
                status = 0
            else:
                status = 62

        if status == 50:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 's':
                status = 51
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 51:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'e':
                status = 52
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 52:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<else, >')
                status = 0
            else:
                status = 62
        
        if status == 53:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'h':
                status = 54
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 54:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'e':
                status = 55
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 55:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'n':
                status = 56
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 56:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<then, >')
                status = 0
            else:
                status = 62
        
        if status == 57:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'h':
                status = 58
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 58:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'i':
                status = 59
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 59:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'l':
                status = 60
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 60:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == 'e':
                status = 61
            else:
                contador_leitura = contador_leitura - 1
                status = 62
        
        if status == 61:
            contador_leitura += 1
            c = simbolo[contador_leitura]
            if c == ' ':
                print('<while, >')
                status = 0
            else:
                status = 100
        
        if status == 62:
            c = simbolo[contador_leitura]
            if c.isalnum():
                programa_nome = programa_nome + c
                contador_leitura += 1
                status = 62
            elif c == ' ' or c == '\n' or c == ';' or c == ',' or c == ':' or c == '<' or c == '>' or c == '=':
                print('<id,', programa_nome,'>')
                status = 0
                programa_nome = ''
            else:
                status = 100
        
        if status == 100:
            c = simbolo[contador_leitura]
            if (c == ' ') or (c == '\n'):
                status = 0
                contador_leitura += 1
            else:
                status = falhar(status)
                Token.token_nome = -1
                Token.token_atributo = -1
                return Token
        
    
    Token.token_nome = EOFError
    Token.token_atributo = -1
    return Token


def main():
    #simbolo = ler_arquivo("programa_certo.txt")
    simbolo = ler_arquivo("programa_errado.txt")
    token = proximo_token(simbolo, 0)

main()