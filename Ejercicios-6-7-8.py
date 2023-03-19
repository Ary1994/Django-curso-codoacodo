class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres")
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Error: La edad debe ser un número entero positivo")
    
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres")
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad
    
    def set_titular(self, titular):
        if isinstance(titular, Persona):
            self.titular = titular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona")
    
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:", self.titular.mostrar())
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

            
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        edad = self.titular.get_edad()
        return edad >= 18 and edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: El titular no es válido para retirar dinero")
    
    def mostrar(self):
        print("Cuenta Joven")
        print("Bonificación:", self.__bonificacion)