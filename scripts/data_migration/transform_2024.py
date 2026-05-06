import csv
import os

# Configuración de rutas
input_file = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"
output_dir = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\2024"

# Mapeo de Carreras (Fuerza bruta basada en el catálogo existente)
carreras_map = {
    "DAT": "Ciencia de Datos",
    "DEV": "Desarrollo de Software",
    "GEN": "Formación General",
    "IA": "Inteligencia Artificial",
    "MKT": "Marketing Digital",
    "NEG": "Negocios Digitales",
    "UX": "Diseño de Experiencia de Usuario",
}


def transform():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Contenedores para datos únicos
    carreras = set()
    contactos = {}  # DNI -> {datos}
    materias = {}  # Codigo -> {datos}
    inscripciones = {}  # ID_Importacion -> {datos}
    evaluaciones = {}  # ID_Evaluacion -> {datos}

    print(f"Leyendo archivo: {input_file}")

    with open(input_file, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dni = row["DNI"]
            codigo_materia = row["Codigo_Materia"]
            prefix = codigo_materia.split("-")[0]
            nombre_carrera = carreras_map.get(prefix, "Otros")
            anio = "2024"

            # Calcular Año Lectivo dinámicamente (Anio-Semestre)
            fecha_lista = row["Fecha_Examen"]
            try:
                mes = int(fecha_lista.split("-")[1])
                semestre = "1" if mes <= 6 else "2"
                anio_lectivo = f"{anio}-{semestre}"
            except Exception:
                anio_lectivo = anio

            # 1. Carreras
            carreras.add((nombre_carrera, prefix))

            # 2. Contactos (Alumno)
            if dni not in contactos:
                contactos[dni] = {
                    "Nombre": row["Nombre"],
                    "Apellido": row["Apellido"],
                    "Numero_Documento__c": dni,
                    "Email": row["Email"],
                    "Telefono": row["Telefono"],
                    "Rol__c": "Alumno",
                    "Tipo_Documento__c": "DNI",
                }

            # 3. Materias
            if codigo_materia not in materias:
                materias[codigo_materia] = {
                    "Codigo_Materia__c": codigo_materia,
                    "Nombre_Materia": row["Nombre_Materia"],
                    "Abreviatura__c": prefix,
                }

            # 4. Inscripciones (Única por Alumno-Materia-Anio)
            id_importacion = f"{dni}_{codigo_materia}_{anio_lectivo}"
            if id_importacion not in inscripciones:
                inscripciones[id_importacion] = {
                    "Numero_Documento__c": dni,
                    "Codigo_Materia": codigo_materia,
                    "ID_Importacion": id_importacion,
                    "Anio_Lectivo": anio_lectivo,
                }

            # 5. Evaluaciones (Captura todos los intentos, deduplica por ID_Evaluacion)
            id_evaluacion = f"{id_importacion}_{fecha_lista}"
            new_eval = {
                "ID_Evaluacion": id_evaluacion,
                "ID_Inscripcion": id_importacion,
                "Fecha_Lista": fecha_lista,
                "Nota": row["Nota"],
                "Estado": row["Estado"],
            }

            if id_evaluacion not in evaluaciones:
                evaluaciones[id_evaluacion] = new_eval
            else:
                # Si hay colisión en el mismo día, nos quedamos con la nota más alta
                try:
                    if int(new_eval["Nota"]) > int(evaluaciones[id_evaluacion]["Nota"]):
                        evaluaciones[id_evaluacion] = new_eval
                except Exception:
                    pass

    # Escritura de archivos
    def write_csv(filename, data, fieldnames):
        path = os.path.join(output_dir, filename)
        with open(path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()
            writer.writerows(data)
        print(f"Generado: {filename} ({len(data)} registros)")

    # 00_Carga_Carreras_2024.csv
    write_csv(
        "00_Carga_Carreras_2024.csv",
        [
            {"Nombre_Carrera": c[0], "Abreviatura__c": c[1]}
            for c in sorted(list(carreras))
        ],
        ["Nombre_Carrera", "Abreviatura__c"],
    )

    # 01_Carga_Contactos_2024.csv
    write_csv(
        "01_Carga_Contactos_2024.csv",
        list(contactos.values()),
        [
            "Nombre",
            "Apellido",
            "Numero_Documento__c",
            "Email",
            "Telefono",
            "Rol__c",
            "Tipo_Documento__c",
        ],
    )

    # 02_Carga_Materias_2024.csv
    write_csv(
        "02_Carga_Materias_2024.csv",
        list(materias.values()),
        ["Codigo_Materia__c", "Nombre_Materia", "Abreviatura__c"],
    )

    # 03_Carga_Inscripciones_2024.csv
    write_csv(
        "03_Carga_Inscripciones_2024.csv",
        list(inscripciones.values()),
        ["Numero_Documento__c", "Codigo_Materia", "ID_Importacion", "Anio_Lectivo"],
    )

    # 04_Carga_Evaluaciones_2024.csv
    write_csv(
        "04_Carga_Evaluaciones_2024.csv",
        list(evaluaciones.values()),
        ["ID_Evaluacion", "ID_Inscripcion", "Fecha_Lista", "Nota", "Estado"],
    )


if __name__ == "__main__":
    transform()
