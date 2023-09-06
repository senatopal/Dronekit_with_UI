from python_havalanma import Ui_havalanma
from PyQt5.QtWidgets import *
from dronekit import connect,VehicleMode,LocationGlobalRelative
import time



class Havalanma(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.havalan=Ui_havalanma()
        self.havalan.setupUi(self)
        self.havalan.pushButton.clicked.connect(self.Havalan)
        


    def Havalan(self,yukseklik):
        yukseklik=float(self.havalan.lineEdit.text())
        self.close()
        arm_ol_yuksel(yukseklik)



def arm_ol_yuksel( hedef_yukseklik):

    out="127.0.0.1:14550"
    iha=connect(out,wait_ready=True,timeout=100)
    while iha.is_armable==False:
        print("arm için gerekli sartlar sağlanamadı")
        time.sleep(1.5)
    print("iha arm edilebilir")
    iha.mode=VehicleMode("GUIDED")
    while iha.mode=="GUIDED":  # demek ki hep burada kalmıyor 
        print("GUIDED moduna geçiliyor")
        time.sleep(1.5)
    print("GUIDED moduna geçiş yapıldı")
    iha.armed=True
    while iha.mode is False:
        print("arm için bekleniliyor")
        time.sleep(1.5)
    print("iha arm oldu")
    iha.simple_takeoff(hedef_yukseklik)
    while iha.location.global_relative_frame.alt <= hedef_yukseklik*0.95:
        print("anlık yükseklik: {}".format(iha.location.global_relative_frame.alt))
        time.sleep(2)
    print("takeoff gerceklesti")


