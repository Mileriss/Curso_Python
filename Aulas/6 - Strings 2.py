curso = "Curso de Python" 
print(curso)

res = "Python" in curso #Verifica se a palavra Python está armazenada na variável curso e retorna "TRUE"
print(res)
res = "Python" not in curso #Verifica se a palavra Python está armazenada na variável curso e retorna "FALSE"
print(res)

cidade = "Sao Paulo"
dia = 30
mes = "Junho"
ano = 2022
data = "{}, {} de {} de {}" #Placeholders para armazenar as variáveis e converter INT em STRING

print(data.format(cidade,dia,mes,ano)) #Formato utilizado para realizar um Casting direto

"""
SIMBOLOS EM STRINGS
\' -> Aspas simples
\" -> Aspas duplas
\n -> Quebra de linha
\r -> Como se estivesse presisonando enter
\b -> Backspace (Retorna um espaço)
\t -> Tabulação (TAB)
"""
aspasSimples="\'Exemplo\' \'com\' \'aspas\' \'simples\'"
print(aspasSimples)
aspasDuplas="\"Exemplo\" \"com\" \"aspas\" \"duplas\""
print(aspasDuplas)
quebraDeLinha="Exemplo\n com\n quebra\n de\n linha"
print(quebraDeLinha)
backSpace="\bExemplo \bcom \bBackspace\b"
print(backSpace)
tabulacao="\tExemplo \tcom \ttabulacao"
print(tabulacao)


