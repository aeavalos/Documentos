# Definicion individuo para usarlo como un nodo.
class Individuo:
    def __init__(self, nombre, ident):
        self.nombre = nombre
        self.ident = ident
        self.amigos = list()

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def cantidad_amigos(self):
        return "{} tiene {} amigos.".format(self.nombre, len(self.amigos))

    def __repr__(self):
        return "Nombre: {} \nIdentificador: {}\n".format(self.nombre, self.ident)

    def __eq__(self, other):
        return self.ident == other.ident

    def __lt__(self, other):
        return self.ident < other.ident


# Obtención de datos.
datos_individuos = open("individuos.txt", "r")
personas = {int(str(individuo).strip().split("\t")[1]): str(individuo).strip().split("\t")[0] for individuo in datos_individuos}
datos_individuos.close()

datos_amistades = open("amistades.txt", "r")
amistades = list()
for relacion in datos_amistades:
    previo = str(relacion).strip().split("\t")
    amistades.append([int(previo[0]), int(previo[1])])
datos_amistades.close()

individuos = [Individuo(personas[key], key) for key in personas.keys()]
individuos.sort()

for r in amistades:
    individuos[r[0] - 1].agregar_amigo(individuos[r[1] - 1])
    individuos[r[1] - 1].agregar_amigo(individuos[r[0] - 1])

ind_definitivos = dict()
keys_elegidos = list()
for i in individuos:
    if i.nombre in ["Alex", "Carla", "Juan", "Marta", "Pedro"]:
        keys_elegidos.append(i.ident)
    ind_definitivos[i.ident] = i

# Imprimir en pantalla numero de amigos de personas elegidas.
for key in keys_elegidos:
        print(ind_definitivos[key].cantidad_amigos())

# Crear archivo grado.txt con grados de relacion para cada par de individuos de elegidos format = (n1   n2  grado).
grados = open("grados.txt", "w")
# Reviso en los keys_elegidos y empiezo a navegar entre los amigos de los amigos hasta encontrar a todos los buscados.
# Parte viendo los amigos de la persona final, y luego empiezo a buscar desde la persona inicial a ver si encuentro a
# los amigos del final.
grados.close()

# Crear archivo con parejas en peligro.
parejas_peligro = open("ParejasQuePeligran.txt", "w")
# Revisar si entre los nodos existe un ciclo, si existe un nodo, no peligra.
# Existen dos rutas que no comparten arcos. Porque de esta manera se formaria un ciclo que una a ambos nodos.
parejas_peligro.close()

# Encontrar grupos y ver si estan en peligro.
# Grupo: Si hacemos el subgrafo inducido con los vertices solicitados obtengo un grafo conexo?
# Empezar en un nodo inicial y ver si entre sus amigos está alguno del grupo, luego seguir sin repetir nodos.
# Grupo peligra: Si una pareja dentro del grupo peligra.
# Funcion de peligro para revisar desde un nodo a cada par de arcos.

# Si el grafo es un grupo.
# Encontrar AMEM, si existe, el grafo es un grupo.



# Preguntas al profe:
# Dos amigos de grado uno peligran.
# ¿Como se compone un grupo? ¿Es cerrado son personas conectadas entre amigos?
