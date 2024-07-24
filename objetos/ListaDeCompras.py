class ListaDeCompras:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item=str, quantidade_item=int):
        if item == str and quantidade_item > 0:
            item_e_quant = {'item':item, 'quantidade_item':quantidade_item}
            self._itens.append(item_e_quant)

    def remover_item(self, item_a_remover=str):
        for item in self._itens:
            if item['item'] == item_a_remover:
                self._itens.remove(item)

    def listar_itens(self):
        for item in self._itens:
            nome_produto = item['item']
            quantidade = item['quantidade_item']
            print(f'Produto: {nome_produto} | Quantidade: {quantidade}')
