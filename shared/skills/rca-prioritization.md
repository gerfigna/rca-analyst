---
name: rca-prioritization
description: Matriz de priorización de causas raíz por Impacto vs Esfuerzo/Complejidad. Clasifica las causas raíz identificadas en Técnicas (T) y de Proceso (P) y las ubica en una matriz para guiar la acción. Úsalo cuando necesites priorizar causas raíz, o cuando el usuario mencione "priorización", "matriz impacto-esfuerzo", "qué atacar primero", "plan de acción" en el contexto de un análisis de causa raíz o RCA.
---

# Priorización de Causas Raíz — Impacto × Esfuerzo

## Propósito

Priorizar el esfuerzo de validación y acción sobre las causas raíz identificadas. Trabaja solo con causas raíz (T y P del Paso 2.3) — no con síntomas ni causas intermedias.

---

## Evaluación en dos dimensiones

**IMPACTO** — Si se elimina esta causa, ¿cuánto se resuelve el problema?
- **Alto**: elimina o reduce el problema drásticamente (>70%)
- **Medio**: reducción moderada (40–70%)
- **Bajo**: efecto pequeño (<40%)

**ESFUERZO / COMPLEJIDAD** — ¿Qué requiere eliminar esta causa?
- **Bajo/Moderado**: complejidad y recursos moderados, tiempo corto (días o semanas)
- **Alto**: inversión importante, recursos difíciles de obtener, cambios organizacionales o tiempo largo (meses)

Si el usuario no proporciona información sobre esfuerzo → indica los supuestos usados y pide confirmación.

---

## Matriz de priorización

```
                        | ALTO IMPACTO | MEDIO IMPACTO | BAJO IMPACTO
BAJO/MODERADO ESFUERZO  |  PRIORIDAD 1 |  PRIORIDAD 2  |  PRIORIDAD 3
ALTO ESFUERZO           |  PRIORIDAD 2 |  PRIORIDAD 3  |  NO ATACAR
```

- **P1 (Quick Wins)**: atacar primero — alto impacto con poco esfuerzo
- **P2**: planificar — alto impacto/alto esfuerzo, o medio impacto/bajo esfuerzo
- **P3**: evaluar si vale la pena a largo plazo
- **No atacar**: bajo impacto + alto esfuerzo → descartar o diferir

---

## Validación con datos (Paso 2.5)

Si hay datos disponibles, indica el estado de cada causa raíz:

- **Validada**: la relación causa-efecto está confirmada con datos
- **Descartada**: los datos refutan la hipótesis
- **Hipótesis**: pendiente de validación con más datos, ensayos o investigación

Las causas Validadas tienen prioridad sobre las Hipótesis al mismo nivel de impacto/esfuerzo. Incluye en el plan de acción cómo validar las hipótesis pendientes.

---

## Formato de salida

```
## 2.4 PRIORIZACIÓN DE CAUSAS RAÍZ

| ID   | Causa Raíz | Tipo | Impacto | Esfuerzo | Prioridad | Estado |
|------|-----------|------|---------|----------|-----------|--------|
| CR-1 | texto     | T    | Alto    | Bajo     | 1         | Validada |
| CR-2 | texto     | P    | Alto    | Alto     | 2         | Hipótesis |
| CR-3 | texto     | T    | Medio   | Bajo     | 2         | Hipótesis |
| CR-4 | texto     | P    | Bajo    | Alto     | No atacar | Hipótesis |

### Matriz visual
|                        | ALTO IMPACTO | MEDIO IMPACTO | BAJO IMPACTO |
|------------------------|-------------|--------------|-------------|
| BAJO/MODERADO ESFUERZO | CR-1        | CR-3         |             |
| ALTO ESFUERZO          | CR-2        |              | CR-4        |

---

## 2.5 VALIDACIÓN CON DATOS (si aplica)

| ID   | Estado    | Evidencia disponible | Confianza |
|------|-----------|---------------------|-----------|
| CR-1 | Validada  | descripción de datos | Alto |
| CR-2 | Hipótesis | Sin datos            | Bajo |

**Gaps de información:** [qué datos harían falta para confirmar las hipótesis pendientes]

---

## Plan de Acción

### Prioridad 1 — Atacar inmediatamente
1. [CR-X]: acción concreta propuesta

### Prioridad 2 — Planificar a corto-medio plazo
2. [CR-X]: acción concreta propuesta

### Prioridad 3 — Evaluar / Diferir
3. [CR-X]: decisión razonada
```
