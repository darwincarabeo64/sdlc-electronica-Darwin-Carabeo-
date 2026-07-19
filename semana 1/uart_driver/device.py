from config import UartConfig
from parsers import MessageParser


# =====================================================
# Dispositivo UART
# DIP: depende de una abstracción (MessageParser)
# =====================================================

class UartDevice:

    def __init__(self, config: UartConfig, parser: MessageParser):

        # Guarda la configuración
        self.config = config

        # Guarda el parser recibido
        self.parser = parser

        # El dispositivo inicia desconectado
        self.connected = False


    # Conectar el dispositivo
    def connect(self):

        self.connected = True


    # Desconectar el dispositivo
    def disconnect(self):

        self.connected = False


    # Leer un mensaje y analizarlo
    def read_and_parse(self, message):

        # Si no está conectado, no puede leer
        if not self.connected:
            raise ConnectionError("El dispositivo no está conectado")

        # Si el parser reconoce el mensaje
        if self.parser.can_parse(message):
            return self.parser.parse(message)

        # Si no reconoce el mensaje
        return None