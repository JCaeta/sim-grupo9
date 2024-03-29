from ui import PyQtApp
from generators import normalDist
from generators import mixedCongruentGenerator

class Controller:
    def __init__(self):
        self.ui = PyQtApp() # Es la clase que hace toda la parte gráfica
        self.build_interface()
    
    def on_change_a(self, value):
        print('a: ', value)
        
    def on_change_b(self, value):
        print('b: ', value)
        
    def on_change_sample_size(self, value):
        print('b: ', value)
        
    def on_change_intervals(self, value):
        print('b: ', value)
    
    def create_uniform_distribution(self):
        print("create_uniform_distribution")
    
    def build_interface(self):
        self.ui.create_button(
            'Dist Uniforme', 
            self.create_uniform_distribution)
        
        self.ui.create_button(
            'Dist Exponencial', 
            self.create_exponential_distribution)
        
        self.ui.create_button(
            'Dist Normal', 
            self.create_normal_distribution)
        
        self.a_input = self.ui.create_input('a', self.on_change_a)
        self.b_input = self.ui.create_input('b', self.on_change_b)
        self.sample_size_input = self.ui.create_input('Tamaño de muestra', self.on_change_sample_size, width = 120)
        self.interval_input = self.ui.create_input('Intervalos', self.on_change_intervals, width = 120)
        
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

    def create_exponential_distribution(self):
        print("create_exponential_distribution()")
        # Retrieve and print the input values
        print("a input:", self.a_input.text())
        print("b input:", self.b_input.text())
        print("Sample size input:", self.sample_size_input.text())
        print("Interval input:", self.interval_input.text())

    def start(self):
        self.ui.run()
        