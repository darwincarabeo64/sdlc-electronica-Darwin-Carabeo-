from abc import ABC, abstractmethod


# =====================================================
# Clase base para todos los analizadores (parsers)
# OCP, LSP e ISP
# =====================================================

class MessageParser(ABC):

    @abstractmethod
    def can_parse(self, message):
        pass

    @abstractmethod
    def parse(self, message):
        pass


# =====================================================
# Parser para mensajes Modbus
# =====================================================

class ModbusParser(MessageParser):

    def can_parse(self, message):
        # Un ejemplo simple: los mensajes Modbus comienzan con "MODBUS"
        return message.startswith("MODBUS")

    def parse(self, message):

        if self.can_parse(message):
            return {
                "protocol": "Modbus",
                "data": message
            }

        return None


# =====================================================
# Parser para mensajes NMEA
# =====================================================

class NMEAParser(MessageParser):

    def can_parse(self, message):
        # Un ejemplo simple: los mensajes NMEA comienzan con "$GPGGA"
        return message.startswith("$GPGGA")

    def parse(self, message):

        if self.can_parse(message):
            return {
                "protocol": "NMEA",
                "data": message
            }

        return None