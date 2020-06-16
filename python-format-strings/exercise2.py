# capitalize é uma função que diexa o primeira caractere de uma string maiúsculo
message = str.capitalize('first message')
print(message) #chamando a função str tendo como argumento a string
message = 'second message'.capitalize()
print(message.capitalize()) # a função opera no string literal e não é necessário ser passado nenhum argumento
message = 'third message'
print(message.capitalize()) #chama a função como membro da variável
#pode-se usar os 3 exemplos mas o mais comum é o terceiro


message = 'hello world'
print(message.lower()) #minusculo
print(message.upper()) #maiusculo

message = message.title() #maiuscula em todos os caracteres iniciais
print(message)
print(message.swapcase()) #minusculo nos caracteres iniciais


location = 'Mississippi'
print(location.count('s')) #quantidade de letras definida
print(len('how many letters in this string?')) #quantidade de letras na string


message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))
#retorna valores booleanos caso a string comece ou termine com os caracteres citados


message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))
#começando do 0, retorna em que posição está o caractere x, se não tiver o caractere retorna -1



message = '    middle     '
print('.' + message.lstrip() + '.')
#remove os espaços do lado esquerdo da string
print('.' + message.rstrip() + '.')
#remove os espaços do lado direito da string
print('.' + message.strip() + '.')
#remove dos dois lados



message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
#troca uma palavra especifica dentro de uma string """


message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))
#adiciona espaços 