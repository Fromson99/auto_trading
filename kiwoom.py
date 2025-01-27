from PyQt5.QAxContainer import *

class Kiwoom(QAxWidget):
    def __init__(slef):
        super.__init__()
        print('Kiwoom() class start.')

        self.get_ocx_instance()
    def get_ocx_instance(self):
        self.