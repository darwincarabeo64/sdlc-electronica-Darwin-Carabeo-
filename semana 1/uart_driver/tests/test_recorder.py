import json

from recorder import DataRecorder



# =====================================================
# TEST 1
# Verifica que escribe un registro JSON
# =====================================================

def test_recorder_write_json(tmp_path):

    # Archivo temporal para la prueba
    file = tmp_path / "data.jsonl"


    recorder = DataRecorder(file)


    data = {
        "protocol": "Modbus",
        "value": 25
    }


    recorder.save(data)


    # Leer el archivo creado
    with open(file, "r") as f:

        line = f.readline()


    result = json.loads(line)


    assert result["protocol"] == "Modbus"
    assert result["value"] == 25




# =====================================================
# TEST 2
# Verifica que puede guardar varios registros
# =====================================================

def test_recorder_multiple_lines(tmp_path):

    file = tmp_path / "data.jsonl"


    recorder = DataRecorder(file)


    recorder.save({
        "sensor": "TEMP01",
        "value": 20
    })


    recorder.save({
        "sensor": "TEMP01",
        "value": 21
    })


    with open(file, "r") as f:

        lines = f.readlines()


    assert len(lines) == 2




# =====================================================
# TEST 3
# Verifica que guarda datos vacíos correctamente
# =====================================================

def test_recorder_empty_data(tmp_path):

    file = tmp_path / "data.jsonl"


    recorder = DataRecorder(file)


    recorder.save({})


    with open(file, "r") as f:

        line = f.readline()


    result = json.loads(line)


    assert result == {}