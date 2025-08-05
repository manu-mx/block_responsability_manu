from abc import ABC, abstractmethod

# Manejador Abstracto
class ManejadorSoporte(ABC):
    def __init__(self):
        self._siguiente = None

    def establecer_siguiente(self, manejador):
        self._siguiente = manejador
        return manejador  # Permite encadenamiento fluido: .establecer_siguiente(...)

    @abstractmethod
    def manejar_ticket(self, nivel_complejidad, mensaje):
        pass

# Manejadores Concretos
class SoporteBasico(ManejadorSoporte):
    def manejar_ticket(self, nivel_complejidad, mensaje):
        if nivel_complejidad <= 1:  # Problema sencillo
            print(f"[Soporte Básico] Resuelto: '{mensaje}'")
        elif self._siguiente:
            self._siguiente.manejar_ticket(nivel_complejidad, mensaje)

class SoporteAvanzado(ManejadorSoporte):
    def manejar_ticket(self, nivel_complejidad, mensaje):
        if nivel_complejidad <= 3:  # Problema moderado
            print(f"[Soporte Avanzado] Resuelto: '{mensaje}'")
        elif self._siguiente:
            self._siguiente.manejar_ticket(nivel_complejidad, mensaje)

class SoporteEspecialista(ManejadorSoporte):
    def manejar_ticket(self, nivel_complejidad, mensaje):
        if nivel_complejidad <= 5:  # Problema complejo
            print(f"[Especialista] Resuelto: '{mensaje}'")
        else:
            print(f"[Especialista] Ticket demasiado complejo: '{mensaje}' (Derivado a desarrollo)")

# Cliente
if __name__ == "__main__":
    # Configurar cadena de responsabilidad
    basico = SoporteBasico()
    avanzado = SoporteAvanzado()
    especialista = SoporteEspecialista()

    basico.establecer_siguiente(avanzado).establecer_siguiente(especialista)

    # Tickets de ejemplo
    tickets = [
        {"nivel": 1, "mensaje": "No puedo iniciar sesión."},
        {"nivel": 3, "mensaje": "Error al conectar a la base de datos."},
        {"nivel": 5, "mensaje": "Fallo crítico en el servidor."},
        {"nivel": 6, "mensaje": "Bug en el núcleo del sistema."}
    ]

    for ticket in tickets:
        print(f"\nNuevo ticket (Nivel {ticket['nivel']}): {ticket['mensaje']}")
        basico.manejar_ticket(ticket["nivel"], ticket["mensaje"])
