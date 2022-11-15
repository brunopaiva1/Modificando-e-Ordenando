lista_numerica = [9, 5, 2, 7, 1, 8, 3, 0, 6]
lista_animal = ['golfinho', 'água-viva', 'lobo', 'cachorroCaramelo', 'aranha']

print(lista_animal)
incluir = input('O animal que deseja tem na lista? ')
if incluir == 'sim' or incluir =='s':
    print('Programa finalizado!')
elif incluir == 'não' or incluir == 'n':
    adicionar = input('Digite o nome do animal que deseja inserir: ')
    lista_animal.append(adicionar)
    print(lista_animal)
else:
    print('ERRO! Opção Inválida, Programa finalizado')
    
remover = input('Deseja remover algum animal? ')
if remover == 'sim' or remover == 's':
    print(lista_animal)
    rem = input('Digite o animal que deseja remover: ')
    lista_animal.remove(rem)
    print(lista_animal)
elif remover == 'não' or remover == 'n':
    print('Programa finalizado')
else:
    print('ERRO! Opção Inválida, Programa finalizado')
    
lista_numerica.sort()
lista_animal.sort()

print(lista_numerica)
print(lista_animal)