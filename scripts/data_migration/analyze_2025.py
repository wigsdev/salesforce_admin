import csv

file_path = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"


def analyze():
    dnis = set()
    careers = set()
    subjects = set()
    enrollments = set()
    evaluations = set()
    total_rows = 0

    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_rows += 1
                dni = row["DNI"]
                cod_materia = row["Codigo_Materia"]
                fecha = row["Fecha_Examen"]

                # Career prefix
                career_code = cod_materia.split("-")[0]

                # Semester logic
                try:
                    mes = int(fecha.split("-")[1])
                    semestre = "1" if mes <= 6 else "2"
                    anio_lectivo = f"2025-{semestre}"
                except:
                    anio_lectivo = "2025"

                id_inscripcion = f"{dni}_{cod_materia}_{anio_lectivo}"
                id_evaluacion = f"{id_inscripcion}_{fecha}"

                dnis.add(dni)
                careers.add(career_code)
                subjects.add(cod_materia)
                enrollments.add(id_inscripcion)
                evaluations.add(id_evaluacion)

        print("--- REPORTE DE VOLUMEN 2025 ---")
        print(f"Total de Filas: {total_rows}")
        print(f"Contactos (Alumnos): {len(dnis)}")
        print(f"Carreras: {len(careers)}")
        print(f"Materias: {len(subjects)}")
        print(f"Inscripciones: {len(enrollments)}")
        print(f"Evaluaciones: {len(evaluations)}")

    except Exception as e:
        print(f"Error analizando el archivo: {e}")


if __name__ == "__main__":
    analyze()
