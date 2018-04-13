class Individuo:
    def __init__(self, nombre, ident):
        self.nombre = nombre
        self.ident = ident
        self.amigos = list()

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)
        print("Ahora {} y {} son amigos".format(self.nombre, amigo.nombre))

    def __repr__(self):
        return "Mi nombre es {} y mi identificador es {}".format(self.nombre, self.ident)

##Obtención de datos##
datos_individuos = open("individuos.txt", "r")
personas = {str(individuo).strip().split("\t")[1] : str(individuo).strip().split("\t")[0] for individuo in datos_individuos}
datos_individuos.close()

datos_amistades = open("amistades.txt", "r")
amistades = [str(relacion).strip().split("\t") for relacion in datos_amistades]
datos_amistades.close()

individuos = [Individuo(personas[key],key) for key in personas.keys()]
for i in individuos:
    print(i)
