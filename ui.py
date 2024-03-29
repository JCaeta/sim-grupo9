import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QGroupBox,
    QLabel,
    QSizePolicy,
    QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtCore import Qt

class PyQtApp(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt Example')
        self.setGeometry(100, 100, 500, 300)
        
        self.group_box = None
        self.widgets_layout = None
        self.grid = None
        self.button_width = 100
        self.input_width = 50
        self.input_height = 25
        self.button_height = 25
        
        self.create_grid()
        self.create_group_box()
        self.init_ui()
        
    def init_ui(self):
        self.create_chart_layout()
        
    def create_grid(self):
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(20) 
        self.grid.setVerticalSpacing(10) 
        self.grid.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.grid)
        
    def create_group_box(self):
        self.group_box = QGroupBox("Controles", self)
        self.widgets_layout = QHBoxLayout()
        self.group_box.setLayout(self.widgets_layout)
        self.grid.addWidget(self.group_box, 0, 0, 1, 1)
        
    def create_button(self, text, callback):
        button = QPushButton(text, self)
        button.setFixedSize(self.button_width, self.button_height)
        button.clicked.connect(callback)
        self.widgets_layout.addWidget(button)

    def create_input(self, text, callback, width = None):
        if width == None:
            width = self.input_width
            
        def print_callback():
            print("Return pressed!")
            callback()
            
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(text)
        input_field.setFixedSize(width, self.input_height)
        # input_field.returnPressed.connect(print_callback)
        # input_field.keyPressEvent()
        self.widgets_layout.addWidget(input_field)
        return input_field
        
    def create_chart_layout(self):
        # Create a matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.grid.addWidget(self.canvas, 1, 0, 5, 1)
        
    def plot_histogram_chart(self, params):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        ax.hist(params['data'], density=False, weights = np.ones(len(params['data']))/len(params['data']), rwidth=0.95)
        ax.set_ylabel(params['ylabel'])
        ax.set_xlabel(params['xlabel'])
        ax.set_title('Histograma')
        ax.grid(axis='y')
        self.canvas.draw()

    def run(self):
        self.showMaximized()
        sys.exit(self.app.exec_())