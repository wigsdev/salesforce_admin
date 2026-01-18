# DevOPS

## 📋 Proyecto: Financiera Horizonte S.A.

**Última actualización**: [Fecha]

---

## 🎯 Objetivo

Documentar los pasos, procesos y herramientas de DevOPS para automatizar y optimizar el ciclo de desarrollo, testing y deployment de Salesforce.

---

## 🔄 Flujo de Trabajo DevOPS

### Pipeline Actual

```
DEV → QA → PROD
```

**Descripción**:
1. **Desarrollo en DEV**: Crear/modificar configuraciones
2. **Testing en QA**: Validar funcionalidades
3. **Deployment a PROD**: Liberar a producción

---

## 🛠️ Herramientas Utilizadas

### Herramientas Actuales (Sprint 1)

| Herramienta | Propósito | Estado |
|-------------|-----------|--------|
| Change Sets | Deployment manual | ✅ En uso |
| Data Loader | Migración de datos | ✅ En uso |
| Trello | Gestión de tareas | ✅ En uso |
| Google Docs | Documentación | ✅ En uso |

---

### Herramientas Recomendadas (Futuro)

| Herramienta | Propósito | Prioridad |
|-------------|-----------|-----------|
| Salesforce CLI (SFDX) | Deployment automatizado | Alta |
| Git/GitHub | Control de versiones | Alta |
| VS Code + Salesforce Extensions | IDE moderno | Media |
| Jenkins/GitHub Actions | CI/CD | Media |
| Copado/Gearset | DevOPS platform | Baja |

---

## 📝 Proceso de Deployment

### Método Actual: Change Sets

#### Ventajas
- ✅ Interfaz gráfica (fácil de usar)
- ✅ No requiere instalación
- ✅ Validación antes de deploy

#### Desventajas
- ⚠️ Manual (no automatizable)
- ⚠️ No versionable en Git
- ⚠️ Difícil de revertir

---

### Pasos Detallados

#### 1. Crear Change Set en DEV/QA

```
Setup → Environments → Outbound Change Sets → New
```

**Nombre sugerido**: `Sprint[X]_[YYYYMMDD]_[Descripción]`

**Ejemplo**: `Sprint1_20260130_BankAccounts`

**Componentes a incluir**:
- Custom Objects
- Custom Fields
- Flows
- Validation Rules
- Page Layouts
- Permission Sets
- Reports
- Dashboards

---

#### 2. Upload Change Set

```
Change Set → Upload → Select Target Org (QA o PROD)
```

**Tiempo estimado**: 5-10 minutos

---

#### 3. Deploy en Ambiente Destino

```
Setup → Inbound Change Sets → [Nombre del Change Set]
```

**Opciones de Deployment**:
- ✅ **Validate Only**: Probar sin deployar (recomendado primero)
- ✅ **Run All Tests**: Si hay Apex code
- ✅ **Rollback on Error**: Revertir si falla

**Tiempo estimado**: 10-30 minutos (depende del tamaño)

---

## 🚀 Migración a SFDX (Recomendado para Sprint 2+)

### ¿Por qué SFDX?

- ✅ Versionable en Git
- ✅ Automatizable (CI/CD)
- ✅ Fácil de revertir (git revert)
- ✅ Trabajo en equipo mejorado
- ✅ Deployment más rápido

---

### Instalación de SFDX

#### Paso 1: Instalar Salesforce CLI

**Windows**:
```bash
# Descargar desde:
https://developer.salesforce.com/tools/sfdxcli
```

**Mac**:
```bash
brew install sfdx
```

**Linux**:
```bash
wget https://developer.salesforce.com/media/salesforce-cli/sfdx/channels/stable/sfdx-linux-x64.tar.xz
tar xJf sfdx-linux-x64.tar.xz -C ~/sfdx --strip-components 1
```

---

#### Paso 2: Verificar Instalación

```bash
sfdx --version
# Output: sfdx-cli/7.x.x
```

---

#### Paso 3: Autenticar Orgs

```bash
# Autenticar DEV
sfdx auth:web:login -a dev-org

# Autenticar QA
sfdx auth:web:login -a qa-org

# Autenticar PROD
sfdx auth:web:login -a prod-org
```

---

### Comandos Básicos de SFDX

#### Retrieve (Descargar metadata)

```bash
# Retrieve specific metadata
sfdx force:source:retrieve -m CustomObject:Bank_Account__c -u dev-org

# Retrieve all metadata
sfdx force:source:retrieve -m CustomObject,CustomField,Flow -u dev-org
```

---

#### Deploy (Subir metadata)

```bash
# Validate only (dry run)
sfdx force:source:deploy -p force-app -u prod-org --checkonly

# Deploy for real
sfdx force:source:deploy -p force-app -u prod-org
```

---

#### Open Org

```bash
# Open DEV org in browser
sfdx force:org:open -u dev-org

# Open PROD org
sfdx force:org:open -u prod-org
```

---

## 🔀 Control de Versiones con Git

### Estructura de Repositorio Sugerida

```
admin_salesforce/
├── force-app/
│   └── main/
│       └── default/
│           ├── objects/
│           │   └── Bank_Account__c/
│           ├── flows/
│           ├── layouts/
│           └── permissionsets/
├── docs/
├── .gitignore
├── sfdx-project.json
└── README.md
```

---

### Comandos Git Básicos

```bash
# Initialize repo
git init

# Add files
git add .

# Commit
git commit -m "Sprint 1: Bank Accounts feature"

# Push to GitHub
git push origin main

# Create branch for new feature
git checkout -b feature/sprint2-notifications
```

---

## 🤖 CI/CD con GitHub Actions (Avanzado)

### Ejemplo de Workflow

Crear archivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to QA

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Install SFDX
        run: |
          wget https://developer.salesforce.com/media/salesforce-cli/sfdx/channels/stable/sfdx-linux-x64.tar.xz
          tar xJf sfdx-linux-x64.tar.xz -C ~/sfdx --strip-components 1
          echo "$HOME/sfdx/bin" >> $GITHUB_PATH
      
      - name: Authenticate QA
        run: |
          echo ${{ secrets.SFDX_AUTH_URL }} > auth.txt
          sfdx auth:sfdxurl:store -f auth.txt -a qa-org
      
      - name: Deploy to QA
        run: sfdx force:source:deploy -p force-app -u qa-org
```

---

## 📊 Métricas de DevOPS

### Métricas a Trackear

| Métrica | Objetivo | Actual |
|---------|----------|--------|
| Deployment Frequency | 1 por sprint | [A completar] |
| Lead Time (DEV → PROD) | < 1 semana | [A completar] |
| Change Failure Rate | < 10% | [A completar] |
| Mean Time to Recovery | < 1 hora | [A completar] |

---

## 📝 Checklist de DevOPS

### Pre-Deployment

- [ ] Código/configuración en DEV
- [ ] Testing en QA completado
- [ ] Aprobación de Product Owner
- [ ] Backup de PROD realizado
- [ ] Change Set/Package preparado
- [ ] Usuarios notificados

### Durante Deployment

- [ ] Validar antes de deployar
- [ ] Monitorear deployment status
- [ ] Ejecutar smoke tests
- [ ] Verificar logs de errores

### Post-Deployment

- [ ] Verificar funcionalidades en PROD
- [ ] Notificar a usuarios
- [ ] Documentar deployment
- [ ] Actualizar versión
- [ ] Monitorear por 24-48 horas

---

## 🐛 Troubleshooting

### Problemas Comunes

#### Error: "Component already exists"

**Solución**:
- Verificar que el componente no existe en destino
- Usar "Update" en lugar de "Create"

#### Error: "Missing dependencies"

**Solución**:
- Agregar componentes dependientes al Change Set
- Orden correcto: Fields → Validation Rules → Flows

#### Error: "Tests failed"

**Solución**:
- Revisar Apex tests
- Corregir tests en DEV
- Re-deployar

---

## 📚 Recursos de Aprendizaje

### Trailhead Modules

- [Salesforce DX](https://trailhead.salesforce.com/content/learn/trails/sfdx_get_started)
- [Application Lifecycle Management](https://trailhead.salesforce.com/content/learn/modules/application-lifecycle-and-development-models)
- [Change Sets](https://trailhead.salesforce.com/content/learn/modules/declarative-change-set-development)

### Documentación Oficial

- [SFDX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/)
- [Change Sets Guide](https://help.salesforce.com/s/articleView?id=sf.changesets.htm)
- [Deployment Best Practices](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/)

---

## 🔄 Roadmap de DevOPS

### Sprint 1 (Actual)
- ✅ Change Sets manuales
- ✅ Documentación básica

### Sprint 2-3 (Próximo)
- [ ] Implementar SFDX
- [ ] Configurar Git/GitHub
- [ ] Automatizar backups

### Sprint 4+ (Futuro)
- [ ] CI/CD con GitHub Actions
- [ ] Automated testing
- [ ] Monitoring y alertas

---

**Última actualización**: [Fecha]  
**Responsable DevOPS**: [Nombre]  
**Próxima revisión**: [Fecha]
