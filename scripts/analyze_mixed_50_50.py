import csv

file_2024 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"
file_2025 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"


def get_sample_metrics(path, year_key, count):
    sample_dnis = set()
    rows = 0
    enrollments = set()
    evaluations = set()

    with open(path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        all_dnis = []
        for row in reader:
            d = row["DNI"]
            if d not in sample_dnis and len(sample_dnis) < count:
                sample_dnis.add(d)

        # Reset and read again for all records of these DNIS
        f.seek(0)
        reader = csv.DictReader(f)
        for row in reader:
            dni = row["DNI"]
            if dni in sample_dnis:
                rows += 1
                cod_materia = row["Codigo_Materia"]
                fecha = row["Fecha_Examen"]

                try:
                    mes = int(fecha.split("-")[1])
                    semestre = "1" if mes <= 6 else "2"
                    anio_lectivo = f"{year_key}-{semestre}"
                except:
                    anio_lectivo = year_key

                id_inscripcion = f"{dni}_{cod_materia}_{anio_lectivo}"
                id_evaluacion = f"{id_inscripcion}_{fecha}"

                enrollments.add(id_inscripcion)
                evaluations.add(id_evaluacion)

    return len(sample_dnis), len(enrollments), len(evaluations)


def analyze_50_50():
    c24, e24, v24 = get_sample_metrics(file_2024, "2024", 50)
    c25, e25, v25 = get_sample_metrics(file_2025, "2025", 50)

    total_c = c24 + c25
    total_e = e24 + e25
    total_v = v24 + v25
    total_r = total_c + total_e + total_v

    print("--- REPORTE MUESTRA MIXTA (50+50) ---")
    print(f"Contactos Totales: {total_c}")
    print(f"Inscripciones Totales: {total_e}")
    print(f"Evaluaciones Totales: {total_v}")
    print(f"SUMA TOTAL REGISTROS: {total_r}")
    print(f"ESPACIO ESTIMADO: {total_r * 2} KB ({round((total_r * 2)/1024, 2)} MB)")
    print(f"CAPACIDAD DISPONIBLE (5MB): {round(((total_r * 2)/1024)/5 * 100, 2)}%")


if __name__ == "__main__":
    analyze_50_50()
