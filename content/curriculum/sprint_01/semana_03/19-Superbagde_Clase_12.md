# Salesforce Admin + Agent Force (Superbadge Clase 12)

**Daily**
*   ¿Cómo venimos?
*   ¿Algo nos bloquea?
*   ¿Cómo estamos?

**Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol.

---

## SUPERBADGE
**LINK AL SUPERBADGE**

**Guia**: Consultar si Saben que es un administrador de Salesforce, si habian escuchado antes de rol.

---

### Superbadges: La Prueba de Fuego del Administrador

**¿Qué es un Superbadge?**
*   No es un módulo normal. Es una **Credencial basada en Habilidades**.
*   **Adiós a las instrucciones**: Aquí no existe el "Paso 1, haz clic aquí". Salesforce te da un Caso de Negocio (un problema real de una empresa ficticia) y tú debes decidir cómo resolverlo.
*   **Evaluación Automática**: Un "robot" entra a tu organización de Salesforce y verifica si la configuración funciona correctamente según los requisitos del cliente.

**¿Por qué son vitales para tu carrera?**
*   **El Puente Teórico-Práctico**: Los módulos te enseñan a usar el martillo; los Superbadges te piden construir una casa.
*   **Resume Booster (CV)**: Los reclutadores saben que un Superbadge no se consigue leyendo, se consigue haciendo. Valen mucho más que 100 badges normales.
*   **Prerrequisito de Certificación**: Para algunas certificaciones avanzadas, debes tener ciertos Superbadges completados.

> **¿Por qué son vitales para tu carrera?**
> *   **El Puente Teórico-Práctico**: Los módulos te enseñan a usar el martillo; los Superbadges te piden construir una casa.
> *   **Resume Booster (CV)**: Los reclutadores saben que un Superbadge no se consigue leyendo, se consigue haciendo. Valen mucho más que 100 badges normales.
> *   **Prerrequisito de Certificación**: Para algunas certificaciones avanzadas, debes tener ciertos Superbadges completados.

**ESTOS SB NO SON OBLIGATORIOS - SON OPCIONALES**

---

### ¡Manos a la obra!
Avanzamos con los trails.

**LINK de SP de seguridad**

En Salesforce, los datos son el activo más valioso.
Si no puedes protegerlos, no puedes administrar la plataforma. Este Superbadge no es solo un examen; es la prueba de que se les puede confiar las llaves del reino.

**Valor para su carrera:**
1.  **Como Admin/Consultant**: Es la habilidad técnica #1 que valida que entiendes el modelo de **"Confianza Cero"** y **"Privilegio Mínimo"**. Sin esto, no hay certificación de Admin avanzada.
2.  **Como Business Analyst (BA)**: Les enseña a hacer las preguntas correctas: "¿Quién debe ver este campo?" en lugar de solo "¿Qué campo necesitas?".
3.  **Como QA/Tester**: El 50% de los bugs críticos en UAT son de acceso. Aprenderán a probar "en negativo" (verificar que alguien no pueda ver lo que no debe).

### ¿Qué teoría van a aprender?
Estos Superbadge los obligará a dominar las tres capas de seguridad de Salesforce. Usa la analogía del "Edificio de Oficinas":
*   **Seguridad a Nivel de Objeto (Permisos CRUD)**: ¿Tienes tarjeta para entrar al edificio? (Profiles & Permission Sets).
    *   *Concepto clave*: La diferencia entre "Base" (Profile) y "Extensión" (Permission Set Groups).
*   **Seguridad a Nivel de Campo (FLS)**: Entraste a la oficina, pero ¿puedes ver lo que hay en los papeles sobre el escritorio?
    *   *Concepto clave*: Ocultar datos sensibles (salarios, SSN) incluso a usuarios con acceso al objeto.
*   **Seguridad a Nivel de Registro (Sharing)**: ¿Puedes ver todos los expedientes o solo los tuyos?
    *   *Concepto clave*: La pirámide de acceso: OWD (Org-Wide Defaults) > Role Hierarchy > Sharing Rules > Manual Sharing.
    *   **Punto vital para el Superbadge**: Entender que los OWD (Valores predeterminados de toda la organización) siempre deben ser **lo más restrictivos posible**.

### Nivel de Dificultad y Trampas Comunes
*   **Nivel**: Intermedio-Alto. No por la complejidad técnica, sino por la lógica.
*   Es un rompecabezas.
*   **El Reto**: El Superbadge simula un escenario real donde los requisitos son vagos o contradictorios.

**Trampa común (Tip de DevOps)**:
Muchos fallan porque intentan solucionar problemas de visibilidad de registro (Sharing) cambiando permisos de objeto (Profiles).
*   *Ejemplo*: "Si no veo el registro de Juan, no me des permiso de 'Ver Todo' en el perfil, mejor crea una Sharing Rule".

### Aplicación en un Proyecto Real
*   **El Escenario**: Una empresa implementa un proceso de "Evaluación de Desempeño".
*   **El BA (Ellos)**: Debe levantar el requerimiento: "Los Managers ven las evaluaciones de su equipo, pero no las de otros equipos. RRHH ve todo. Los empleados solo ven la suya".
*   **El Admin (Ellos)**: Configura OWD en 'Private', usa la Jerarquía de Roles para los Managers y Sharing Rules para RRHH.
*   **El QA (Ellos)**: Se loguea como un Manager y trata de buscar a un empleado de otro equipo. Si lo encuentra, el test falla.
*   **El DevOps (Ellos)**: Debe asegurarse de que estos cambios de perfil y sharing rules se desplieguen correctamente de Sandbox a Producción sin borrar permisos existentes.

### TIPS
Este Superbadge es su rito de iniciación. Cuando lo completen, dejarán de configurar 'a ver qué pasa' y empezarán a arquitectura seguridad con propósito.

*   **Tarea**: Revisar los Help Articles sobre "Record Ownership" antes de empezar, es donde la mayoría se atasca.

### Consejos de Supervivencia para el Superbadge
*   **Superbadge**: Security Specialist.
*   **Duración aprox**: 4 - 6 horas.
*   **Prerrequisitos**: Módulos de Data Security y Identity Basics.
*   **Concepto Estrella**: El principio de "Privilegio Mínimo" (Least Privilege).
*   **Tip de Oro**: ¡Nunca uses perfiles estándar para cumplir requisitos del Superbadge! Siempre clona o usa Permission Sets.

---

### Después de completar el Superbadge
Es **OBLIGATORIO** llenar el formulario.

1.  Cargar la imágen del SuperBadge
2.  Análisis de lo aprendido
3.  Llenar formulario de entrega

**SuperBadge**
**SPRINT 1**
