import csv
import os

dirs = [
    r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\Limpieza\CSV\2024",
    r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\Limpieza\CSV\2025",
]


def check_file(filepath, key_fields):
    if not os.path.exists(filepath):
        print(f"ERROR: No existe {filepath}")
        return

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)
        total = len(rows)

        # Check total duplicates (entire row)
        unique_rows = set(tuple(row.items()) for row in rows)
        if len(unique_rows) < total:
            print(f"  [!] Filas duplicadas encontradas: {total - len(unique_rows)}")

        # Check key duplicates
        for key in key_fields:
            if key not in reader.fieldnames:
                continue
            values = [row[key] for row in rows]
            unique_values = set(values)
            if len(unique_values) < total:
                print(
                    f"  [!] Duplicados en columna '{key}': {total - len(unique_values)}"
                )
                # Mostrar ejemplo
                seen = set()
                dups = []
                for v in values:
                    if v in seen:
                        dups.append(v)
                    seen.add(v)
                print(f"      Ejemplos: {list(set(dups))[:3]}")


def audit():
    for d in dirs:
        print(f"\nAuditando directorio: {d}")
        year = d.split("\\")[-1]

        print("--- Carreras ---")
        check_file(os.path.join(d, f"00_Carga_Carreras_{year}.csv"), ["Abreviatura__c"])

        print("--- Contactos ---")
        check_file(
            os.path.join(d, f"01_Carga_Contactos_{year}.csv"), ["Numero_Documento__c"]
        )

        print("--- Materias ---")
        check_file(
            os.path.join(d, f"02_Carga_Materias_{year}.csv"), ["Codigo_Materia__c"]
        )

        print("--- Inscripciones ---")
        check_file(
            os.path.join(d, f"03_Carga_Inscripciones_{year}.csv"), ["ID_Importacion"]
        )

        print("--- Evaluaciones ---")
        check_file(
            os.path.join(d, f"04_Carga_Evaluaciones_{year}.csv"), ["ID_Importacion"]
        )

    # Auditoría Global entre años para Maestros
    print("\n\n--- Auditoría Global (Cruce 2024 vs 2025) ---")

    def get_column(path, col):
        if not os.path.exists(path):
            return set()
        with open(path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            return set(row[col] for row in reader)

    # Contactos Globales (DNI)
    dnis_24 = get_column(
        os.path.join(dirs[0], "01_Carga_Contactos_2024.csv"), "Numero_Documento__c"
    )
    dnis_25 = get_column(
        os.path.join(dirs[1], "01_Carga_Contactos_2025.csv"), "Numero_Documento__c"
    )
    repetidos = dnis_24.intersection(dnis_25)
    print(
        f"Contactos coincidentes en ambos años: {len(repetidos)} (Correcto, son alumnos recurrentes)"
    )

    # Materias Globales
    mat_24 = get_column(
        os.path.join(dirs[0], "02_Carga_Materias_2024.csv"), "Codigo_Materia__c"
    )
    mat_25 = get_column(
        os.path.join(dirs[1], "02_Carga_Materias_2025.csv"), "Codigo_Materia__c"
    )
    mat_rep = mat_24.intersection(mat_25)
    print(
        f"Materias coincidentes en ambos años: {len(mat_rep)} (Correcto, es el mismo catálogo)"
    )


if __name__ == "__main__":
    audit()
