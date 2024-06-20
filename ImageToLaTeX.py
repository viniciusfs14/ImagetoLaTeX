from PIL import Image
from pix2tex.cli import LatexOCR
from gui.ui_main import Ui_MainWindow 
import sys, os
from PySide6 import QtWidgets

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.pushButton.released.connect(self.locate_path)
        self.convert.released.connect(self.converter)

        
    
    def locate_path(self):  # Calling the File Browser Widget
        data_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            caption="Search for the data file",
            filter="Png Files (*.png);;All Files (*)",
        )[0]
        self.linha.setText(data_path)
        
        
    def converter(self):
        dir = self.linha.text()
        img = Image.open(dir)
        model = LatexOCR()
        x = model(img)
        self.linha2.setText(x)
        
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())    

        