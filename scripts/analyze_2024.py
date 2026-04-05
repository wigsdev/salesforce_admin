import csv
from collections import Counter

file_path = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"


def analyze_2024():
    months = []
    total_rows = 0
    dnis = set()

    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_rows += 1
                dni = row["DNI"]
                fecha = row["Fecha_Examen"]
                dnis.add(dni)

                try:
                    mes = int(fecha.split("-")[1])
                    months.append(mes)
                except:
                    pass

        month_counts = Counter(months)
        print("--- REPORTE DE VOLUMEN 2024 ---")
        print(f"Total de Filas: {total_rows}")
        print(f"Contactos únicos: {len(dnis)}")
        print("Distribución por Mes:")
        for m in sorted(month_counts.keys()):
            print(f"  Mes {m:02}: {month_counts[m]} registros")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    analyze_2024()
