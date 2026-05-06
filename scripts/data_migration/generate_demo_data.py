import csv
import os

# Configuración de rutas
input_2024 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"
input_2025 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"
output_dir = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DEMO"

carreras_map = {
    "DAT": "Ciencia de Datos",
    "DEV": "Desarrollo de Software",
    "GEN": "Formación General",
    "IA": "Inteligencia Artificial",
    "MKT": "Marketing Digital",
    "NEG": "Negocios Digitales",
    "UX": "Diseño de Experiencia de Usuario",
}


def generate_demo():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Identificar cohortes (100 alumnos de cada año)
    def get_sample_dnis(path, count):
        dnis = set()
        with open(path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                dnis.add(row["DNI"])
                if len(dnis) >= count:
                    break
        return dnis

    sample_2024 = get_sample_dnis(input_2024, 100)
    sample_2025 = get_sample_dnis(input_2025, 100)

    # Estructuras para CSVs
    carreras = set()
    contactos = {}
    materias = {}
    inscripciones = {}
    evaluaciones = {}

    def process_data(path, sample_set, year):
        with open(path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                dni = row["DNI"]
                if dni not in sample_set:
                    continue

                cod_materia = row["Codigo_Materia"]
                prefix = cod_materia.split("-")[0]
                nombre_carrera = carreras_map.get(prefix, "Otros")
                fecha = row["Fecha_Examen"]

                # Registro Carrera/Materia
                carreras.add((nombre_carrera, prefix))
                if cod_materia not in materias:
                    materias[cod_materia] = {
                        "Codigo_Materia__c": cod_materia,
                        "Nombre_Materia": row["Nombre_Materia"],
                        "Abreviatura__c": prefix,
                    }

                # Registro Contacto
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

                # Lógica de Semestre/Inscripción
                try:
                    mes = int(fecha.split("-")[1])
                    sem = "1" if mes <= 6 else "2"
                    anio_lec = f"{year}-{sem}"
                except Exception:
                    anio_lec = year

                id_ins = f"{dni}_{cod_materia}_{anio_lec}"
                if id_ins not in inscripciones:
                    inscripciones[id_ins] = {
                        "Numero_Documento__c": dni,
                        "Codigo_Materia": cod_materia,
                        "ID_Importacion": id_ins,
                        "Anio_Lectivo": anio_lec,
                    }

                # Registro Evaluación (Upsert Strategy - Mejor Nota)
                id_eval = f"{id_ins}_{fecha}"
                new_eval = {
                    "ID_Evaluacion": id_eval,
                    "ID_Inscripcion": id_ins,
                    "Fecha_Lista": fecha,
                    "Nota": row["Nota"],
                    "Estado": row["Estado"],
                }
                if id_eval not in evaluaciones or int(row["Nota"]) > int(
                    evaluaciones[id_eval]["Nota"]
                ):
                    evaluaciones[id_eval] = new_eval

    # Procesar ambos años
    process_data(input_2024, sample_2024, "2024")
    process_data(input_2025, sample_2025, "2025")

    # Escritura de Archivos
    def save_csv(name, data, fields):
        with open(
            os.path.join(output_dir, name), mode="w", encoding="utf-8-sig", newline=""
        ) as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        print(f"Creado: {name} ({len(data)} registros)")

    save_csv(
        "00_Carga_Carreras_DEMO.csv",
        [
            {"Nombre_Carrera": c[0], "Abreviatura__c": c[1]}
            for c in sorted(list(carreras))
        ],
        ["Nombre_Carrera", "Abreviatura__c"],
    )
    save_csv(
        "01_Carga_Contactos_DEMO.csv",
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
    save_csv(
        "02_Carga_Materias_DEMO.csv",
        list(materias.values()),
        ["Codigo_Materia__c", "Nombre_Materia", "Abreviatura__c"],
    )
    save_csv(
        "03_Carga_Inscripciones_DEMO.csv",
        list(inscripciones.values()),
        ["Numero_Documento__c", "Codigo_Materia", "ID_Importacion", "Anio_Lectivo"],
    )
    save_csv(
        "04_Carga_Evaluaciones_DEMO.csv",
        list(evaluaciones.values()),
        ["ID_Evaluacion", "ID_Inscripcion", "Fecha_Lista", "Nota", "Estado"],
    )


if __name__ == "__main__":
    generate_demo()
