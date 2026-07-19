from dataclasses import dataclass


# =====================================================
# Configuración del UART
# SRP: solo almacena y valida la configuración
# =====================================================

@dataclass(frozen=True)
class UartConfig:

    baudrate: int
    parity: str
    stop_bits: int
    timeout: float

    # Se ejecuta automáticamente después del constructor
    def __post_init__(self):

        # Verifica que el baudrate sea mayor que cero
        if self.baudrate <= 0:
            raise ValueError("El baudrate debe ser mayor que 0")