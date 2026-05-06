# 📝 Tarea: Campos personalizados

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Calidad de Datos**: Estrictamente tipados.
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../../Gestor_de_Versiones/03-Salesforce_Admin.md)

## Diccionario de Datos (Implementación)

Configuración de campos para cumplir los requisitos de Calidad (**[REQ-QUAL]**).

### Objeto: Student (`Student__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Record Name** | `Name` | Auto-Number | **[REQ-QUAL-003]**: Auto-generado `A-{YYYY}-{0000}`. |
| **National ID** | `National_ID__c` | Number(8,0) | **[REQ-QUAL-003]**: Unique + Required + ExtID. |
| **Email** | `Email__c` | Email | **[REQ-QUAL-001]**: Validación de formato regex. |

### Objeto: Enrollment (`Enrollment__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Cycle** | `Cycle__c` | Picklist | [REQ-DATA-002]: Diferencia historial. |
| **Status** | `Status__c` | Picklist | Enrolled, Passed, Failed. |

### Objeto: Exam (`Exam__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Final Grade** | `Final_Grade__c` | Number(4,2) | **[REQ-QUAL-002]**: Validación `Grade_Range_1_10`. |
| **Date** | `Date__c` | Date | **[REQ-FUNC-001]**: Fecha obligatoria. |
| **Attended?** | `Attended__c`| Checkbox | **[REQ-FUNC-002]**: Registro de Asistencia. |

---
**Nota**: Campos bloqueados para edición según [REQ-SEC-003].
