# Tarea 1
class Persona:
    def __init__(self, nombre, apellido, correo):
        self.nombre =  nombre
        self.apellido = apellido
        self.correo  = correo

    def saludar(self):
        return 'hola soy {}'.format(self.nombre)

class Alumno:
    def __init__(self, nombre, fec_nac, dni, nacionalidad, cursos):
        super().__init__(nombre, fec_nac, dni, nacionalidad, cursos)
        self.__cursos = cursos


class Docente:
    def __init__(self, nombre, fec_nac, dni, nacionalidad,seg_social, cts, cursos):
        super().__init__(nombre, fec_nac, dni, nacionalidad, cursos)
        self.cts = cts
        self.__seg_social = seg_social


#Amanda = Alumno(nombre='Amanda', fec_nac='2222-21-12', dni= '23255673', nacionalidad='Ecuatoriana', cursos=['mate', 'letra'])










































































