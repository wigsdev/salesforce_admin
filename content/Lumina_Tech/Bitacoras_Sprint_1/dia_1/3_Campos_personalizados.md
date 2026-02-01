# 📝 Tarea: Campos personalizados

**Rol Responsable**: 🛡️ **Salesforce Admin**
**Calidad de Datos**: Estrictamente tipados.
**Destino en Gestor**: [`03-Salesforce_Admin.md`](../../Gestor_de_Versiones/03-Salesforce_Admin.md)

## Diccionario de Datos (Implementación)

Configuración de campos para cumplir los requisitos de Calidad (**[REQ-QUAL]**).

### Objeto: Alumno (`Alumno__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Legajo** | `Name` | Auto-Number | **[REQ-QUAL-003]**: Auto-generado `{L-0000}`. |
| **DNI** | `DNI__c` | Number(8,0) | **[REQ-QUAL-003]**: Unique + Required. |
| **Email** | `Email__c` | Email | **[REQ-QUAL-001]**: Validación de formato regex. |

### Objeto: Inscripción (`Inscripcion__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Ciclo Lectivo** | `Ciclo__c` | Picklist | [REQ-DATA-002]: Diferencia historial. |
| **Estado** | `Estado__c` | Picklist | En Curso, Aprobado, Reprobado. |

### Objeto: Examen (`Examen__c`)
| Label | API Name | Tipo | Reglas / REQ |
| :--- | :--- | :--- | :--- |
| **Nota** | `Nota__c` | Number(2,2) | **[REQ-QUAL-002]**: Validación `VR_Nota_Rango`. |
| **Fecha** | `Fecha__c` | Date | **[REQ-FUNC-001]**: Fecha obligatoria. |
| **Asistió?** | `Asistio__c`| Checkbox | **[REQ-FUNC-002]**: Registro de Asistencia. |

---
**Nota**: Campos bloqueados para edición según [REQ-SEC-003].
