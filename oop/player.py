class Player:
    pass

a = Player()
a.name = "sean"
a.color = "orange"

print(a.name)
print(a.color)

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

a = Player('sean', 'orange')

print(a.name)
print(a.color)