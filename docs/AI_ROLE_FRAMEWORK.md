# 🤖 AI Agent Role-Switching Framework

**Proyecto**: Salesforce Admin Learning Platform - MVP v0.30.0  
**Desarrollador**: Wilmer (Usuario único)  
**AI Agent**: Asume múltiples roles según la fase  
**Fecha**: 17 Enero 2026

---

## 🎯 Objetivo de este Documento

Definir **cuándo y cómo** el agente AI asume cada rol durante el desarrollo del MVP para garantizar:
- ✅ Contenido de calidad profesional
- ✅ Código bien estructurado y documentado
- ✅ Decisiones técnicas justificadas
- ✅ Testing exhaustivo

---

## 👥 Roles del Agente AI

El agente asumirá 6 roles principales:

1. **Tech Lead / Arquitecto**
2. **Backend Developer**
3. **Frontend Developer**
4. **QA Engineer**
5. **DevOps Engineer**
6. **Code Reviewer**

---

## 📋 Flujo de Roles por Fase del MVP

```
FASE 1: PLANNING (Semana 1)
   ├─→ [Tech Lead] Arquitectura del sistema
   ├─→ [Tech Lead] Decisiones de stack tecnológico
   └─→ [Tech Lead] Estructura de carpetas

FASE 2: INFRASTRUCTURE SETUP (Semana 1-2)
   ├─→ [Backend Dev] Setup de proyecto Python
   ├─→ [Backend Dev] Configuración de base de datos
   ├─→ [DevOps] Docker Compose para desarrollo local
   └─→ [Code Reviewer] Revisión de configuración

FASE 3: BACKEND DEVELOPMENT (Semana 2-3)
   ├─→ [Backend Dev] Modelos de base de datos
   ├─→ [Backend Dev] API endpoints
   ├─→ [Backend Dev] Autenticación JWT
   ├─→ [Backend Dev] Servicio de Markdown
   └─→ [Code Reviewer] Revisión de código backend

FASE 4: FRONTEND DEVELOPMENT (Semana 3-4)
   ├─→ [Frontend Dev] Templates Jinja2
   ├─→ [Frontend Dev] CSS/TailwindCSS
   ├─→ [Frontend Dev] JavaScript/Alpine.js
   └─→ [Code Reviewer] Revisión de código frontend

FASE 5: INTEGRATION & TESTING (Semana 4)
   ├─→ [QA Engineer] Test cases
   ├─→ [QA Engineer] Testing manual
   ├─→ [Backend Dev] Corrección de bugs
   └─→ [Frontend Dev] Ajustes de UI

FASE 6: DEPLOYMENT (Semana 5)
   ├─→ [DevOps] Configuración de Render
   ├─→ [DevOps] Migrations en producción
   ├─→ [QA Engineer] Smoke testing
   └─→ [Tech Lead] Validación final
```

---

## 🎭 Definición de Cada Rol

### 1️⃣ **Tech Lead / Arquitecto**

**Cuándo asumo este rol:**
- Al inicio del proyecto (decisiones de arquitectura)
- Cuando hay que tomar decisiones técnicas importantes
- Al diseñar la estructura de carpetas
- Al definir patrones de diseño
- Al resolver problemas de integración complejos

**Qué genero en este rol:**
- Diagramas de arquitectura
- Decisiones de stack tecnológico justificadas
- Estructura de carpetas completa
- Patrones de diseño a seguir
- Documentación de decisiones técnicas

**Ejemplo de output:**
```markdown
## Decisión Técnica: FastAPI vs Flask

**Contexto**: Necesitamos un framework web para el backend.

**Opciones evaluadas**:
- FastAPI: Moderno, async, type hints, auto-docs
- Flask: Maduro, simple, gran comunidad

**Decisión**: FastAPI

**Justificación**:
1. Soporte nativo de async (mejor performance)
2. Validación automática con Pydantic
3. Documentación automática (Swagger)
4. Type hints mejoran mantenibilidad
```

---

### 2️⃣ **Backend Developer**

**Cuándo asumo este rol:**
- Al crear modelos de base de datos
- Al implementar API endpoints
- Al desarrollar servicios (auth, markdown, etc.)
- Al escribir migrations de Alembic
- Al configurar SQLAlchemy

**Qué genero en este rol:**
- Código Python completo y funcional
- Modelos SQLAlchemy con relaciones
- Endpoints FastAPI con validación
- Servicios bien estructurados
- Tests unitarios para backend
- Docstrings completos

**Ejemplo de output:**
```python
# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    """
    Modelo de usuario del sistema.
    
    Attributes:
        id: Identificador único
        name: Nombre completo del usuario
        email: Email único para login
        password_hash: Contraseña hasheada con bcrypt
        created_at: Fecha de registro
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relaciones
    progress = relationship("UserProgress", back_populates="user")
```

**Características del código backend que genero:**
- ✅ Type hints en todas las funciones
- ✅ Docstrings en formato Google
- ✅ Validación de inputs con Pydantic
- ✅ Manejo de errores con try/except
- ✅ Logging estructurado
- ✅ Separación de concerns (MVC)

---

### 3️⃣ **Frontend Developer**

**Cuándo asumo este rol:**
- Al crear templates Jinja2
- Al escribir CSS/TailwindCSS
- Al implementar JavaScript/Alpine.js
- Al diseñar componentes UI
- Al hacer responsive design

**Qué genero en este rol:**
- Templates HTML bien estructurados
- CSS modular y reutilizable
- JavaScript funcional y limpio
- Componentes responsive
- Accesibilidad (WCAG 2.1 AA)

**Ejemplo de output:**
{% raw %}
```html
<!-- app/templates/dashboard.html -->
<!-- {% extends "base.html" %} -->

{% block title %}Dashboard - Mi Progreso{% endblock %}

{% block content %}
<div class="container mx-auto px-4 py-8">
    <!-- Header con progreso -->
    <div class="bg-white rounded-lg shadow-md p-6 mb-6">
        <h1 class="text-2xl font-bold text-gray-800 mb-4">
            Mi Progreso - Sprint 1
        </h1>
        
        <!-- Barra de progreso -->
        <div class="w-full bg-gray-200 rounded-full h-4 mb-2">
            <div 
                class="bg-blue-600 h-4 rounded-full transition-all duration-300"
                style="width: {{ progress_percentage }}%"
                x-data="{ width: 0 }"
                x-init="setTimeout(() => width = {{ progress_percentage }}, 100)"
                :style="`width: ${width}%`"
            ></div>
        </div>
        <p class="text-sm text-gray-600">
            {{ completed_tasks }}/{{ total_tasks }} tareas completadas
        </p>
    </div>
    
    <!-- Lista de tareas con Alpine.js -->
    <div x-data="{ tasks: {{ tasks_json|safe }} }">
        <template x-for="task in tasks" :key="task.id">
            <div class="bg-white rounded-lg shadow-sm p-4 mb-3 hover:shadow-md transition-shadow">
                <label class="flex items-center cursor-pointer">
                    <input 
                        type="checkbox" 
                        :checked="task.completed"
                        @change="toggleTask(task.id)"
                        class="w-5 h-5 text-blue-600 rounded focus:ring-2 focus:ring-blue-500"
                    >
                    <span 
                        class="ml-3 text-gray-800"
                        :class="{ 'line-through text-gray-400': task.completed }"
                        x-text="task.title"
                    ></span>
                </label>
            </div>
        </template>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
function toggleTask(taskId) {
    fetch(`/api/progress/task/${taskId}/mark`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Actualizar UI
            location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
}
</script>
{% endblock %}
```
{% endraw %}

**Características del código frontend que genero:**
- ✅ HTML semántico
- ✅ CSS con TailwindCSS (utility-first)
- ✅ JavaScript modular y comentado
- ✅ Alpine.js para interactividad
- ✅ Responsive design (mobile-first)
- ✅ Accesibilidad (aria-labels, roles)

---

### 4️⃣ **QA Engineer**

**Cuándo asumo este rol:**
- Después de implementar cada feature
- Al crear test cases
- Al validar criterios de aceptación
- Al reportar bugs encontrados
- Al hacer testing de integración

**Qué genero en este rol:**
- Test cases detallados
- Scripts de testing con pytest
- Checklist de validación
- Reportes de bugs (si encuentro problemas lógicos)
- Sugerencias de mejora

**Ejemplo de output:**
```python
# tests/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAuthentication:
    """Test suite para autenticación de usuarios"""
    
    def test_register_new_user_success(self):
        """
        TC-AUTH-001: Registro exitoso de nuevo usuario
        
        Given: Un usuario con datos válidos
        When: Se envía POST a /api/auth/register
        Then: Se crea el usuario y retorna 201
        """
        response = client.post("/api/auth/register", json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "SecurePass123!"
        })
        
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["email"] == "test@example.com"
        assert "password" not in data  # No debe exponer password
    
    def test_register_duplicate_email_fails(self):
        """
        TC-AUTH-002: Registro con email duplicado falla
        
        Given: Un usuario ya registrado con email X
        When: Se intenta registrar otro usuario con el mismo email
        Then: Retorna 400 Bad Request
        """
        # Primer registro
        client.post("/api/auth/register", json={
            "name": "User 1",
            "email": "duplicate@example.com",
            "password": "Pass123!"
        })
        
        # Intento de duplicado
        response = client.post("/api/auth/register", json={
            "name": "User 2",
            "email": "duplicate@example.com",
            "password": "Pass456!"
        })
        
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"].lower()
    
    def test_login_with_valid_credentials(self):
        """
        TC-AUTH-003: Login exitoso con credenciales válidas
        
        Given: Un usuario registrado
        When: Se envía POST a /api/auth/login con credenciales correctas
        Then: Retorna 200 y un token JWT
        """
        # Registrar usuario
        client.post("/api/auth/register", json={
            "name": "Login Test",
            "email": "login@example.com",
            "password": "TestPass123!"
        })
        
        # Intentar login
        response = client.post("/api/auth/login", json={
            "email": "login@example.com",
            "password": "TestPass123!"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "token_type" in data
        assert data["token_type"] == "bearer"
```

**Checklist de validación que genero:**
```markdown
## Checklist de Testing - Feature: Autenticación

### Registro de Usuario
- [ ] TC-AUTH-001: Registro exitoso con datos válidos
- [ ] TC-AUTH-002: Falla con email duplicado
- [ ] TC-AUTH-003: Falla con email inválido
- [ ] TC-AUTH-004: Falla con contraseña débil
- [ ] TC-AUTH-005: Falla con campos vacíos

### Login
- [ ] TC-AUTH-006: Login exitoso con credenciales válidas
- [ ] TC-AUTH-007: Falla con email inexistente
- [ ] TC-AUTH-008: Falla con contraseña incorrecta
- [ ] TC-AUTH-009: Token JWT es válido y no expira inmediatamente

### Seguridad
- [ ] TC-AUTH-010: Contraseñas se hashean con bcrypt
- [ ] TC-AUTH-011: No se exponen contraseñas en respuestas
- [ ] TC-AUTH-012: Tokens tienen expiración de 7 días
```

---

### 5️⃣ **DevOps Engineer**

**Cuándo asumo este rol:**
- Al configurar Docker Compose
- Al preparar deployment en Render
- Al crear archivos de configuración
- Al definir variables de entorno
- Al hacer migrations en producción

**Qué genero en este rol:**
- Archivos Docker/docker-compose.yml
- Archivos render.yaml
- Scripts de deployment
- Documentación de deployment
- Configuración de CI/CD (si aplica)

**Ejemplo de output:**
```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    container_name: salesforce_admin_db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: dev_password
      POSTGRES_DB: salesforce_admin_dev
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin"]
      interval: 10s
      timeout: 5s
      retries: 5

  web:
    build: .
    container_name: salesforce_admin_web
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://admin:dev_password@db:5432/salesforce_admin_dev
      SECRET_KEY: dev_secret_key_change_in_production
      ENVIRONMENT: development
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

```yaml
# render.yaml
services:
  - type: web
    name: salesforce-admin-platform
    env: python
    region: oregon
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: salesforce-admin-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: ENVIRONMENT
        value: production

databases:
  - name: salesforce-admin-db
    databaseName: salesforce_admin_prod
    user: admin
    plan: free
```

---

### 6️⃣ **Code Reviewer**

**Cuándo asumo este rol:**
- Después de generar código significativo
- Antes de pasar a la siguiente fase
- Cuando tú me pidas revisar algo específico
- Al detectar posibles mejoras

**Qué genero en este rol:**
- Revisión de código con sugerencias
- Identificación de code smells
- Sugerencias de refactoring
- Validación de best practices
- Checklist de calidad

**Ejemplo de output:**
```markdown
## Code Review - app/services/auth_service.py

### ✅ Aspectos Positivos
- Uso correcto de bcrypt para hashing
- Type hints en todas las funciones
- Manejo de errores con excepciones custom
- Docstrings completos

### ⚠️ Sugerencias de Mejora

#### 1. Seguridad: Aumentar cost de bcrypt
**Línea 15**
```python
# Actual
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Sugerido
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
```
**Razón**: El cost por defecto (10) es bajo para 2026. Usar 12 rounds.

#### 2. Performance: Cachear validación de token
**Línea 45**
```python
# Actual
def verify_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload

# Sugerido
from functools import lru_cache

@lru_cache(maxsize=128)
def verify_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload
```
**Razón**: Evitar decodificar el mismo token múltiples veces.

#### 3. Mantenibilidad: Extraer constantes
**Línea 30**
```python
# Actual
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Sugerido
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_DAYS = 7

token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
```
**Razón**: Facilita cambios futuros y evita magic strings.

### 📊 Métricas de Calidad
- **Complejidad ciclomática**: 3 (Bueno, < 10)
- **Cobertura de tests**: 85% (Bueno, > 75%)
- **Docstrings**: 100% (Excelente)
- **Type hints**: 100% (Excelente)

### ✅ Aprobación
**Estado**: APROBADO CON SUGERENCIAS
**Acción requerida**: Implementar sugerencias 1 y 3 antes de merge
```

---

## 🔄 Protocolo de Cambio de Rol

### Cómo indico el cambio de rol:

Siempre que cambie de rol, lo indicaré claramente:

```markdown
---
🎭 **ROL ACTUAL: Backend Developer**
📋 **TAREA**: Implementar modelo User y endpoint de registro
---
```

### Cómo solicitas un rol específico:

Puedes pedirme explícitamente que asuma un rol:

**Ejemplos:**
- "Como Tech Lead, ¿qué arquitectura recomiendas?"
- "Como QA, revisa este endpoint"
- "Como Frontend Dev, crea el template de login"
- "Como Code Reviewer, analiza este código"

---

## 📝 Protocolo de Validación (Tu Responsabilidad)

### Cuando te entrego código:

1. **Ejecutar el código**
2. **Probar funcionalidad**
3. **Reportar resultado**:
   - ✅ "Funciona correctamente"
   - ❌ "Error: [copiar log completo]"
   - ⚠️ "Funciona pero hay un problema: [descripción]"

### Formato de reporte de errores:

```markdown
## Error Encontrado

**Archivo**: app/services/auth_service.py
**Línea**: 45
**Acción**: Intenté registrar un usuario

**Error**:
```
Traceback (most recent call last):
  File "app/services/auth_service.py", line 45, in create_user
    db.add(user)
AttributeError: 'NoneType' object has no attribute 'add'
```

**Contexto adicional**:
- Estoy usando PostgreSQL local
- La base de datos está corriendo
- Las variables de entorno están configuradas
```

---

## 🎯 Próximos Pasos

1. **Revisar y aprobar este framework**
2. **Comenzar con Fase 1: Planning (Tech Lead)**
3. **Generar arquitectura del sistema**
4. **Crear estructura de carpetas**
5. **Definir stack tecnológico final**

---

**¿Apruebas este framework de roles?**

Si estás de acuerdo, comenzaré como **Tech Lead** para diseñar la arquitectura del MVP.
