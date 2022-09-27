from FilaArray import *
from DequeArray import *
fila = FilaArray()
deque = DequeArray()
saldo = 0
menu = input("COMPRAR / VENDER / (<) DESFAZER / SAIR? ")
# Loop do Menu
while menu.upper() != "SAIR":
  if menu.upper() == "COMPRAR" or menu.upper() == "VENDER":
    qtd_acoes = int(input('Quantidade de ações: '))
    valor_acoes = float(input('Valor ações R$: '))
  # Operação de Compra das ações
  if menu.upper() == "COMPRAR":
    for f in range(qtd_acoes):
      fila.enqueue(valor_acoes)
    for i in range(qtd_acoes):
      saldo -= valor_acoes
    print(fila.dados)
    print("o Saldo atual é de: R${:.2f}".format(saldo))
    lista_transacoes = []
    lista_transacoes = [fila.dados[:], saldo]
    deque.add_last(lista_transacoes[:])
    print(deque.items)
  # Operação de Vendas das Ações
  if menu.upper() == "VENDER":
    if len(fila.dados) == 0:
      print("A fila está vazia.")
    else:
      valor_vendas = qtd_acoes * valor_acoes
      for k in range(qtd_acoes):
        fila.dequeue()
      saldo += valor_vendas
      if len(fila.dados) == 0:
        print("Todas as ações foram vendidas.")
      else:
        print(fila.dados)
      print("o Saldo atual é de: R${:.2f}".format(saldo))
      lista_transacoes = []
      lista_transacoes = [fila.dados[:], saldo]
      deque.add_last(lista_transacoes[:])
  try:
    if menu == "<":
        k = deque.delete_last()
        if len(deque.items) == 0:
          fila.dados = []
          saldo = 0
          print(fila.dados)
          print(deque.items)
          print("o Saldo atual é de: R${:.2f}".format(saldo))
        else:
          fila.dados = deque.items[0][0]
          saldo = deque.items[0][1]
          print(fila.dados)
          print(deque.items)
          print("o Saldo atual é de: R${:.2f}".format(saldo))
  except:
    print("O deque está vazio.")  
  menu = input("COMPRAR / VENDER / (<) DESFAZER / SAIR? ") 

print(fila.dados)
print(deque.items)
print("o Saldo atual é de: R${:.2f}".format(saldo))

#Erros a serem tratados
#DequeVazio
#FilaVazia
#Vender mais ações do que eu tenho ou ações com lista vazia
#Tratar o deque com mais de 10 itens.