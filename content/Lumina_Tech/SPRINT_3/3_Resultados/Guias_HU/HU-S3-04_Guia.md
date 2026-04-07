# 🎯 GUÍA DE IMPLEMENTACIÓN: HU-S3-04
**Nombre:** Screen Flow Privado (Reclamos - Case)
**Proyecto:** Lumina Tech University
**Audiencia:** Administradores Salesforce

### Paso 1: Crear el Flow que toma el ID automático
1. **Setup → Flows → New Screen Flow**.
2. Crea tu primer Screen y agrega:
   - Picklist (`inputMotivo`): Ponle de opciones: "Notas", "Certificados". Obligatorio.
   - Text Area (`inputProblema`): Label "Describe tu problema". Obligatorio.
3. Ahora la lógica: Agrega un **Create Records** → Object: `Case`.
4. Mapeo de campos:
   - `Subject` → `{!inputMotivo}`
   - `Description` → `{!inputProblema}`
   - `Origin` → `Web`
   - `Status` → `New`
   - **¡ATENCIÓN A ESTE:!** Busca el campo `ContactId`. En valor, borra y ve buscando: `$User` (Variable Global Usuario) → `ContactId`. Quedará así: `{!$User.ContactId}`. *(Esto vincula al caso con el alumno que tiene sesión iniciada).*
5. Guarda el flow como `Reclamo de Alumnado` y actívalo.

### Paso 2: Publicar en área privada
1. Ve al **Experience Builder**.
2. Dale click al título de la página arriba en el centro, y luego en el menú emergente, abajo dale a **+ New Page** -> Standard Page -> Flexible Layout. Llámala `Trámites`.
3. Notarás que el candado de esa página dice "Page Access: Default". Como es privada por defecto, déjalo así.
4. Arrastra el componente de **Flow**, suéltalo, selecciona tu Flow `Reclamo de Alumnado`.
5. **Publish.**
