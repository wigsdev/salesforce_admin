# 📐 Development Rules - Salesforce Admin Platform

**Proyecto**: Salesforce Admin Learning Platform  
**Versión**: 0.30.0  
**Última actualización**: 17 Enero 2026

---

## 🎯 Propósito

Este documento establece las reglas y estándares de desarrollo que TODO el equipo debe seguir para mantener la calidad, consistencia y mantenibilidad del código.

---

## 1. Principios Fundamentales

### 1.1 SOLID Principles
- **S**ingle Responsibility: Una clase/función = una responsabilidad
- **O**pen/Closed: Abierto a extensión, cerrado a modificación
- **L**iskov Substitution: Subclases deben ser sustituibles por sus clases base
- **I**nterface Segregation: Interfaces específicas mejor que una general
- **D**ependency Inversion: Depender de abstracciones, no de concreciones

### 1.2 DRY (Don't Repeat Yourself)
- No duplicar código
- Crear funciones/clases reutilizables
- Usar herencia y composición apropiadamente

### 1.3 KISS (Keep It Simple, Stupid)
- Soluciones simples sobre complejas
- Evitar over-engineering
- Código legible > código "clever"

---

## 2. Estándares de Código Python

### 2.1 Style Guide
- **Seguir PEP 8** estrictamente
- **Usar Black** para formateo automático (line length: 88)
- **Usar isort** para ordenar imports
- **Usar flake8** para linting

### 2.2 Type Hints
```python
# ✅ CORRECTO
def calculate_progress(user_id: int, sprint_id: int) -> float:
    pass

# ❌ INCORRECTO
def calculate_progress(user_id, sprint_id):
    pass
```

### 2.3 Docstrings
```python
# ✅ CORRECTO (Google Style)
def create_user(name: str, email: str, password: str) -> User:
    """
    Crea un nuevo usuario en el sistema.
    
    Args:
        name: Nombre completo del usuario
        email: Email único del usuario
        password: Contraseña en texto plano (será hasheada)
        
    Returns:
        User: Instancia del usuario creado
        
    Raises:
        ValueError: Si el email ya existe
        ValidationError: Si el password es débil
    """
    pass
```

### 2.4 Naming Conventions
```python
# Classes: PascalCase
class UserService:
    pass

# Functions/Methods: snake_case
def get_user_by_id():
    pass

# Variables: snake_case
user_count = 10

# Constants: UPPER_SNAKE_CASE
MAX_LOGIN_ATTEMPTS = 5

# Private: _leading_underscore
def _internal_helper():
    pass
```

---

## 3. Estructura de Archivos

### 3.1 Organización de Módulos
```python
# ✅ CORRECTO
from app.models.user import User
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate

# ❌ INCORRECTO
from app.models import *
from app.services import auth_service
```

### 3.2 Imports Ordenados (isort)
```python
# 1. Standard library
import os
from typing import List, Optional

# 2. Third-party
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# 3. Local application
from app.models.user import User
from app.services.auth_service import AuthService
```

---

## 4. Base de Datos

### 4.1 Migraciones (Alembic)
- **NUNCA** modificar la DB manualmente
- **SIEMPRE** crear migrations para cambios de schema
- **Nombrar** migrations descriptivamente: `add_user_role_column`
- **Revisar** migrations antes de aplicar

```bash
# Crear migration
alembic revision --autogenerate -m "add_user_role_column"

# Aplicar migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

### 4.2 Queries
```python
# ✅ CORRECTO (usar ORM)
user = db.query(User).filter(User.email == email).first()

# ❌ INCORRECTO (raw SQL solo si es necesario)
db.execute("SELECT * FROM users WHERE email = ?", email)
```

### 4.3 Transacciones
```python
# ✅ CORRECTO
try:
    db.add(user)
    db.add(progress)
    db.commit()
except Exception as e:
    db.rollback()
    raise
```

---

## 5. Testing

### 5.1 Coverage Mínimo
- **Unit tests**: 80% coverage
- **Integration tests**: Features críticas
- **E2E tests**: User flows principales

### 5.2 Naming Conventions
```python
# ✅ CORRECTO
def test_create_user_with_valid_data_succeeds():
    pass

def test_create_user_with_duplicate_email_raises_error():
    pass

# ❌ INCORRECTO
def test_user():
    pass
```

### 5.3 Estructura de Tests
```python
# Arrange-Act-Assert (AAA)
def test_calculate_progress():
    # Arrange
    user = create_test_user()
    tasks = create_test_tasks(count=10)
    
    # Act
    progress = calculate_progress(user.id)
    
    # Assert
    assert progress == 0.0
```

### 5.4 Fixtures
```python
# conftest.py
@pytest.fixture
def test_db():
    """Crea una DB de prueba limpia"""
    db = create_test_database()
    yield db
    db.drop_all()
```

---

## 6. Git Workflow

### 6.1 Branching Strategy
```
main (production)
  ↑
develop (staging)
  ↑
feature/add-markdown-renderer
feature/implement-auth
hotfix/fix-login-error
```

### 6.2 Commit Messages (Conventional Commits)
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: Nueva feature
- `fix`: Bug fix
- `docs`: Cambios en documentación
- `style`: Formateo, sin cambios de código
- `refactor`: Refactorización
- `test`: Agregar/modificar tests
- `chore`: Mantenimiento (deps, config)

**Ejemplos:**
```
feat(auth): add JWT token refresh endpoint

Implementa endpoint para refrescar tokens expirados.
Tokens tienen TTL de 7 días.

Closes #123

---

fix(markdown): correct relative link resolution

Links relativos ahora se resuelven correctamente
cuando el documento está en subdirectorios profundos.

Fixes #456
```

### 6.3 Pull Requests
- **Título**: Descriptivo y claro
- **Descripción**: Qué, por qué, cómo
- **Tests**: Incluir tests para nuevas features
- **Review**: Mínimo 1 aprobación antes de merge
- **CI/CD**: Debe pasar antes de merge

---

## 7. Seguridad

### 7.1 Contraseñas
```python
# ✅ CORRECTO
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash(password)

# ❌ INCORRECTO
import hashlib
hashed = hashlib.md5(password.encode()).hexdigest()
```

### 7.2 SQL Injection
```python
# ✅ CORRECTO (ORM)
user = db.query(User).filter(User.email == email).first()

# ❌ INCORRECTO
query = f"SELECT * FROM users WHERE email = '{email}'"
```

### 7.3 XSS Prevention
```python
# ✅ CORRECTO (Jinja2 auto-escapes)
{{ user.name }}

# ❌ INCORRECTO
{{ user.name | safe }}  # Solo si confías en la fuente
```

### 7.4 Secrets
```python
# ✅ CORRECTO
from app.config import settings
SECRET_KEY = settings.SECRET_KEY

# ❌ INCORRECTO
SECRET_KEY = "hardcoded-secret-123"
```

---

## 8. Performance

### 8.1 Database Queries
```python
# ✅ CORRECTO (eager loading)
users = db.query(User).options(joinedload(User.progress)).all()

# ❌ INCORRECTO (N+1 problem)
users = db.query(User).all()
for user in users:
    progress = user.progress  # Lazy load
```

### 8.2 Caching
```python
# Para v0.40.0 (Redis)
@cache(ttl=300)
def get_team_progress():
    pass
```

---

## 9. Logging

### 9.1 Niveles de Log
```python
import logging

logger = logging.getLogger(__name__)

# DEBUG: Información detallada para debugging
logger.debug(f"User {user_id} attempting login")

# INFO: Eventos normales
logger.info(f"User {user_id} logged in successfully")

# WARNING: Algo inesperado pero no crítico
logger.warning(f"User {user_id} failed login attempt {attempt}/5")

# ERROR: Error que impide una operación
logger.error(f"Failed to send email to {email}: {error}")

# CRITICAL: Error grave que puede detener la app
logger.critical(f"Database connection lost")
```

### 9.2 Structured Logging
```python
# ✅ CORRECTO (JSON)
logger.info(
    "User login",
    extra={
        "user_id": user.id,
        "email": user.email,
        "ip": request.client.host
    }
)
```

---

## 10. Code Review Checklist

### 10.1 Antes de Crear PR
- [ ] Código sigue PEP 8
- [ ] Type hints agregados
- [ ] Docstrings completos
- [ ] Tests agregados/actualizados
- [ ] Tests pasan localmente
- [ ] No hay print() statements
- [ ] No hay código comentado
- [ ] Variables tienen nombres descriptivos

### 10.2 Durante Code Review
- [ ] Lógica es clara y correcta
- [ ] No hay código duplicado
- [ ] Manejo de errores apropiado
- [ ] Queries de DB son eficientes
- [ ] Seguridad considerada
- [ ] Performance considerada

---

## 11. Deployment

### 11.1 Pre-Deploy Checklist
- [ ] Todos los tests pasan
- [ ] Coverage > 75%
- [ ] Migrations probadas
- [ ] Variables de entorno configuradas
- [ ] Logs funcionando
- [ ] Rollback plan definido

### 11.2 Post-Deploy
- [ ] Verificar health check
- [ ] Monitorear logs por 15 min
- [ ] Verificar métricas (response time, errors)
- [ ] Notificar al equipo

---

## 12. Documentación

### 12.1 Código
- Docstrings en todas las funciones públicas
- Comentarios para lógica compleja
- Type hints siempre

### 12.2 API
- Actualizar `docs/API.md` con nuevos endpoints
- Incluir ejemplos de request/response
- Documentar errores posibles

### 12.3 README
- Mantener actualizado
- Instrucciones de setup claras
- Troubleshooting común

---

## 13. Prohibiciones Absolutas

### ❌ NUNCA HACER:
1. Commit directo a `main`
2. Push de secrets/passwords
3. Modificar DB manualmente en producción
4. Usar `SELECT *` en queries
5. Ignorar errores silenciosamente (`except: pass`)
6. Hardcodear valores de configuración
7. Usar `eval()` o `exec()`
8. Desactivar CORS en producción
9. Hacer deploy sin tests
10. Ignorar warnings de seguridad

---

## 14. Herramientas Obligatorias

### 14.1 Pre-commit Hooks
```bash
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    hooks:
      - id: flake8
```

### 14.2 IDE Configuration
- **VSCode**: Usar settings.json del proyecto
- **PyCharm**: Configurar Black como formateador
- **Linter**: flake8 habilitado

---

## 15. Proceso de Onboarding

### Para Nuevos Developers:
1. Leer este documento completo
2. Setup del entorno local
3. Ejecutar tests
4. Hacer un PR de prueba (fix typo en docs)
5. Code review con mentor

---

**Estas reglas son OBLIGATORIAS. Cualquier PR que no las siga será rechazado.**

---

**Creado por**: Tech Lead - VISIONARY ADMINS  
**Aprobado por**: Equipo completo  
**Versión**: 1.0
