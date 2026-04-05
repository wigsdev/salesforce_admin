import csv

file_2024 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"
file_2025 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"


def analyze_cohort():
    # 1. Select 100 unique DNI from 2024 as the base cohort
    cohort_dnis = set()
    try:
        with open(file_2024, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cohort_dnis.add(row["DNI"])
                if len(cohort_dnis) >= 100:
                    break
    except Exception as e:
        print(f"Error reading 2024 base: {e}")
        return

    # Metrics
    metrics = {
        "2024": {"rows": 0, "enrollments": set(), "evaluations": set()},
        "2025": {"rows": 0, "enrollments": set(), "evaluations": set()},
    }

    def process_file(path, year_key):
        try:
            with open(path, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dni = row["DNI"]
                    if dni in cohort_dnis:
                        metrics[year_key]["rows"] += 1
                        cod_materia = row["Codigo_Materia"]
                        fecha = row["Fecha_Examen"]

                        # Semester logic
                        try:
                            mes = int(fecha.split("-")[1])
                            semestre = "1" if mes <= 6 else "2"
                            anio_lectivo = f"{year_key}-{semestre}"
                        except:
                            anio_lectivo = year_key

                        id_inscripcion = f"{dni}_{cod_materia}_{anio_lectivo}"
                        id_evaluacion = f"{id_inscripcion}_{fecha}"

                        metrics[year_key]["enrollments"].add(id_inscripcion)
                        metrics[year_key]["evaluations"].add(id_evaluacion)
        except Exception as e:
            print(f"Error processing {year_key}: {e}")

    process_file(file_2024, "2024")
    process_file(file_2025, "2025")

    total_enrollments = len(
        metrics["2024"]["enrollments"] | metrics["2025"]["enrollments"]
    )
    total_evaluations = len(
        metrics["2024"]["evaluations"] | metrics["2025"]["evaluations"]
    )

    # Salesforce calculates 1 record as 2KB.
    # Objects involved: Contact (Cohort Size), Enrollment (Total Unique), Evaluation (Total Unique)
    total_records = len(cohort_dnis) + total_enrollments + total_evaluations

    print("--- REPORTE DE COHORTE (100 ALUMNOS) ---")
    print(f"Alumnos en la muestra: {len(cohort_dnis)}")
    print("\nDetalle 2024:")
    print(f"  Filas procesadas: {metrics['2024']['rows']}")
    print(f"  Inscripciones únicas: {len(metrics['2024']['enrollments'])}")
    print(f"  Evaluaciones únicas: {len(metrics['2024']['evaluations'])}")

    print("\nDetalle 2025:")
    print(f"  Filas procesadas: {metrics['2025']['rows']}")
    print(f"  Inscripciones únicas: {len(metrics['2025']['enrollments'])}")
    print(f"  Evaluaciones únicas: {len(metrics['2025']['evaluations'])}")

    print("\nTotales Consolidados (Salesforce):")
    print(f"  Contactos: {len(cohort_dnis)}")
    print(f"  Inscripciones (Inscripcion__c): {total_enrollments}")
    print(f"  Evaluaciones (Evaluacion__c): {total_evaluations}")
    print(f"  SUMA TOTAL REGISTROS: {total_records}")
    print(
        f"  ESPACIO ESTIMADO: {total_records * 2} KB ({round((total_records * 2)/1024, 2)} MB)"
    )
    print(
        f"  CAPACIDAD DISPONIBLE (5MB): {round(((total_records * 2)/1024)/5 * 100, 2)}%"
    )


if __name__ == "__main__":
    analyze_cohort()
