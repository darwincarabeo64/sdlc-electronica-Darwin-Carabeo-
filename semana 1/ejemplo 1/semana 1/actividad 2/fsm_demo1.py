from enum import Enum, auto
# Definimos los posibles estados del semáforo
class TrafficLightState(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

# Clase que representa la Máquina de Estados Finitos (FSM)
class TrafficLightFSM:

    # Constructor: se ejecuta al crear un objeto
    def __init__(self):
        self.state = TrafficLightState.RED      # Estado inicial
        self.cycle_count = 0                    # Contador de transiciones

    # Método que cambia al siguiente estado va preguntando una condición tras otra 
    # hasta encontrar la correcta, a diferencia del diccionario que es mas directo y no necesita preguntar
    #el ejercicio de ejemplo busca el estado actual en una tabla de manera mas optimizada
    def transition(self):

        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN

        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW

        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

        # Cada vez que cambia de estado aumenta el contador
        self.cycle_count += 1

        # Regresa el nuevo estado
        return self.state