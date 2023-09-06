from PyQt5.QtWidgets import *
from giris import Giris

app=QApplication([])
pencere=Giris()
pencere.show()
app.exec_()
