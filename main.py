# Класс
class Hero:
    # Конструктор класса
    def __init__(self, name = "John Doe", lvl = 1, hp = 100):
        # Атрибуты класса
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp

    # Метод класса
    def action(self):
        print(f"Базовое действие {self.name_1}")



# Экземпляр класс| Объект класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero(hp = 1000, name = "Asuna", lvl = 98)



# kirito.action()
# asuna.action()

print(asuna.hp_1)