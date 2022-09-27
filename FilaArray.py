class FilaArray():
    def __init__(self):
        self.dados = []

    def enqueue(self, elemento):
        self.dados.append(elemento)

    def dequeue(self):
        #Lembrar de tratar o erro de quando a quantidade de ações para vender for menor do que o total de ações na fila.
        return self.dados.pop(0)
        
    def first(self):
        return self.dados[0]

    def isempty(self):
        return len(self.dados) == 0

    def __len__(self):
        return len(self.dados)