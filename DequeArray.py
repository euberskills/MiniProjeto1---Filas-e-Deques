class DequeArray:
    def __init__(self, CAPACIDADE_MAXIMA = 10):
        self.CAPACIDADE_MAXIMA = CAPACIDADE_MAXIMA
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_first(self, item):
        self.items.append(item)

    def add_last(self, item):
        self.items.insert(0,item)

    def delete_first(self):
        return self.items.pop()

    def delete_last(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)