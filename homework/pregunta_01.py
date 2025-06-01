"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    # leer el archivo
    with open("files/input/clusters_report.txt", "r") as file:
        # extraer columnas y datos
        columns, rows = [file.readline(), file.readline()], file.readlines()

    # organizar las columnas
    columns = [line.strip() for line in columns]
    columns = [columns[0].split()[0], ' '.join(columns[0].split()[1:3] + columns[1].split()[:2]),
               ' '.join(columns[0].split()[3:5] + columns[1].split()[2:]), ' '.join(columns[0].split()[5:])]
    columns = [column.lower().replace(' ', '_') for column in columns]

    # organizar las filas
    helper = rows[2:].copy()
    rows = []
    row = []
    while helper:
        data = helper.pop(0)

        if not data.isspace(): # registro
            data = data.strip().replace('.', '') # eliminar puntos
            data = ' '.join(data.split()) # eliminar espacios dobles

            if data.split()[0].isnumeric(): # primera parte del registro
                data = data.split()
                clus = int(data[0])
                cant = int(data[1])
                perc = float(data[2].replace(',', '.'))
                text = ' '.join(data[4:])
                row.extend([clus, cant, perc, text])
            else:
                row[-1] += f" {data}"

        else: # salto a otro registro
            rows.append(row)
            row = []

    return pd.DataFrame(rows, columns=columns)
