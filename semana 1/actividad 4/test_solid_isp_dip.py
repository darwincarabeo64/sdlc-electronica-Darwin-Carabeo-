from solid_isp_dip import (
    TemperatureSensor,
    PressureSensor,
    InMemoryRepository,
    DataProcessor,
)


# =====================================================
# ISP (2 pruebas)
# =====================================================

# Test 1: Verificar que TemperatureSensor puede leer
def test_temperature_sensor():
    sensor = TemperatureSensor()

    assert sensor.read() == 25.5


# Test 2: Verificar que PressureSensor puede calibrarse
def test_pressure_sensor():
    sensor = PressureSensor()

    assert sensor.calibrate() == "Sensor calibrado"


# =====================================================
# DIP (2 pruebas)
# =====================================================

# Test 3: Verificar que DataProcessor guarda un dato
def test_data_processor_save():
    repository = InMemoryRepository()
    processor = DataProcessor(repository)

    processor.process("S1", 30)

    assert repository.get_latest("S1") == 30


# Test 4: Verificar que DataProcessor obtiene el último dato
def test_data_processor_latest():
    repository = InMemoryRepository()
    processor = DataProcessor(repository)

    processor.process("TEMP01", 26.5)

    assert processor.latest("TEMP01") == 26.5