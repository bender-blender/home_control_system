

class Lamp:
    """Лампа
    """
    def __init__(self):
        self.brightness = 0 # Яркость

    def functional(self):
        """Включить/Выключить
        """
        if self.brightness == 0:
            print("Включить лампу")
            self.brightness = 100
        else:
            print("Выключить лампу")
            self.brightness = 0