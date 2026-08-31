class Usuario:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def agregarSaldo(self, monto):
        self.saldo = self.saldo + monto
        print("Saldo agregado correctamente.")

    def rentar(self, scooter):
        if self.saldo >= 20:
            if scooter.estaDisponible == True:
                if scooter.desbloquear() == True:
                    self.saldo = self.saldo - 20
                    print("Scooter rentado correctamente.")
                    print("Se descontaron $20 de tu saldo.")
                else:
                    print("No se pudo desbloquear el scooter.")
            else:
                print("El scooter no está disponible.")
        else:
            print("No tienes suficiente saldo.")

        
class Scooter:
    def __init__(self, id, nivelBateria):
        self.id = id
        self.nivelBateria = nivelBateria
        self.estaDisponible = True

    def desbloquear(self):
        if self.nivelBateria > 0 and self.estaDisponible == True:
            self.estaDisponible = False
            print("Scooter desbloqueado.")
            return True
        else:
            return False

    def finalizarViaje(self):
        if self.estaDisponible == False:
            self.estaDisponible = True
            print("Viaje finalizado.")
            print("El scooter está disponible.")
        else:
            print("No hay ningún viaje activo.")

    def recargar(self):
        self.nivelBateria = 100
        print("Scooter recargado al 100%.")


# Crear objetos

nombre = input("Escribe tu nombre: ")

usuario1 = Usuario(nombre, 0)

scooter1 = Scooter("S001", 80)


# Menú

while True:

    print("\n===== SISTEMA DE SCOOTERS =====")
    print("1. Ver información")
    print("2. Agregar saldo")
    print("3. Rentar scooter")
    print("4. Finalizar viaje")
    print("5. Recargar scooter")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        print("\n--- INFORMACIÓN ---")
        print("Usuario:", usuario1.nombre)
        print("Saldo: $", usuario1.saldo)

        print("\nScooter:", scooter1.id)
        print("Batería:", scooter1.nivelBateria, "%")
        print("Disponible:", scooter1.estaDisponible)

    elif opcion == "2":

        monto = float(input("¿Cuánto dinero quieres agregar?: "))

        usuario1.agregarSaldo(monto)

        print("Saldo actual: $", usuario1.saldo)

    elif opcion == "3":

        usuario1.rentar(scooter1)

    elif opcion == "4":

        scooter1.finalizarViaje()

    elif opcion == "5":

        scooter1.recargar()

    elif opcion == "6":

        print("Programa terminado.")
        break

    else:

        print("Opción no válida.")