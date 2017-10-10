from tkinter import *

class ImageButton(Button):
    def __init__(self, parent = None, **kw):
        Button.__init__(self, parent, kw)

    # 해당 widget에 숨겨진 이미지 추가
    # alphabet 인수에는 머가 들어가야하지? hidden에는 무슨 인수가 들어가야 하지?
    def add_hidden(self, alphabet, hidden):
        self.alphabet = alphabet
        self.hidden = hidden

    # 해당 widget의 숨겨진 이미지 값 return
    def get_hidden(self):
        return self.hidden