class ClaseB:
    num_llamadas_B = 0
    def llamar(self):
        print("Llamando método en Clase B")
        self.num_llamadas_B += 1

class SubClaseDerecha(ClaseB):
    num_llamadas_der = 0
    def llamar(self):
        ClaseB.llamar(self)
        print("Llamando método en Subclase Derecha")
        self.num_llamadas_der += 1

class SubClaseIzquierda(ClaseB):
    num_llamadas_izq = 0
    def llamar(self):
        ClaseB.llamar(self)
        print("Llamando método en Subclase Izquierda")
        self.num_llamadas_izq += 1


class SubClaseA(SubClaseDerecha, SubClaseIzquierda):
    num_llamadas_subA = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en SubclaseA")
        self.num_llamadas_subA += 1

s = SubClaseA()
s.llamar()
print(s.num_llamadas_subA, s.num_llamadas_izq, s.num_llamadas_der, s.num_llamadas_B)
print(SubClaseA.__mro__)