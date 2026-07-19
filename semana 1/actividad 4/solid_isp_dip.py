from abc import ABC, abstractmethod
from typing import Protocol

# ISP - Interface Segregation Principle
# Interfaces pequeñas y específicas

class Readable(ABC):

    @abstractmethod
    def read(self):
        pass

class Writable(ABC):

    @abstractmethod
    def write(self, data):
        pass

class Calibratable(ABC):

    @abstractmethod
    def calibrate(self):
        pass

# Sensor que solo lee
class TemperatureSensor(Readable):

    def read(self):
        return 25.5

# Dispositivo que solo escribe
class MemoryDevice(Writable):

    def write(self, data):
        print(f"Dato guardado: {data}")

# Sensor que necesita calibrarse
class PressureSensor(Calibratable):

    def calibrate(self):
        return "Sensor calibrado"

# DIP - Dependency Inversion Principle
# Depender de una abstracción

class DataRepository(Protocol):

    def save(self, sensor_id, value):
        ...

    def get_latest(self, sensor_id):
        ...

# Repositorio en memoria (simula una base de datos)
class InMemoryRepository:

    def __init__(self):
        self.data = {}

    def save(self, sensor_id, value):
        self.data[sensor_id] = value

    def get_latest(self, sensor_id):
        return self.data.get(sensor_id)

class DataProcessor:

    def __init__(self, repository):
        self.repository = repository

    def process(self, sensor_id, value):
        self.repository.save(sensor_id, value)

    def latest(self, sensor_id):
        return self.repository.get_latest(sensor_id)