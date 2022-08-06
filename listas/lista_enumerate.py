# Preparar uma lista para salvar em txt
# Recuperar dados txt para gerar uma lista

# Gera string para salvar em txt separando campos por ';'
frutas = ['Banana', 'Maça', 'Melancia', 'Limão', 'Laranja']
linha = ''
for indice, fruta in enumerate(frutas):
    if indice < len(frutas) - 1:
        linha += fruta + ';'
    else:
        linha += fruta + '\n'

print(linha)

# Prepara uma string separada por ; e gera uma lista
frutas.clear()
fruta = ''

for letra in linha:
    if letra not in ';\n':
        fruta += letra
    else:
        frutas.append(fruta)
        fruta = ''

print(frutas)
