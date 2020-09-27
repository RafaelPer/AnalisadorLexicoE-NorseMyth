import ply.lex as lex
#import array as arr

consoleText = []

#Lista de palavras reservadas
reserved = {
    'Balder'    :   'PALAVRA_RESERVADA_IF',
    'Proclama'       :   'PALAVRA_RESERVADA_THEN',
    'Loki_Mente'     :   'PALAVRA_RESERVADA_ELSE',
    'Frey_for'    :   'PALAVRA_RESERVADA_FOR',
    'Frey_eq'      :   'PALAVRA_RESERVADA_WHILE',
    'heimdall_in'    :   'PALAVRA_RESERVADA_LEITURA',
    'heimdall_out'      :   'PALAVRA_RESERVADA_PRINT',
    'Yggdrasil'      :   'PALAVRA_RESERVADA_MAIN',
}

# List of token names.   This is always required
tokens = [
    'NUMERO',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'APARENTESES',
    'FPARENTESES',
    'IGUAL',
    'MAIORIGUAL',
    'MENORIGUAL',
    'MENOR',
    'MAIOR',
    'OU',
    'TERMINO',
    'IESCOPO',
    'TESCOPO',
    'ATRIBUICAO',
    'E',
    'TEXTO',
    'VARIAVEL',
    'CONCATENAR',
    'BOOLEANO',
    'FLOATDOUBLE',
    'ATRIBUICAOTIPO',
    "AASPAS",
    "FASPAS",
    'DeclaracaoVariavelInteira',
    'DeclaracaoVariavelFloat',
    'DeclaracaoVariavelBoleana',
    'DeclaracaoVariavelString',
    'DeclaracaoVariavelDouble',

] + list(reserved.values())

# Regular expression rules for simple tokens
t_SOMA    = r'\*\+\+\*'
t_SUBTRACAO   = r'\*\-\-\*'
t_MULTIPLICACAO   = r'\*\_\_\*'
t_DIVISAO  = r'\*\/\/\*'
t_IGUAL = r'\*\=\=\*'
t_MAIORIGUAL = r'\*\>\>\*\*\=\=\*'
t_MENORIGUAL = r'\*\<\<\*\*\=\=\*'
t_MENOR = r'\*\<\<\*'
t_MAIOR = r'\*\>\>\*'
t_OU = r'\*\$\$\*'
t_APARENTESES  = r'\<\.'
t_FPARENTESES  = r'\.\>'
t_TERMINO = r'\!\;'
t_IESCOPO = r'\{\!'
t_TESCOPO = r'\!\}'
t_ATRIBUICAO = r'\-\-'
t_E = r'\*\*\*\*'
t_CONCATENAR = r'\\\+\/'
t_ATRIBUICAOTIPO = r'\:'
t_AASPAS = r'\(\!'
t_FASPAS = r'\!\)'


# A regular expression rule with some action code
def t_NUMERO(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_TEXTO(t):
    r'\(\![a-zA-Z0-9\s]*\!\)'
    t.value = str(t.value)

    return t

def t_BOOLEANO(t):
    r'(true|false|1|0)'
    t.value = str(t.value)

    return t

def t_FLOATDOUBLE(t):
    r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)'

    t.value = float(t.value)

    return t

def t_ALFHEIM(t):
    r'!Frigga_[a-zA-Z0-9]+:Alfheim'
    t.type = reserved.get(t.value, 'DeclaracaoVariavelFloat')
    return t


def t_ASGARD(t):
    r'!Frigga_[a-zA-Z0-9]+:Asgard'
    t.type = reserved.get(t.value, 'DeclaracaoVariavelInteira')
    return t


def t_JOTUNHEIM(t):
    r'!Frigga_[a-zA-Z0-9]+:Jotunheim'
    t.type = reserved.get(t.value, 'DeclaracaoVariavelBoleana')
    return t


def t_MANNHEIM(t):
    r'!Frigga_[a-zA-Z0-9]+:Mannheim'
    t.type = reserved.get(t.value, 'DeclaracaoVariavelString')
    return t

def t_SVARTALFHEIM(t):
    r'!Frigga_[a-zA-Z0-9]+:Svartalfheim'
    t.type = reserved.get(t.value, 'DeclaracaoVariavelDouble')
    return t

def t_VARIAVEL(t):
    r'!Frigga_[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIAVEL')  # Check for reserved words
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    #print(t.type)
    #rw = reserved.get(t.value)
    #print(rw)
    if t.type == 'ID':
        consoleText.append("Caractere Invalido: " + t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Caractere Invalido '%s'" % t.value[0])
    consoleText.append("Caractere Invalido: "+t.value[0])
    #t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
data = '''
Yggdrasil <. .> {!
	!Frigga_teste:Mannheim -- (!teste!) !;
	!Frigga_teste1:Mannheim !;
	!Frigga_teste2:Jotunheim -- true !;
	!Frigga_cont:Asgard -- 0 !;
	!Frigga_cont:Alfheim -- 1.5 !;
	Balder <. !Frigga_teste *==* (!teste!) .> Proclama
	{!
		!Frigga_teste1 -- (!balder proclama!) !;
	!}

	Loki_Mente
	{!
		!Frigga_teste1 -- (!loki mente!) !;
	!}
	Frey_eq <. !Frigga_teste2 *==* true .> {!
		!Frigga_cont -- !Frigga_cont \+/ 1 !;
		Balder <. !Frigga_cont *==* 10 .> Proclama
		{!
			!Frigga_teste2 -- false !;
		!}
	!}
!}

'''
er = None
def realizarAnaliseLexica(file):
#def realizarAnaliseLexica():
    consoleText.clear()
    #print(file)
    lexer.input(file)
    #lexer.input(data)

    try:
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
                print("teste if not")
            consoleText.append(str(tok))
        er = "not error"
    except Exception as error:
        print(error)
        er = error
        #print(tok)
        #datas.append(str(tok))
    return consoleText, er
#teste = realizarAnaliseLexica()
#print(teste)