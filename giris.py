from python_giris import Ui_MainWindow
from PyQt5.QtWidgets import *
from havalanma import Havalanma
from konumbilgileri import Konum
from dronekit import connect,VehicleMode,LocationGlobalRelative
import time

class Giris(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.giris=Ui_MainWindow()
        self.giris.setupUi(self)
        self.havalan=Havalanma()
        self.konum=Konum()
        self.giris.pushButton_havalan.clicked.connect(self.gitHavalan)
        self.giris.pushButton_konumgit.clicked.connect(self.gitKonum)
        self.giris.pushButtonKonum.clicked.connect(self.anlikKonum)
        self.giris.pushButton_inis.clicked.connect(self.inis)
        self.giris.pushButton.clicked.connect(self.baslangic)
        
    def gitHavalan(self):
        self.havalan.show()
        self.hide()
    def gitKonum(self):
        self.konum.show()
        self.hide()
    
    def anlikKonum(self):
        self.hide()
        out = "127.0.0.1:14550"
        try:
            iha = connect(out, wait_ready=True, timeout=100)
            print("İha konum bilgisi veriliyor...")
            print(iha.location.global_relative_frame)
        except Exception as e:
            print("Bağlantı hatası:", e)

        # Belirli bir süre boyunca belirli bir durumu kontrol et
        baslangic_zamani = time.time()
        bekleme_suresi = 10  # 10 saniye bekleyelim

        while True:
            gecen_sure = time.time() - baslangic_zamani
            if gecen_sure >= bekleme_suresi:
                break
            time.sleep(1)
        

    def inis(self):
       out="127.0.0.1:14550"
       try:
        iha = connect(out, wait_ready=True, timeout=100)
        
        if iha.mode == "GUIDED":
            iha.mode = VehicleMode("LAND")
            while iha.mode.name != "LAND":
                time.sleep(1)
                print("İniş yapılıyor...")
        
        iha.armed = False
        while iha.armed:
            time.sleep(1)
        
        iha.close()
        print("İHA indirildi ve bağlantı kapatıldı.")
       except Exception as e:
        print("Hata:", e)
    
    def baslangic(self):
        self.hide()
        out="127.0.0.1:14550"
        iha=connect(out,wait_ready=True,timeout=100)
        iha.mode=VehicleMode("RTL")
        while not iha.mode.name== "RTL":
            time.sleep(1)
        print("Başlangıç noktasına gidildi.")