from parsers import (
    ModbusParser,
    NMEAParser,
)


# =====================================================
# MODBUS
# =====================================================

# Test 1: Frame Modbus válido
def test_modbus_valid_frame():

    parser = ModbusParser()

    message = "MODBUS 01 03"

    # Verifica que reconoce el protocolo
    assert parser.can_parse(message) is True

    result = parser.parse(message)

    # Verifica que parse() devolvió información
    assert result is not None

    # Ahora es seguro acceder al diccionario
    assert result["protocol"] == "Modbus"
    assert result["data"] == message



# Test 2: Frame Modbus inválido
def test_modbus_invalid_frame():

    parser = ModbusParser()

    message = "$GPGGA,12345"

    # No debe reconocer un mensaje NMEA
    assert parser.can_parse(message) is False

    # Debe devolver None porque no puede interpretarlo
    assert parser.parse(message) is None



# =====================================================
# NMEA
# =====================================================

# Test 3: Frame NMEA válido
def test_nmea_valid_frame():

    parser = NMEAParser()

    message = "$GPGGA,12345"

    # Verifica que reconoce el protocolo
    assert parser.can_parse(message) is True

    result = parser.parse(message)

    # Evita el error de Pylance
    assert result is not None

    # Verifica que es un mensaje NMEA
    assert result["protocol"] == "NMEA"
    assert result["data"] == message



# Test 4: Frame NMEA inválido
def test_nmea_invalid_frame():

    parser = NMEAParser()

    message = "MODBUS 01 03"

    # No debe reconocer mensajes Modbus
    assert parser.can_parse(message) is False

    # Debe devolver None
    assert parser.parse(message) is None