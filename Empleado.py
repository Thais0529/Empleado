class Empleado:
    '''
    crear objeto de la clase Empleado
    '''

    def __init__(self, nombre, sueldo):
        '''
        constructor de la clase Empleado
        :param nombre: nombre del empleado
        :param sueldo: sueldo del empleado
        :param eliminado: True si el empleado es eliminado, False si el empleado no es eliminado
        '''
        self.nombre = nombre
        self.sueldo = sueldo
        self.eliminado = False

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
        #falta crear otros atributos