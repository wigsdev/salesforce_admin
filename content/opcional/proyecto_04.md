# 🏆 Proyecto 4: Simulador de Torneo de Fútbol

Entregables:
1. Diagrama de flujo del registro de partidos
2. Diagrama de flujo de actualización de puntos
3. Pseudocódigo del sistema
4. Código C++
5. Ejecución del programa

## FASE 1: Estructura de Datos

### Variables Globales (Sin usar ARREGLOS)
```text
CONSTANTE MAX_EQUIPOS = 4
VARIABLE GLOBAL numEquipos = 0

// Variables Equipo 1
string e1_nombre;
int e1_pj, e1_pg, e1_pe, e1_pp, e1_gf, e1_gc, e1_puntos;

// Variables Equipo 2
string e2_nombre;
int e2_pj, e2_pg, e2_pe, e2_pp, e2_gf, e2_gc, e2_puntos;

// Variables Equipo 3
string e3_nombre;
int e3_pj, e3_pg, e3_pe, e3_pp, e3_gf, e3_gc, e3_puntos;

// Variables Equipo 4
string e4_nombre;
int e4_pj, e4_pg, e4_pe, e4_pp, e4_gf, e4_gc, e4_puntos;
```

---

## FASE 2: Diagrama de Flujo — Menú Principal

```mermaid
flowchart TD
    A([INICIO]) --> B[Mostrar Menú]
    B --> C{¿Opción del usuario?}
    C -->|1| D[Registrar equipos]
    C -->|2| E[Registrar partido]
    C -->|3| F[Mostrar tabla]
    C -->|4| G[Buscar equipo]
    C -->|5| H[Ver campeón]
    C -->|0| I([FIN])
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
```

---

## FASE 3: Diagrama de Flujo — Registrar Partido

> **Entregable 1 del proyecto**

```mermaid
flowchart TD
    A([INICIO]) --> B{¿numEquipos < 2?}
    B -->|Sí| C[Mostrar Error: Faltan equipos]
    C --> Z([FIN])
    B -->|No| D[Mostrar listado de Equipos Registrados]
    D --> E[Pedir índice Equipo 1]
    E --> F[Pedir índice Equipo 2]
    F --> G{¿El índice E1 o E2 es mayor a numEquipos o son iguales?}
    G -->|Sí| H[Mostrar Error: Inválido]
    H --> Z
    G -->|No| I[Pedir Goles E1]
    I --> J[Pedir Goles E2]
    J --> K[Actualizar puntos y estadísticas]
    K --> Z
```

---

## FASE 4: Diagrama de Flujo — Actualización de Puntos

> **Entregable 2 del proyecto**

```mermaid
flowchart TD
    A([INICIO]) --> B[Incrementar PJ del equipo 1 y 2]
    B --> C[Actualizar GF y GC]
    C --> D{¿Resultado?}
    D -->|Victoria E1| E[E1: PG++, Puntos+=3 / E2: PP++]
    D -->|Empate| F[E1 y E2: PE++, Puntos+=1]
    D -->|Victoria E2| G[E1: PP++ / E2: PG++, Puntos+=3]
    E --> H([FIN])
    F --> H
    G --> H
```

---

## FASE 5: Pseudocódigo del Sistema Completo

> **Entregable 3 del proyecto**

### 5.1 — Lógica del CASO 1: Registrar Equipo
```text
CASO 1:
    SI numEquipos >= MAX_EQUIPOS ENTONCES
        MOSTRAR "Límite de equipos alcanzado"
        ROMPER (break)
    
    LEER nombre del nuevo equipo
    
    // Validación de nombres (en vez de arreglo, se usan IFs)
    yaExiste = FALSO
    SI numEquipos >= 1 Y nombre == e1_nombre ENTONCES yaExiste = VERDADERO
    SI numEquipos >= 2 Y nombre == e2_nombre ENTONCES yaExiste = VERDADERO
    SI numEquipos >= 3 Y nombre == e3_nombre ENTONCES yaExiste = VERDADERO
    SI numEquipos >= 4 Y nombre == e4_nombre ENTONCES yaExiste = VERDADERO

    SI yaExiste ENTONCES
        MOSTRAR "Equipo ya registrado"
    SINO
        SI numEquipos == 0 ENTONCES
            e1_nombre = nombre
        SINO SI numEquipos == 1 ENTONCES
            e2_nombre = nombre
        SINO SI numEquipos == 2 ENTONCES
            e3_nombre = nombre
        SINO SI numEquipos == 3 ENTONCES
            e4_nombre = nombre
        
        numEquipos++
        MOSTRAR "Equipo registrado correctamente"
        
    ROMPER (break)
```

### 5.2 — Lógica del CASO 2: Registrar Partido
```text
CASO 2:
    SI numEquipos < 2 ENTONCES
        MOSTRAR "Se necesitan al menos 2 equipos"
        ROMPER (break)

    MOSTRAR lista de equipos mediante (SI numEquipos >= X)

    LEER indiceE1
    LEER indiceE2

    SI indiceE1 coincide con rango Y indiceE2 coincide con rango Y indice1 != indice2 ENTONCES
        LEER golesE1
        LEER golesE2

        // Ejemplo: Si indiceE1 == 1, actualizar e1_pj, e1_gf, etc.
        SI indiceE1 == 1 ENTONCES
            e1_pj++ 
            e1_gf += golesE1
            e1_gc += golesE2
            SI golesE1 > golesE2 ENTONCES e1_pg++; e1_puntos += 3
            SINO SI golesE1 == golesE2 ENTONCES e1_pe++; e1_puntos += 1
            SINO e1_pp++
        SINO SI indiceE1 == 2 ENTONCES ... 

        // Repetir exactamente la misma lógica cruzada para indiceE2
    SINO
        MOSTRAR "Equipo no encontrado o son el mismo"
    ROMPER (break)
```

### 5.3 — Lógica del CASO 3: Mostrar Tabla
```text
CASO 3:
    MOSTRAR cabecera: "Equipo | PJ | PG | PE | PP | GF | GC | Puntos"
    
    SI numEquipos >= 1 ENTONCES 
        MOSTRAR e1_nombre, e1_pj, e1_pg, e1_pe, e1_pp, e1_gf, e1_gc, e1_puntos
    SI numEquipos >= 2 ENTONCES
        MOSTRAR e2_nombre, e2_pj, e2_pg, e2_pe, e2_pp, e2_gf, e2_gc, e2_puntos
    SI numEquipos >= 3 ENTONCES
        MOSTRAR e3_nombre ...
    SI numEquipos >= 4 ENTONCES
        MOSTRAR e4_nombre ...
    ROMPER (break)
```

### 5.4 — Lógica del CASO 4: Buscar Equipo
```text
CASO 4:
    LEER nombreBuscado
    encontrado = FALSO
    
    SI numEquipos >= 1 Y nombreBuscado == e1_nombre ENTONCES
        MOSTRAR datos e1_nombre
        encontrado = VERDADERO
    SINO SI numEquipos >= 2 Y nombreBuscado == e2_nombre ENTONCES
        MOSTRAR datos e2_nombre
        encontrado = VERDADERO
    ... (hasta 4)
    
    SI NO encontrado ENTONCES
        MOSTRAR "Equipo no encontrado"
    ROMPER (break)
```

### 5.5 — Lógica del CASO 5: Mostrar Campeón
```text
CASO 5:
    SI numEquipos == 0 ENTONCES
        MOSTRAR "No hay equipos registrados"
        ROMPER (break)
    
    campeon_nombre = e1_nombre; max_puntos = e1_puntos
    
    SI numEquipos >= 2 Y e2_puntos > max_puntos ENTONCES campeon_nombre = e2_nombre; max_puntos = e2_puntos
    SI numEquipos >= 3 Y e3_puntos > max_puntos ENTONCES campeon_nombre = e3_nombre; max_puntos = e3_puntos
    SI numEquipos >= 4 Y e4_puntos > max_puntos ENTONCES campeon_nombre = e4_nombre; max_puntos = e4_puntos
    
    MOSTRAR "🏆 Campeón: " + campeon_nombre
    MOSTRAR "Puntos: " + max_puntos
    ROMPER (break)
```

### 5.6 — Estructura Principal: do-while y switch
```text
PROGRAMA PRINCIPAL:
    opcion = -1
    
    HACER:
        MOSTRAR menú de opciones (1-5, 0 para salir)
        LEER opcion
        
        SEGÚN opcion:
            CASO 1: (Lógica explícita en el sub-apartado 5.1)
            CASO 2: (Lógica explícita en el sub-apartado 5.2)
            CASO 3: (Lógica explícita en el sub-apartado 5.3)
            CASO 4: (Lógica explícita en el sub-apartado 5.4)
            CASO 5: (Lógica explícita en el sub-apartado 5.5)
            CASO 0: MOSTRAR "¡Hasta luego!"; ROMPER (break)
            POR DEFECTO: MOSTRAR "Opción inválida"; ROMPER (break)
    
    MIENTRAS opcion != 0
```

---

