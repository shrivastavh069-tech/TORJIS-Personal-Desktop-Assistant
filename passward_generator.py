import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow,QApplication
from passed import Ui_MainWindow as weUI
import random
import string


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=weUI()
        self.ui.setupUi(self)
        self.clear()
        self.ui.copy.clicked.connect(self.copy)
        self.ui.pushButton.clicked.connect(self.password)
        self.ui.recreate.clicked.connect(self.password)
        self.ui.criteria.clicked.connect(self.clear)
        self.ui.ok.clicked.connect(self.hide)
        

        
    def password(self):
        lis=[]

        if self.ui.upp.isChecked():
            lis.append("upp")
        if self.ui.low.isChecked():
            lis.append("low")
        if self.ui.digit.isChecked():
            lis.append("dig")
        if self.ui.pun.isChecked():
            lis.append("pun")

            
        user_pass=""
        length=int(self.ui.length.text())            
        if (len(lis)) < 2:
            self.ui.warning.show()
            QTimer.singleShot(1000,self.clear)
            return

            
        elif  length < 8 :
            self.ui.warning_2_box.show()
            self.ui.warning_3.show()
            self.ui.warning_3_1.show()
            QTimer.singleShot(1000,self.clear)
            return
            
        
        i=0
        while i<length:
            user=self.call(lis)
            if user == "dig":
                user_pass +=random.choice(string.digits)
            if user == "upp":
                user_pass +=random.choice(string.ascii_uppercase)
            if user == "low":
                user_pass +=random.choice(string.ascii_lowercase)
            if user == "pun":    
                user_pass +=random.choice(string.punctuation)
            i+=1
            
    
        
        self.ui.dec7.show()
        self.ui.dec8.show()
        self.ui.copy.show()
        self.ui.genpass.show()
        self.ui.ok.show()
        self.ui.criteria.show()
        self.ui.recreate.show()
        self.ui.genpass.setText(user_pass)
            
            

    def call (self,lis):
        user=random.choice(lis)
        return(user)

    def copy(self):
        password=self.ui.genpass.text()
        QApplication.clipboard().setText(password)
        
    def clear (self):
        self.ui.warning.hide()
        self.ui.recreate.hide()
        self.ui.criteria.hide()
        self.ui.warning_2_box.hide()
        self.ui.dec7.hide()
        self.ui.warning_3_1.hide()
        self.ui.warning_3.hide()
        self.ui.dec8.hide()
        self.ui.copy.hide()
        self.ui.genpass.hide()
        self.ui.ok.hide()
        
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =GUI()
    window.show()      
    sys.exit(app.exec())
