first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip() #cancela os espaços
first_value = first_value.lower() #coloca todos os caracteres no maiusculo
first_value = first_value.title() #apenas o primeiro caractere de cada palavra fica maiusuclo
first_value = f'{first_value:^30}' #centraliza a string em meio de 30 caracteres

# Second challenge
second_value = second_value.replace('-','') #substitui os - por espaços vazios
second_value = second_value.strip()
second_value = second_value.capitalize() #deixa apenas a primeira letra da primeira palavra maiuscula

# Third challenge
third_value = third_value.replace(' ','')
third_value = third_value.replace('-','')
third_value = third_value.swapcase() #reverte os maiusculos/minusculos
third_value = f'{third_value:>30}' #espaço com 30 caractres

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#',end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')