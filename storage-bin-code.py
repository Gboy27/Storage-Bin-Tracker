import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
import sqlite3

#This dict helps keep track of whether or not a bin was created by filling the value, while also defining the order in which bins are created
bins = {
    "pb1": "",
    "pb2": "",
    "pb3": "",
    "pb4": "",
    "pb5": "",
    "pb6": "",
    "pb7": "",
    "pb8": "",
    "pb9": "",
    "pb10": "",
    "pb11": "",
    "pb12": "",
}

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("storage_bin_tracker_welcome_screen.ui", self)
        self.initUI()
        self.initcovers()

    def initcovers(self):
        
        #These initialize the covers for each bin showing that they are either not created or have been deleted.
        self.pb1c.setHidden(False)
        self.pb2c.setHidden(False)
        self.pb3c.setHidden(False)
        self.pb4c.setHidden(False)
        self.pb5c.setHidden(False)
        self.pb6c.setHidden(False)
        self.pb7c.setHidden(False)
        self.pb8c.setHidden(False)
        self.pb9c.setHidden(False)
        self.pb10c.setHidden(False)
        self.pb11c.setHidden(False)
        self.pb12c.setHidden(False)

        #These buttons when clicked will hide the contents of a specific bin
        self.bb1.setHidden(True)
        self.bb2.setHidden(True)
        self.bb3.setHidden(True)
        self.bb4.setHidden(True)
        self.bb5.setHidden(True)
        self.bb6.setHidden(True)
        self.bb7.setHidden(True)
        self.bb8.setHidden(True)
        self.bb9.setHidden(True)
        self.bb10.setHidden(True)
        self.bb11.setHidden(True)
        self.bb12.setHidden(True)

    def initUI(self):
        #Here we are hiding the bins not created yet so that they are revealed and renamed when the user wants them to be
        self.pb1.setHidden(True)
        self.pb2.setHidden(True)
        self.pb3.setHidden(True)
        self.pb4.setHidden(True)
        self.pb5.setHidden(True)
        self.pb6.setHidden(True)
        self.pb7.setHidden(True)
        self.pb8.setHidden(True)
        self.pb9.setHidden(True)
        self.pb10.setHidden(True)
        self.pb11.setHidden(True)
        self.pb12.setHidden(True)

        #When a created bin is clicked, it will show what is inside the bin
        self.pb1.clicked.connect(lambda: self.openBin(self.pb1,self.bb1))
        self.pb2.clicked.connect(lambda: self.openBin(self.pb2,self.bb2))
        self.pb3.clicked.connect(lambda: self.openBin(self.pb3,self.bb3))
        self.pb4.clicked.connect(lambda: self.openBin(self.pb4,self.bb4))
        self.pb5.clicked.connect(lambda: self.openBin(self.pb5,self.bb5))
        self.pb6.clicked.connect(lambda: self.openBin(self.pb6,self.bb6))
        self.pb7.clicked.connect(lambda: self.openBin(self.pb7,self.bb7))
        self.pb8.clicked.connect(lambda: self.openBin(self.pb8,self.bb8))
        self.pb9.clicked.connect(lambda: self.openBin(self.pb9,self.bb9))
        self.pb10.clicked.connect(lambda: self.openBin(self.pb10,self.bb10))
        self.pb11.clicked.connect(lambda: self.openBin(self.pb11,self.bb11))
        self.pb12.clicked.connect(lambda: self.openBin(self.pb12,self.bb12))

        #When a user wants to hide the cotents of the bin, these buttons are clicked
        self.bb1.clicked.connect(lambda: self.closeBin(self.pb1,self.bb1))
        self.bb2.clicked.connect(lambda: self.closeBin(self.pb2,self.bb2))
        self.bb3.clicked.connect(lambda: self.closeBin(self.pb3,self.bb3))
        self.bb4.clicked.connect(lambda: self.closeBin(self.pb4,self.bb4))
        self.bb5.clicked.connect(lambda: self.closeBin(self.pb5,self.bb5))
        self.bb6.clicked.connect(lambda: self.closeBin(self.pb6,self.bb6))
        self.bb7.clicked.connect(lambda: self.closeBin(self.pb7,self.bb7))
        self.bb8.clicked.connect(lambda: self.closeBin(self.pb8,self.bb8))
        self.bb9.clicked.connect(lambda: self.closeBin(self.pb9,self.bb9))
        self.bb10.clicked.connect(lambda: self.closeBin(self.pb10,self.bb10))
        self.bb11.clicked.connect(lambda: self.closeBin(self.pb11,self.bb11))
        self.bb12.clicked.connect(lambda: self.closeBin(self.pb12,self.bb12))

        #This is connected to an error message that will appear if user tries to make the name of a bin an empty string. There is no error for duplicate
        #- bins being named the same, but this does not interfere with the way bins hold data or are deleted.
        self.ERROR_EMPTYSTRING.setHidden(True)

        #If the add or delete a bin button is clicked, this code is executed
        self.addABin.clicked.connect(self.revealBin)
        self.del_B.clicked.connect(self.deleteBin)

        #This points to the saveAllContent()function
        #self.saveButton.clicked.connect(self.saveAllContent)


    #These 2 functions hide and reveal the contents of a bin

    def openBin(self,pb,bb):
        if pb.clicked:
            pb.setHidden(True)
            bb.setHidden(False)
    def closeBin(self,pb,bb):
        if bb.clicked:
            pb.setHidden(False)
            bb.setHidden(True)

    def revealBin(self):
        #Iterates through the creation of each bin, setting their order.
        userinput = self.le_getName.text()
        if userinput != "":
            self.ERROR_EMPTYSTRING.setHidden(True)
            value = bins["pb1"]
            if value == "":
                bins["pb1"]=userinput
                addBin(self,self.pb1,self.pb1c,userinput)
            else:
                value = bins["pb2"]
                if value == "":
                    bins["pb2"]=userinput
                    addBin(self,self.pb2,self.pb2c,userinput)
                else:
                    value = bins["pb3"]
                    if value == "":
                        bins["pb3"]=userinput
                        addBin(self,self.pb3,self.pb3c,userinput)
                    else:
                        value = bins["pb4"]
                        if value == "":
                            bins["pb4"]=userinput
                            addBin(self,self.pb4,self.pb4c,userinput)
                        else:
                            value = bins["pb5"]
                            if value == "":
                                bins["pb5"]=userinput
                                addBin(self,self.pb5,self.pb5c,userinput)
                            else:
                                value = bins["pb6"]
                                if value == "":
                                    bins["pb6"]=userinput
                                    addBin(self,self.pb6,self.pb6c,userinput)
                                else:
                                    value = bins["pb7"]
                                    if value == "":
                                        bins["pb7"]=userinput
                                        addBin(self,self.pb7,self.pb7c,userinput)
                                    else:
                                        value = bins["pb8"]
                                        if value == "":
                                            bins["pb8"]=userinput
                                            addBin(self,self.pb8,self.pb8c,userinput)
                                        else:
                                            value = bins["pb9"]
                                            if value == "":
                                                bins["pb9"]=userinput
                                                addBin(self,self.pb9,self.pb9c,userinput)
                                            else:
                                                value = bins["pb10"]
                                                if value == "":
                                                    bins["pb10"]=userinput
                                                    addBin(self,self.pb10,self.pb10c,userinput)
                                                else:
                                                    value = bins["pb11"]
                                                    if value == "":
                                                        bins["pb11"]=userinput
                                                        addBin(self,self.pb11,self.pb11c,userinput)
                                                    else:
                                                        value = bins["pb12"]
                                                        if value == "":
                                                            bins["pb12"]=userinput
                                                            addBin(self,self.pb12,self.pb12c,userinput)
        else:
            self.ERROR_EMPTYSTRING.setHidden(False)

    def deleteBin(self):
        #This function reads which bin to delete, then resets the selected bin and the contents inside
        userinput = self.le_getBinID.text()
        if userinput == "Bin 1":
            bins["pb1"]=""
            resetBin(self,self.pb1,self.pb1c,self.bb1,self.b1l1,self.b1l2,self.b1l3,self.b1l4,self.b1l5,self.b1l6,self.b1l7,self.b1l8,self.b1l9,self.b1l10,self.b1l11,self.b1l12)
        elif userinput == "Bin 2":
            bins["pb2"]=""
            resetBin(self,self.pb2,self.pb2c,self.bb2,self.b2l1,self.b2l2,self.b2l3,self.b2l4,self.b2l5,self.b2l6,self.b2l7,self.b2l8,self.b2l9,self.b2l10,self.b2l11,self.b2l12)
        elif userinput == "Bin 3":
            bins["pb3"]=""
            resetBin(self,self.pb3,self.pb3c,self.bb3,self.b3l1,self.b3l2,self.b3l3,self.b3l4,self.b3l5,self.b3l6,self.b3l7,self.b3l8,self.b3l9,self.b3l10,self.b3l11,self.b3l12)
        elif userinput == "Bin 4":
            bins["pb4"]=""
            resetBin(self,self.pb4,self.pb4c,self.bb4,self.b4l1,self.b4l2,self.b4l3,self.b4l4,self.b4l5,self.b4l6,self.b4l7,self.b4l8,self.b4l9,self.b4l10,self.b4l11,self.b4l12)
        elif userinput == "Bin 5":
            bins["pb5"]=""
            resetBin(self,self.pb5,self.pb5c,self.bb5,self.b5l1,self.b5l2,self.b5l3,self.b5l4,self.b5l5,self.b5l6,self.b5l7,self.b5l8,self.b5l9,self.b5l10,self.b5l11,self.b5l12)
        elif userinput == "Bin 6":
            bins["pb6"]=""
            resetBin(self,self.pb6,self.pb6c,self.bb6,self.b6l1,self.b6l2,self.b6l3,self.b6l4,self.b6l5,self.b6l6,self.b6l7,self.b6l8,self.b6l9,self.b6l10,self.b6l11,self.b6l12)
        elif userinput == "Bin 7":
            bins["pb7"]=""
            resetBin(self,self.pb7,self.pb7c,self.bb7,self.b7l1,self.b7l2,self.b7l3,self.b7l4,self.b7l5,self.b7l6,self.b7l7,self.b7l8,self.b7l9,self.b7l10,self.b7l11,self.b7l12)
        elif userinput == "Bin 8":
            bins["pb8"]=""
            resetBin(self,self.pb8,self.pb8c,self.bb8,self.b8l1,self.b8l2,self.b8l3,self.b8l4,self.b8l5,self.b8l6,self.b8l7,self.b8l8,self.b8l9,self.b8l10,self.b8l11,self.b8l12)
        elif userinput == "Bin 9":
            bins["pb9"]=""
            resetBin(self,self.pb9,self.pb9c,self.bb9,self.b9l1,self.b9l2,self.b9l3,self.b9l4,self.b9l5,self.b9l6,self.b9l7,self.b9l8,self.b9l9,self.b9l10,self.b9l11,self.b9l12)
        elif userinput == "Bin 10":
            bins["pb10"]=""
            resetBin(self,self.pb10,self.pb10c,self.bb10,self.b10l1,self.b10l2,self.b10l3,self.b10l4,self.b10l5,self.b10l6,self.b10l7,self.b10l8,self.b10l9,self.b10l10,self.b10l11,self.b10l12)
        elif userinput == "Bin 11":
            bins["pb11"]=""
            resetBin(self,self.pb11,self.pb11c,self.bb11,self.b11l1,self.b11l2,self.b11l3,self.b11l4,self.b11l5,self.b11l6,self.b11l7,self.b11l8,self.b11l9,self.b11l10,self.b11l11,self.b11l12)
        elif userinput == "Bin 12":
            bins["pb12"]=""
            resetBin(self,self.pb12,self.pb12c,self.bb12,self.b12l1,self.b12l2,self.b12l3,self.b12l4,self.b12l5,self.b12l6,self.b12l7,self.b12l8,self.b12l9,self.b12l10,self.b12l11,self.b12l12)


def addBin(self,pb,pbc,userinput):
    pbc.setHidden(True)
    pb.setHidden(False)
    pb.setText(userinput)

#This function deletes a created bin and all of the contents within it
def resetBin(self,pb,pbc,bb,bl1,bl2,bl3,bl4,bl5,bl6,bl7,bl8,bl9,bl10,bl11,bl12):
        pb.setHidden(True)
        pbc.setHidden(False)
        bb.setHidden(True)
        bl1.clear()
        bl2.clear()
        bl3.clear()
        bl4.clear()
        bl5.clear()
        bl6.clear()
        bl7.clear()
        bl8.clear()
        bl9.clear()
        bl10.clear()
        bl11.clear()
        bl12.clear()

app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
#.setWindowTitle("Storage Bin Tracker")
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(850)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("exiting")

