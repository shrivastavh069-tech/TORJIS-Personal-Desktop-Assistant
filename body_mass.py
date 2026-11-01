import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QTimer
from status import Ui_MainWindow as bmiUI

class calculate (QMainWindow):
    def __init__(self):
        super() .__init__()
        self.ui=bmiUI()
        self.ui.setupUi(self)
        self.hide_label("ok")
        self.hide_label("name")
        self.hide_label("height")
        self.hide_label("weight")
        self.hide_label("stacked")
        self.hide_label("label_4")
        self.hide_label("label_3")
        self.ui.status_2.clicked.connect(self.results)
        self.ui.ok.clicked.connect(self.reset)
    def results (self):
        self.hide_label("ok")
        self.hide_label("name")
        self.hide_label("height")
        self.hide_label("weight")
        self.hide_label("stacked")
        self.hide_label("label_4")
        self.hide_label("label_3")
        name_bar=self.ui.name_bar.text().strip().upper()
        height_bar=int(self.ui.height_bar.text())
        weight_bar=int(self.ui.weight_bar.text())
        if not name_bar:
            self.ui.invalid_name.show()
            QTimer.singleShot(1000,self.ui.invalid_name.hide)
            return
        elif not height_bar:
            self.ui.invalid_height.show()
            QTimer.singleShot(1000,self.ui.invalid_height.hide)
            return
        elif not weight_bar:
            self.ui.invalid_weight.show()
            QTimer.singleShot(1000,self.ui.invalid_weight.hide)
            return
        height_bar=float(height_bar)
        weight_bar=float(weight_bar)

        result=weight_bar/((height_bar/100)**2)
        if result <18.5:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.lineEdit_3.setText(f"{result:.1f}")
        elif result < 24.5:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lineEdit.setText(f"{result:.1f}")
        elif result <29.9:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.lineEdit_5.setText(f"{result:.1f}")
        elif result >=30.0:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.lineEdit_2.setText(f"{result:.1f}")
        self.ui.ok.show()
        self.ui.label_3.show()
        self.ui.label_4.show()
        self.ui.stackedWidget.show()
            
        
    def hide_label (self,hide):
        if hide == "ok":
            self.ui.ok.hide()
        elif hide == "label_3":
            self.ui.label_3.hide()
        elif hide == "stacked":
            self.ui.stackedWidget.hide()
        elif hide == "label_4":
            self.ui.label_4.hide()
        elif hide =="name":
            self.ui.invalid_name.hide()
        elif hide =="height":
            self.ui.invalid_height.hide()
        elif hide =="weight":
            self.ui.invalid_weight.hide()


    def reset(self):
        self.ui.name_bar.clear()
        self.ui.height_bar.clear()
        self.ui.weight_bar.clear()
        self.ui.invalid_name.hide()
        self.ui.invalid_height.hide()
        self.ui.invalid_weight.hide()
        self.ui.ok.hide()
        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.stackedWidget.hide()
        self.ui.radioButton.setEnabled(True)
        self.ui.radioButton_2.setEnabled(True)

if __name__ =="__main__":        
    app=QApplication(sys.argv)
    Window=calculate()
    Window.show()
    sys.exit(app.exec())
