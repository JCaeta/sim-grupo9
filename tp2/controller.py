from ui_utils import PyQtApp
from generators import normalDist
from generators import mixedCongruentGenerator

class Controller:
    def __init__(self):
        self.ui = PyQtApp() # Es la clase que hace toda la parte gráfica
        self.create_buttons()
    
    def create_buttons(self):
        button_width = 100
        self.ui.create_button(
            'Dist Uniforme', 
            self.create_uniform_distribution, 
            10,
            10)
        
        self.ui.create_button(
            'Dist Exponencial', 
            self.create_normal_distribution, 
            10 + button_width,
            10)
        
        self.ui.create_button(
            'Dist Normal', 
            self.create_normal_distribution, 
            10 + button_width*2,
            10)
    
    def create_uniform_distribution(self):
        print("create_uniform_distribution")
        # self.ui.plot_chart()
        
    def create_normal_distribution(self):
        # Constants 
        _a = 1234512354
        _c= 5623154656
        _m = 656878913
        x1= 49781519
        x2 = 478997853

        a = -1.23
        b = 24.5
        lamb = 0.01 
        u = 2 # Mean
        s = 0.707 # Standard deviation
        n = int(1e3) # Number of samples
        random_numbers = []

        for i in range(100):
            x1 = mixedCongruentGenerator(_a, _c, _m, x1)
            x2 = mixedCongruentGenerator(_a, _c, _m, x2)
            r = normalDist(u, s, x1/_m, x2/_m)
            random_numbers.append(r)
        
        chart_params = {
            'xlabel': 'Valores',
            'ylabel': 'Distribución',
            'data': random_numbers
        }
        
        self.ui.plot_histogram_chart(chart_params)

    def start(self):
        self.ui.run()
        