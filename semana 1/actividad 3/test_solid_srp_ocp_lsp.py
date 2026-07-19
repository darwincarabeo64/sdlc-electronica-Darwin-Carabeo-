from solid_srp_ocp_lsp import (
    SensorReader,
    DataLogger,
    ConsoleAlert,
    FileAlert,
    AnomalyDetector,
    TemperatureSensor,
    HumiditySensor,
    process_sensor,
)


# =====================================================
# SRP (2 pruebas)
# =====================================================

def test_sensor_reader():
    reader = SensorReader()

    assert reader.read() == 25.5


def test_data_logger():
    logger = DataLogger()

    resultado = logger.save(25.5)

    assert resultado is None


# =====================================================
# OCP (2 pruebas)
# =====================================================

def test_console_alert():
    detector = AnomalyDetector(ConsoleAlert(), 30)

    resultado = detector.check(35)

    assert resultado is None


def test_file_alert():
    detector = AnomalyDetector(FileAlert(), 30)

    resultado = detector.check(35)

    assert resultado is None


# =====================================================
# LSP (2 pruebas)
# =====================================================

def test_temperature_sensor():
    sensor = TemperatureSensor()

    assert process_sensor(sensor) == "Temperatura: 26°C"


def test_humidity_sensor():
    sensor = HumiditySensor()

    assert process_sensor(sensor) == "Humedad: 60%"