from objetos.ListaDeCompras import ListaDeCompras

lista1 = ListaDeCompras()
print('************************')
print('*** LISTA DE COMPRAS ***')
print('------------------------')
lista1.adicionar_item('Laranja', 10000)
lista1.adicionar_item('Cerveja', 1000)
lista1.adicionar_item('Curso da Alura', 1)
lista1.listar_itens()



def main():
    pass

if __name__ == '__main__':
    main()