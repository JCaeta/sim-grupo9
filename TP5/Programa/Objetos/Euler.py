class Euler:
    def __init__(self, h):
        self.h = h
        self.a = 2000
        self.t = 0

    def calcular_tiempo(self, cant_archivos):
        integraciones = []

        while self.a < cant_archivos:
            t = round(self.t, 4)
            a = round(self.a, 4)

            da_dt = round(-68 - (a**2 / a), 4)

            t_siguiente = round((t + self.h), 4)
            a_euler = round((a + self.h * da_dt), 4)

            datos = {
                "t": t,
                "a": a,
                "da_dt": da_dt,
                "t_siguiente": t_siguiente,
                "a_euler": a_euler
            }

            integraciones.append(datos)

            t = t_siguiente
            a = a_euler


        return integraciones


euler = Euler(h=0.1)

datos = euler.calcular_tiempo(cant_archivos=2000)

for i in datos:
    print(i, "\n")
