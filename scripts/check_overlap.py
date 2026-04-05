import csv

file_2024 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2024_limpio.csv"
file_2025 = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DataBase\Historico_Alumnos_2025_limpio.csv"


def check_overlap():
    dnis_2024 = set()
    dnis_2025 = set()

    with open(file_2024, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dnis_2024.add(row["DNI"])

    with open(file_2025, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dnis_2025.add(row["DNI"])

    overlap = dnis_2024.intersection(dnis_2025)

    print(f"Alumnos 2024: {len(dnis_2024)}")
    print(f"Alumnos 2025: {len(dnis_2025)}")
    print(f"Alumnos en AMBOS años: {len(overlap)}")

    if overlap:
        print("Ejemplos de alumnos compartidos:")
        for dni in list(overlap)[:5]:
            print(f"  - {dni}")


if __name__ == "__main__":
    check_overlap()
