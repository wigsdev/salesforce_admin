import csv
import os

# Configuración de rutas
input_file = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"
output_dir = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\2025"

# Mapeo de Carreras
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

    carreras = set()
    contactos = {}
    materias = {}
    inscripciones = {}
    evaluaciones = {}

    print(f"Leyendo archivo: {input_file}")

    with open(input_file, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dni = row["DNI"]
            codigo_materia = row["Codigo_Materia"]
            prefix = codigo_materia.split("-")[0]
            nombre_carrera = carreras_map.get(prefix, "Otros")
            anio = "2025"

            # Calcular Año Lectivo dinámicamente (Anio-Semestre)
            fecha_lista = row["Fecha_Examen"]
            try:
                mes = int(fecha_lista.split("-")[1])
                semestre = "1" if mes <= 6 else "2"
                anio_lectivo = f"{anio}-{semestre}"
            except:
                anio_lectivo = anio

            carreras.add((nombre_carrera, prefix))

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

            if codigo_materia not in materias:
                materias[codigo_materia] = {
                    "Codigo_Materia__c": codigo_materia,
                    "Nombre_Materia": row["Nombre_Materia"],
                    "Abreviatura__c": prefix,
                }

            id_importacion = f"{dni}_{codigo_materia}_{anio_lectivo}"
            if id_importacion not in inscripciones:
                inscripciones[id_importacion] = {
                    "Numero_Documento__c": dni,
                    "Codigo_Materia": codigo_materia,
                    "ID_Importacion": id_importacion,
                    "Anio_Lectivo": anio_lectivo,
                }

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
                try:
                    if int(new_eval["Nota"]) > int(evaluaciones[id_evaluacion]["Nota"]):
                        evaluaciones[id_evaluacion] = new_eval
                except:
                    pass

    def write_csv(filename, data, fieldnames):
        path = os.path.join(output_dir, filename)
        with open(path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
            writer.writeheader()
            writer.writerows(data)
        print(f"Generado: {filename} ({len(data)} registros)")

    write_csv(
        "00_Carga_Carreras_2025.csv",
        [
            {"Nombre_Carrera": c[0], "Abreviatura__c": c[1]}
            for c in sorted(list(carreras))
        ],
        ["Nombre_Carrera", "Abreviatura__c"],
    )

    write_csv(
        "01_Carga_Contactos_2025.csv",
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

    write_csv(
        "02_Carga_Materias_2025.csv",
        list(materias.values()),
        ["Codigo_Materia__c", "Nombre_Materia", "Abreviatura__c"],
    )

    write_csv(
        "03_Carga_Inscripciones_2025.csv",
        list(inscripciones.values()),
        ["Numero_Documento__c", "Codigo_Materia", "ID_Importacion", "Anio_Lectivo"],
    )

    write_csv(
        "04_Carga_Evaluaciones_2025.csv",
        list(evaluaciones.values()),
        ["ID_Evaluacion", "ID_Inscripcion", "Fecha_Lista", "Nota", "Estado"],
    )


if __name__ == "__main__":
    transform()
