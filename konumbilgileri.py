from python_konumbilgileri import Ui_konumbilgi
from PyQt5.QtWidgets import *
from dronekit import connect,VehicleMode,LocationGlobalRelative
import time

class Konum(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.konum=Ui_konumbilgi()
        self.konum.setupUi(self)
        self.konum.pushButton.clicked.connect(self.GitKonum)

    def GitKonum(self):
        self.close()
        out="127.0.0.1:14550"
        iha=connect(out,wait_ready=True,timeout=100)        
        x=float(self.konum.lineEdit_x.text())
        y=float(self.konum.lineEdit_y.text())
        z=float(self.konum.lineEdit_z.text())

        lokasyon=LocationGlobalRelative(x,y,z)
        iha.simple_goto(lokasyon)
        


