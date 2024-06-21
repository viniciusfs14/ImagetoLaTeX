from PIL import Image
from pix2tex.cli import LatexOCR
from gui.ui_main import Ui_MainWindow 
import sys, os
from PySide6 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as fc

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ImageToLaTeX')
        
        self.pushButton.released.connect(self.locate_path)
        self.convert.released.connect(self.converter)
        self.convert.released.connect(self.show_equation)
        
        
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
        
    def show_equation(self):
        
        latex = self.linha2.text()
        
        fig = Figure(figsize=(5,2))
        ax = fig.add_subplot(111)
        
        ax.text(0.5, 0.5, f"${{{latex}}}$", fontsize =20, ha='center', va='center')
        ax.axis('off')
        
        canvas = fc(fig)
        
        for i in reversed(range(self.layout_equation.count())):
            remove = self.layout_equation.itemAt(i).widget()
            self.layout_equation.removeWidget(remove)
            remove.setParent(None)
            
        self.layout_equation.addWidget(canvas)

        
        
        
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())    

        