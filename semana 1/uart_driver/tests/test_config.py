import pytest

from config import UartConfig


# =====================================================
# Test 1
# Verifica que se cree correctamente una configuración
# =====================================================

def test_valid_config():

    config = UartConfig(9600, "N", 1, 1.0)

    assert config.baudrate == 9600
    assert config.parity == "N"
    assert config.stop_bits == 1
    assert config.timeout == 1.0


# =====================================================
# Test 2
# Verifica que un baudrate inválido produzca un error
# =====================================================

def test_invalid_baudrate():

    with pytest.raises(ValueError):

        UartConfig(0, "N", 1, 1.0)


# =====================================================
# Test 3
# Verifica que la configuración sea inmutable
# =====================================================

def test_config_is_frozen():

    config = UartConfig(9600, "N", 1, 1.0)

    with pytest.raises(Exception):

        config.baudrate = 115200