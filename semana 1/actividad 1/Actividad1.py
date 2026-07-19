from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol

class SensorType(Enum):
    TEMPERATURE = auto()
    HUMIDITY = auto()

@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float
    sensor_type: SensorType

class Transport(Protocol):
    def send(self, payload: bytes) -> None:
        ...

def to_frame(r: Reading) -> bytes:
    """Convierte una lectura a bytes para enviar"""
    return f"{r.sensor_id}:{r.value:.2f}".encode()

# ============ FUNCIÓN 1: Conversión de temperatura ============
def celsius_a_fahrenheit(lectura: Reading) -> Reading:
    """Si es temperatura, convierte Celsius → Fahrenheit"""
    if lectura.sensor_type == SensorType.TEMPERATURE:
        nuevo_valor = (lectura.value * 9.0 / 5.0) + 32.0
        return Reading(lectura.sensor_id, nuevo_valor, lectura.sensor_type)
    return lectura

# ============ FUNCIÓN 2: Detección de umbral peligroso ============
def es_peligroso(lectura: Reading, limite: float = 40.0) -> bool:
    """Devuelve True si la temperatura supera el límite"""
    if lectura.sensor_type == SensorType.TEMPERATURE:
        return lectura.value > limite
    return False

# ============ FUNCIÓN 3: Normalización de humedad ============
def normalizar_humedad(lectura: Reading) -> Reading:
    """Convierte humedad de 0-100% a 0-1 (decimal)"""
    if lectura.sensor_type == SensorType.HUMIDITY:
        nuevo_valor = lectura.value / 100.0
        return Reading(lectura.sensor_id, nuevo_valor, lectura.sensor_type)
    return lectura

# ============ FUNCIÓN 4: Clasificación por rango ============
def clasificar_temperatura(lectura: Reading) -> str:
    """Clasifica la temperatura como 'Frío', 'Templado' o 'Caliente'"""
    if lectura.sensor_type == SensorType.TEMPERATURE:
        if lectura.value < 10:
            return "Frío"
        elif lectura.value < 25:
            return "Templado"
        else:
            return "Caliente"
    return "No es temperatura"

# ============ FUNCIÓN 5: Conversión inversa ============
def fahrenheit_a_celsius(lectura: Reading) -> Reading:
    """Si es temperatura, convierte Fahrenheit → Celsius"""
    if lectura.sensor_type == SensorType.TEMPERATURE:
        nuevo_valor = (lectura.value - 32.0) * 5.0 / 9.0
        return Reading(lectura.sensor_id, nuevo_valor, lectura.sensor_type)
    return lectura