import csv
import unicodedata


def normalize_text(text):
    if not text:
        return ""
    # Normalize unicode to separate accents from characters
    normalized = unicodedata.normalize("NFD", text)
    # Filter out non-spacing mark (accents)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def clean_email(email):
    if not email:
        return ""
    if "@nuevo-email.com" in email.lower():
        return ""
    # Replace spaces with .
    email = email.replace(" ", ".")
    # Remove accents
    email = normalize_text(email)
    # Filter: Keep only English alphabet, numbers, and standard email symbols (@, ., _, -)
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789@._-"
    email = "".join(c for c in email.lower() if c in allowed_chars)
    return email


def clean_phone(phone):
    if not phone:
        return ""
    # Replace " 15 " with " 9 " (preserving spaces)
    return phone.replace(" 15 ", " 9 ")


input_file = r"content\Lumina_Tech\Archivos_intermedios\CSV\Historico_Alumnos_2025.csv"
output_file = (
    r"content\Lumina_Tech\Archivos_intermedios\CSV\Historico_Alumnos_2025_limpio.csv"
)

try:
    with open(input_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                row["Email"] = clean_email(row["Email"])
                row["Telefono"] = clean_phone(row["Telefono"])
                writer.writerow(row)
    print("SUCCESS: Archivo limpio generado correctamente para 2025.")
except Exception as e:
    print(f"ERROR: {e}")
