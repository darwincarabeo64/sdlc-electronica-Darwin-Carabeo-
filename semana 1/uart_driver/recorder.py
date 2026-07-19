import json


# =====================================================
# Guarda datos en formato JSON Lines
# SRP: solo se encarga de guardar información
# =====================================================

class DataRecorder:

    def __init__(self, filename):

        # Nombre del archivo donde se guardarán los datos
        self.filename = filename


    # Guarda un registro en el archivo
    def save(self, data):

        with open(self.filename, "a") as file:

            # Convierte el diccionario a formato JSON
            json.dump(data, file)

            # Agrega un salto de línea (JSON Lines)
            file.write("\n")