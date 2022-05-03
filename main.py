from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from MainWindow import Ui_MainWindow
from IDver import card_reader2
from Glassposition import glassposition
from gantryleft import gantryleft
from valveopen import valveopen
from GlassIDTensor import GlassID
from gantryhome import gantrystayathome
from gantryright import gantryright
import time


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Status.setText("Welcome to the Bar!")
        self.Display.setVisible(True)
        self.frame_2.setVisible(False)
        self.AlcoholScreen.setVisible(False)
        self.Water.clicked.connect(self.displayFrameforWater)
        self.Alcohol.clicked.connect(self.displayFrameforAlc)
        self.WaterChecked = False
        self.AlcoholChecked = False
        self.Submit = False
        self.LiquorTyp.clicked.connect(self.displayFrameforAlcScreen)
        self.GlassTyp.clicked.connect(self.displayFrameforGlassTyp)
        self.Beer.clicked.connect(self.displayFrameforBeer)
        self.Marg.clicked.connect(self.displayFrameforMarg)
        self.Wine.clicked.connect(self.displayFrameforWine)
        self.WaterAlc.clicked.connect(self.displayFrameforWaterAlc)
        a = 0

    def resetFrame(self):
        self.Status.setText("Welcome to the Bar!")
        self.Display.setVisible(True)
        self.frame_2.setVisible(False)
        self.AlcoholScreen.setVisible(False)
        self.Water.clicked.connect(self.displayFrameforWater)
        self.Alcohol.clicked.connect(self.displayFrameforAlc)
        self.Water.setChecked(False)
        self.Alcohol.setChecked(False)
        self.LiquorTyp.setChecked(False)
        self.GlassTyp.setChecked(False)
        self.Wine.setChecked(False)
        self.Beer.setChecked(False)
        self.Marg.setChecked(False)
        self.WaterAlc.setChecked(False)
        a = 0

    def displayFrameforWater(self, checked):
        self.WaterChecked = checked
        print("Water Checked", self.WaterChecked)
        if (self.WaterChecked):
            self.Display.setVisible(True)
            self.Status.setText("Place your glass on the coaster")
            QtTest.QTest.qWait(4000)
            self.Status.setText("Identifying Position")
            QtTest.QTest.qWait(2000)
            pos = glassposition(self)
            if (pos == "no"):
                gantrystayathome(self)
            elif (pos == "left"):
                gantryleft(self)
            elif (pos == "right"):
                gantryright(self)

            self.Status.setText("Identifying Glass")
            QtTest.QTest.qWait(2000)
            a = "water"
            if (str(a) == "margarita"):
                #OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self,'D')
            elif (str(a) == "wine"):
                #OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'A')
            elif (str(a) == "coffee"):
                #OpenWaterforCoffeeTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'C')
            elif (str(a) == "water"):
                #OpenWaterforWaterTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'B')
                QtTest.QTest.qWait(28000)
                if (pos == "left"):
                    gantryright(self)
                    QtTest.QTest.qWait(5000)
                elif (pos == "right"):
                    gantryleft(self)
                    QtTest.QTest.qWait(5000)
            QtTest.QTest.qWait(2000)
            self.Status.setText("Enjoy your drink! Thank you!")
            QtTest.QTest.qWait(5000)
            self.resetFrame()

        else:
            self.Display.setVisible(False)

    def displayFrameforAlc(self, checked):
        self.AlcoholChecked = checked

        print(self.AlcoholChecked)
        if (self.AlcoholChecked):
            self.Display.setVisible(True)
            self.Status.setText("Place your ID in ID Scanner")
            QtTest.QTest.qWait(5000)
            self.Status.setText("Verifying ID")
            QtTest.QTest.qWait(3000)
            a = card_reader2(self)
            if (a > 21):
                self.Status.setText("Your age is " + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("ID Verified.")
                QtTest.QTest.qWait(2000)
                self.Status.setText("Place your glass on the coaster")
                QtTest.QTest.qWait(5000)
                pos = str(glassposition(self))
                print(pos)
                if (pos == "no"):
                    self.Status.setText("No Glass placed")
                    QtTest.QTest.qWait(4000)
                    self.resetFrame()
                elif (pos == "left"):
                    self.Status.setText("Glass on Left")
                    QtTest.QTest.qWait(4000)
                    self.AlcoholScreen.setVisible(True)
                elif (pos == "right"):
                    self.Status.setText("Glass on Right")
                    QtTest.QTest.qWait(2000)
                    self.AlcoholScreen.setVisible(True)

            elif (a < 21):
                self.Status.setText("You're young! Go play.")
                self.close()
        else:
            self.Display.setVisible(False)
            self.AlcoholScreen.setVisible(False)

    def displayFrameforAlcScreen(self):
        if (self.LiquorTyp):
            self.frame_2.setVisible(True)
            self.Status.setText("Choose your Liquor")
        else:
            self.Status.setText("Please select an option")
            self.frame_2.setVisible(False)

    def displayFrameforGlassTyp(self, checked):
        self.GlassTyp = checked
        if (self.GlassTyp):
            self.frame_2.setVisible(False)
            a = GlassID(self)
            if (str(a) == "margarita"):
                # OpenMargaritaforMargaritaTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'P')
            elif (str(a) == "wine"):
                # Open Wine for Wine Time
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'E')
            elif (str(a) == "coffee"):
                # Open Coffee for Coffee Time
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'K')
            elif (str(a) == "water"):
                # Open Water for Water Time
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'B')
        else:
            self.Status.setText("Please select an option")
            self.frame_2.setVisible(False)

    def displayFrameforBeer(self):
        if (self.Beer):
            self.Status.setText("Identifying Position")
            QtTest.QTest.qWait(2000)
            pos = glassposition(self)
            if (pos == "no"):
                gantrystayathome(self)
            elif (pos == "left"):
                gantryleft(self)
            elif (pos == "right"):
                gantryright(self)

            self.Status.setText("Position Identified")
            QtTest.QTest.qWait(2000)
            self.Status.setText("Identifying Glass")
            QtTest.QTest.qWait(2000)
            a = "Beer"
            if (str(a) == "margarita"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'L')
            elif (str(a) == "wine"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'I')
            elif (str(a) == "Beer"):
                # OpenWaterforCoffeeTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'K')
                QtTest.QTest.qWait(18000)
                if (pos == "left"):
                    gantryright(self)
                    QtTest.QTest.qWait(5000)
                elif (pos == "right"):
                    gantryleft(self)
                    QtTest.QTest.qWait(5000)
            elif (str(a) == "water"):
                # OpenWaterforWaterTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'J')
            QtTest.QTest.qWait(2000)

            self.Status.setText("Enjoy your drink! Thank you!")
            QtTest.QTest.qWait(5000)
            self.resetFrame()

        else:
            self.Status.setText("Please select an option")

    def displayFrameforMarg(self):

        if (self.Marg):

            self.Status.setText("Identifying Position")
            QtTest.QTest.qWait(2000)
            pos = glassposition(self)
            if (pos == "no"):
                gantrystayathome(self)
            elif (pos == "left"):
                gantryleft(self)
            elif (pos == "right"):
                gantryright(self)

            self.Status.setText("Position Identified")
            QtTest.QTest.qWait(2000)
            self.Status.setText("Identifying Glass")
            QtTest.QTest.qWait(2000)
            a = "margarita"
            if (str(a) == "margarita"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'P')
                QtTest.QTest.qWait(15000)
                if (pos == "left"):
                    gantryright(self)
                    QtTest.QTest.qWait(5000)
                elif (pos == "right"):
                    gantryleft(self)
                    QtTest.QTest.qWait(5000)
            elif (str(a) == "wine"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'M')
            elif (str(a) == "coffee"):
                # OpenWaterforCoffeeTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'O')
            elif (str(a) == "water"):
                # OpenWaterforWaterTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'N')
            QtTest.QTest.qWait(2000)
            self.Status.setText("Enjoy your drink! Thank you!")
            QtTest.QTest.qWait(5000)
            self.resetFrame()
        else:
            self.Status.setText("Please select an option")

    def displayFrameforWine(self):
        if (self.Wine):

            self.Status.setText("Identifying Position")
            QtTest.QTest.qWait(2000)
            pos = glassposition(self)
            if (pos == "no"):
                gantrystayathome(self)
            elif (pos == "left"):
                gantryleft(self)
            elif (pos == "right"):
                gantryright(self)

            self.Status.setText("Position Identified")
            QtTest.QTest.qWait(2000)
            self.Status.setText("Identifying Glass")
            QtTest.QTest.qWait(2000)
            a = "wine"
            if (str(a) == "margarita"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'H')
            elif (str(a) == "wine"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'E')
                QtTest.QTest.qWait(25000)
                if (pos == "left"):
                    gantryright(self)
                    QtTest.QTest.qWait(5000)
                elif (pos == "right"):
                    gantryleft(self)
                    QtTest.QTest.qWait(5000)
            elif (str(a) == "coffee"):
                # OpenWaterforCoffeeTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'G')
            elif (str(a) == "water"):
                # OpenWaterforWaterTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'F')
            QtTest.QTest.qWait(2000)

            self.Status.setText("Enjoy your drink! Thank you!")
            QtTest.QTest.qWait(5000)
            self.resetFrame()
        else:
            self.Status.setText("Please select an option")

    def displayFrameforWaterAlc(self):

        if (self.WaterAlc):
            self.Status.setText("Identifying Position")
            QtTest.QTest.qWait(2000)
            pos = glassposition(self)
            if (pos == "no"):
                gantrystayathome(self)
            elif (pos == "left"):
                gantryleft(self)
            elif (pos == "right"):
                gantryright(self)

            self.Status.setText("Position Identified")
            QtTest.QTest.qWait(2000)
            self.Status.setText("Identifying Glass")
            QtTest.QTest.qWait(2000)
            a = "water"
            if (str(a) == "margarita"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'D')
            elif (str(a) == "wine"):
                # OpenWaterforWineTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'A')
            elif (str(a) == "coffee"):
                # OpenWaterforCoffeeTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'C')
            elif (str(a) == "water"):
                # OpenWaterforWaterTime
                self.Status.setText("Glass Identified" + str(a))
                QtTest.QTest.qWait(2000)
                self.Status.setText("Pouring")
                valveopen(self, 'B')
                QtTest.QTest.qWait(28000)
                if (pos == "left"):
                    gantryright(self)
                    QtTest.QTest.qWait(5000)
                elif (pos == "right"):
                    gantryleft(self)
                    QtTest.QTest.qWait(5000)
            QtTest.QTest.qWait(2000)
            self.Status.setText("Enjoy your drink! Thank you!")
            QtTest.QTest.qWait(5000)
            self.resetFrame()
        else:
            self.Status.setText("Please select an option")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
