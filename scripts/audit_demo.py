import csv
import os

demo_dir = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\content\Lumina_Tech\Archivos_intermedios\CSV\DEMO"
report_path = r"c:\Users\WIGUSA\Documents\GitHub\admin_salesforce\demo_audit_report.md"


def audit_demo_files():
    report = "# Reporte de Auditoría DEMO (200 Alumnos)\n\n"
    files_to_check = [
        ("00_Carga_Carreras_DEMO.csv", ["Abreviatura__c"]),
        ("01_Carga_Contactos_DEMO.csv", ["Numero_Documento__c"]),
        ("02_Carga_Materias_DEMO.csv", ["Codigo_Materia__c"]),
        ("03_Carga_Inscripciones_DEMO.csv", ["ID_Importacion"]),
        ("04_Carga_Evaluaciones_DEMO.csv", ["ID_Evaluacion"]),
    ]

    all_data = {}

    for filename, keys in files_to_check:
        filepath = os.path.join(demo_dir, filename)
        if not os.path.exists(filepath):
            report += f"### {filename}\n- [ERROR] Archivo no encontrado.\n\n"
            continue

        with open(filepath, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            all_data[filename] = rows
            total = len(rows)

            issues = []
            # Duplicates in rows
            unique_rows = set(tuple(row.items()) for row in rows)
            if len(unique_rows) < total:
                issues.append(
                    f"  - [ALERTA] Filas duplicadas: {total - len(unique_rows)}"
                )

            # Duplicates in keys
            for key in keys:
                values = [row[key] for row in rows]
                if len(set(values)) < total:
                    issues.append(
                        f"  - [ALERTA] Llave duplicada `{key}`: {total - len(set(values))}"
                    )

            status = "✅ Limpio" if not issues else "\n".join(issues)
            report += f"### {filename}\n- Registros: {total}\n- Estado: {status}\n\n"

    # Integrity cross-checks
    report += "## Integridad Referencial\n"

    # 1. Enrollments -> Contacts
    if (
        "03_Carga_Inscripciones_DEMO.csv" in all_data
        and "01_Carga_Contactos_DEMO.csv" in all_data
    ):
        contact_ids = set(
            r["Numero_Documento__c"] for r in all_data["01_Carga_Contactos_DEMO.csv"]
        )
        enroll_contact_ids = set(
            r["Numero_Documento__c"]
            for r in all_data["03_Carga_Inscripciones_DEMO.csv"]
        )
        missing = enroll_contact_ids - contact_ids
        if not missing:
            report += f"- [Contactos] ✅ Todas las {len(all_data['03_Carga_Inscripciones_DEMO.csv'])} inscripciones tienen un alumno válido.\n"
        else:
            report += (
                f"- [Contactos] ❌ ERROR: {len(missing)} inscripciones huérfanas.\n"
            )

    # 2. Evaluations -> Enrollments
    if (
        "04_Carga_Evaluaciones_DEMO.csv" in all_data
        and "03_Carga_Inscripciones_DEMO.csv" in all_data
    ):
        enroll_ids = set(
            r["ID_Importacion"] for r in all_data["03_Carga_Inscripciones_DEMO.csv"]
        )
        eval_enroll_ids = set(
            r["ID_Inscripcion"] for r in all_data["04_Carga_Evaluaciones_DEMO.csv"]
        )
        missing = eval_enroll_ids - enroll_ids
        if not missing:
            report += f"- [Inscripciones] ✅ Todos los {len(all_data['04_Carga_Evaluaciones_DEMO.csv'])} exámenes tienen una inscripción válida.\n"
        else:
            report += (
                f"- [Inscripciones] ❌ ERROR: {len(missing)} exámenes huérfanos.\n"
            )

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Auditoría completada. Reporte en: {report_path}")


if __name__ == "__main__":
    audit_demo_files()
