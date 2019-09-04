

class Keyboard:

    def __init__(self, buttons=list()):
        self.buttons = buttons

    def to_dict(self):
        res = {
            "Type":'keyboard',
            "Buttons": self.buttons,
        }

    def setter(self):
        pass




class Button:
    def __init__(self):
        pass



