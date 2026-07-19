from abc import ABC, abstractmethod

# SRP - Single Responsibility Principle
# Una clase = una responsabilidad

class SensorReader:
    """Solo se encarga de leer un sensor."""

    def read(self):
        return 25.5

class DataLogger:
    """Solo se encarga de guardar datos."""

    def save(self, value):
        print(f"Dato guardado: {value}")

# OCP - Open/Closed Principle
# Extender sin modificar

class AlertStrategy(ABC):

    @abstractmethod
    def send(self, message):
        pass

class ConsoleAlert(AlertStrategy):

    def send(self, message):
        print(f"Consola: {message}")

class FileAlert(AlertStrategy):

    def send(self, message):
        print(f"Archivo: {message}")


# En el futuro simplemente agregamos otra clase.
# No modificamos las anteriores.

class EmailAlert(AlertStrategy):

    def send(self, message):
        print(f"Email: {message}")

class AnomalyDetector:

    def __init__(self, alert, threshold):
        self.alert = alert
        self.threshold = threshold

    def check(self, value):

        if value > self.threshold:
            self.alert.send("Anomalía detectada")

# LSP - Liskov Substitution Principle
# Cualquier hijo puede sustituir al padre

class BaseSensor:

    def read(self):
        pass

class TemperatureSensor(BaseSensor):

    def read(self):
        return "Temperatura: 26°C"

class HumiditySensor(BaseSensor):

    def read(self):
        return "Humedad: 60%"

def process_sensor(sensor):
    return sensor.read()


