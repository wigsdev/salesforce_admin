import csv
import os

dirs = {
    "2024": r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\Limpieza\CSV\2024",
    "2025": r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\Limpieza\CSV\2025",
}

report_path = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\audit_report.md"


def check_file(year, filepath, key_fields):
    if not os.path.exists(filepath):
        return f"### {os.path.basename(filepath)}\n- [ERROR] Archivo no encontrado.\n"

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        rows = list(reader)
        total = len(rows)
        issues = []

        # Unique rows
        unique_rows = set(tuple(row.items()) for row in rows)
        if len(unique_rows) < total:
            issues.append(
                f"  - **[ALERTA]** Filas duplicadas: {total - len(unique_rows)}"
            )

        # Unique keys
        for key in key_fields:
            if key not in reader.fieldnames:
                continue
            values = [row[key] for row in rows]
            unique_values = set(values)
            if len(unique_values) < total:
                issues.append(
                    f"  - **[ALERTA]** Duplicados en llave `{key}`: {total - len(unique_values)}"
                )

        status = "✅ Sin duplicados" if not issues else "".join(issues)
        return f"### {os.path.basename(filepath)}\n- Total registros: {total}\n- Estado: {status}\n\n"


def run_audit():
    report = "# Reporte de Auditoría de Datos (Sprint 2)\n\n"

    for year, path in dirs.items():
        report += f"## Año {year}\n"
        report += check_file(
            year,
            os.path.join(path, f"00_Carga_Carreras_{year}.csv"),
            ["Abreviatura__c"],
        )
        report += check_file(
            year,
            os.path.join(path, f"01_Carga_Contactos_{year}.csv"),
            ["Numero_Documento__c"],
        )
        report += check_file(
            year,
            os.path.join(path, f"02_Carga_Materias_{year}.csv"),
            ["Codigo_Materia__c"],
        )
        report += check_file(
            year,
            os.path.join(path, f"03_Carga_Inscripciones_{year}.csv"),
            ["ID_Importacion"],
        )
        report += check_file(
            year,
            os.path.join(path, f"04_Carga_Evaluaciones_{year}.csv"),
            ["ID_Evaluacion"],
        )

    # Check consistency 03 vs 04
    report += "## Consistencia entre Objetos (Inscripciones vs Evaluaciones)\n"
    for year, path in dirs.items():
        file03 = os.path.join(path, f"03_Carga_Inscripciones_{year}.csv")
        file04 = os.path.join(path, f"04_Carga_Evaluaciones_{year}.csv")

        if os.path.exists(file03) and os.path.exists(file04):
            with open(file03, mode="r", encoding="utf-8") as f:
                ids03 = set(
                    row["ID_Importacion"] for row in csv.DictReader(f, delimiter=",")
                )
            with open(file04, mode="r", encoding="utf-8") as f:
                ids04 = set(
                    row["ID_Inscripcion"] for row in csv.DictReader(f, delimiter=",")
                )

            missing = ids04 - ids03
            if not missing:
                report += f"- **Año {year}:** ✅ Todos los {len(ids04)} exámenes tienen una inscripción válida.\n"
            else:
                report += f"- **Año {year}:** ❌ ERROR: {len(missing)} exámenes no tienen inscripción (IDs huérfanos).\n"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Reporte generado en: {report_path}")


if __name__ == "__main__":
    run_audit()
