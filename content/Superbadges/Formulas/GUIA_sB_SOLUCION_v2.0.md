# Solución: Superbadge Fórmulas

## Reto 1: Lead Score y Lead Rating

### Campo: Lead Score

**Setup → Object Manager → Lead → Fields & Relationships → New**

- Data Type: **Formula**
- Return Type: **Number**, Decimal Places: **0**
- Field Label: `Lead Score`
- Field Name: `Lead_Score`

**Fórmula**:
```javascript
IF(
  ISPICKVAL(Status, 'Closed - Not Converted'),
  0,
  IF(DoNotCall, -25, 0) +
  IF(NOT(ISBLANK(Email)), 15, 0) +
  CASE(
    TEXT(LeadSource),
    'Web', 20,
    'Phone Inquiry', 35,
    'Partner Referral', 25,
    'Purchased List', 10,
    0
  )
)
```

- Description: `Calculates lead score based on status, contact preferences, email presence, and lead source`
- Help Text: `Automated lead scoring to help prioritize sales efforts. Higher scores indicate better qualified leads.`
- Field-Level Security: Visible solo para **Sales Representative**

---

### Campo: Lead Rating

**Setup → Object Manager → Lead → Fields & Relationships → New**

- Data Type: **Formula**
- Return Type: **Text**
- Field Label: `Lead Rating`
- Field Name: `Lead_Rating`

**Fórmula**:
```javascript
IMAGE(
  CASE(
    TRUE,
    Lead_Score__c < 10, '/img/samples/stars_000.gif',
    Lead_Score__c < 20, '/img/samples/stars_100.gif',
    Lead_Score__c < 30, '/img/samples/stars_200.gif',
    Lead_Score__c < 40, '/img/samples/stars_300.gif',
    Lead_Score__c < 50, '/img/samples/stars_400.gif',
    '/img/samples/stars_500.gif'
  ),
  CASE(
    TRUE,
    Lead_Score__c < 10, '0 Star',
    Lead_Score__c < 20, '1 Star',
    Lead_Score__c < 30, '2 Star',
    Lead_Score__c < 40, '3 Star',
    Lead_Score__c < 50, '4 Star',
    '5 Star'
  )
)
```

- Description: `Visual star rating based on Lead Score for quick lead qualification`
- Help Text: `Star rating provides a quick visual indicator of lead quality. More stars = higher priority.`
- Field-Level Security: Visible solo para **Sales Representative**

---

## Reto 2: Opportunity Value y Severity (Number)

### Campo: Opportunity Value

**Setup → Object Manager → Asset → Fields & Relationships → New**

- Data Type: **Formula**
- Return Type: **Currency**, Decimal Places: **2**
- Field Label: `Opportunity Value`
- Field Name: `Opportunity_Value`

**Fórmula**:
```javascript
Opportunity.Amount
```

- Description: `Displays the amount from the related opportunity record for decision-making purposes`
- Help Text: `Shows the value of the opportunity that generated this asset. Used for service-level agreement decisions.`
- Field-Level Security: Visible solo para **Service Agent**
- Page Layout: Agregar al Asset Page Layout

---

### Campo: Severity (Number)

**Setup → Object Manager → Case → Fields & Relationships → New**

- Data Type: **Formula**
- Return Type: **Number**, Decimal Places: **0**
- Field Label: `Severity (Number)`
- Field Name: `Severity_Number`

**Fórmula**:
```javascript
VALUE(TEXT(Severity))
```

- Description: `Numeric representation of Case Severity for reporting and calculations`
- Help Text: `Converts severity picklist to number for KPI tracking. Lower numbers = higher severity.`
- Field-Level Security: Visible solo para **Service Agent**

---

### Modificar Reporte

**Reports → "Case Severity by Month Last Year" → Edit**

1. Agregar columna **Severity (Number)**
2. Click dropdown → **Summarize** → **Average**
3. Verificar agrupación por **Account Name**
4. **Save**

---

## Reto 3: Close Month

### Fórmula de Reporte

**Reports → "Case Severity by Month Last Year" → Edit**

1. Click **Add Column** → **Add Row-Level Formula**
2. Column Name: `Close Month`
3. Format: **Text**

**Fórmula**:
```javascript
IF(
  MONTH(ClosedDate) < 10,
  '0' & TEXT(MONTH(ClosedDate)),
  TEXT(MONTH(ClosedDate))
) & ' - ' &
CASE(
  MONTH(ClosedDate),
  1, 'January',
  2, 'February',
  3, 'March',
  4, 'April',
  5, 'May',
  6, 'June',
  7, 'July',
  8, 'August',
  9, 'September',
  10, 'October',
  11, 'November',
  12, 'December',
  ''
)
```

4. Click **Apply**
5. Arrastrar **Close Month** a Grouping
6. Configurar orden ascendente
7. Verificar Average Severity (Number) por Account Name
8. **Save**

---

**Grupo**: 3 - VISIONARY ADMINS  
**Fecha**: 17 Enero 2026
