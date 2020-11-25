class Cidade:

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __getX__(self):
        return self.x

    def __getY__(self):
        return self.y

    def __getID__(self):
        return self.id

    def all(self):
        return [self.id, self.x, self.y]
