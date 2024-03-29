import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
# import matplotlib.pyplot as plt

class PyQtApp(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt Example')
        self.setGeometry(100, 100, 300, 200)
        
        self.initUI()

    def initUI(self):
        self.create_chart_layout()
        
    def create_button(self, text, callback, x=0, y=0):
        self.button = QPushButton(text, self)
        self.button.setGeometry(x, y, 100, 50) # (x, y, width, height)
        self.button.clicked.connect(callback)
        
    def create_chart_layout(self):
        layout = QVBoxLayout()

        # Create a matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
    def plot_histogram_chart(self, params):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        ax.hist(params['data'], density=False, weights = np.ones(len(params['data']))/len(params['data']), rwidth=0.95)
        ax.set_ylabel(params['ylabel'])
        ax.set_xlabel(params['xlabel'])
        ax.set_title('Probability density')
        ax.grid(axis='y')
        self.canvas.draw()

    def run(self):
        self.show()
        sys.exit(self.app.exec_())