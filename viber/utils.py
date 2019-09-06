

class Keyboard:

    def __init__(self, buttons=list()):
        self.buttons = []
        for button in buttons:
            self.buttons.append(button.to_dict())

    def add_button(self, button):
        self.buttons.append(button.to_dict())

    def to_dict(self):
        res = {
            "Type": 'keyboard',
            "Buttons": self.buttons,
        }
        return res


class Button:

    def __init__(self, text, action_type, action_body, col, row, bg_color="#FFF124"):
        self.bg_color = bg_color
        self.text = text
        self.action_type = action_type
        self.action_body = action_body
        self.col = col
        self.row = row

    def to_dict(self):

        my_button = {
            "Columns": self.col,
            "Rows": self.row,
            "BgColor": self.bg_color,
            "ActionType": self.action_type,
            "ActionBody": self.action_body,
            "Text": self.text,
        }
        return my_button

# [{
# 			"Columns": 6,
# 			"Rows": 1,
# 			"BgColor": "#2db9b9",
# 			"BgMediaType": "gif",
# 			"BgMedia": "http://www.url.by/test.gif",
# 			"BgLoop": true,
# 			"ActionType": "open-url",
# 			"ActionBody": "www.tut.by",
# 			"Image": "www.tut.by/img.jpg",
# 			"Text": "Key text",
# 			"TextVAlign": "middle",
# 			"TextHAlign": "center",
# 			"TextOpacity": 60,
# 			"TextSize": "regular"
# 		}]


