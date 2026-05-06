---
name: rca-method
description: >
  Análisis de Causa Raíz (RCA) completo usando la metodología TFF (The Flow Factory):
  Análisis KT (Kepner-Tregoe / Matriz ES-NO ES), Ishikawa y 5 Porqués.
  Úsalo cuando el usuario quiera realizar un RCA, investigar la causa de un problema,
  analizar por qué un KPI no alcanzó su objetivo, investigar una desviación, fallo
  o incidente, o cuando mencione "RCA", "causa raíz", "por qué falló X",
  "qué causó el problema", "The Flow Factory", "TFF".
---

# RCA Method — Orquestador del Proceso Completo

## Flujo de pasos

```
PASO 1   → Definición del Problema          (este skill)
PASO 1.1 → Matriz ES / NO ES               → cargar: kt-analysis
PASO 1.2 → Enunciado del Problema          → cargar: kt-analysis
PASO 2.1 → Hipótesis de Causas (Ishikawa)  → cargar: ishikawa.md
PASO 2.2 → Cadenas 5 Porqués              → cargar: 5-whys
PASO 2.3 → Clasificación T / P            → cargar: 5-whys
PASO 2.4 → Priorización                   → cargar: rca-prioritization
PASO 2.5 → Validación con Datos           → cargar: rca-prioritization
```

Lee el skill indicado **antes** de ejecutar cada paso. No saltes pasos ni avances sin los datos mínimos requeridos.

---

## PASO 1 — Definición del Problema

Recopila del usuario estos cuatro campos mínimos antes de continuar:

| Campo | Descripción |
|-------|-------------|
| Objeto / KPI afectado | El elemento que presenta la desviación |
| Comportamiento actual | Lo que está ocurriendo |
| Comportamiento esperado | Lo que debería ocurrir |
| Síntoma observado | Cómo se manifiesta el problema |

**Si falta alguno de estos cuatro → pregunta antes de avanzar al Paso 1.1.**

Contexto adicional útil (recoge si está disponible, enriquece la matriz KT): dónde ocurre, cuándo empezó, frecuencia, volumen/impacto.

---

## PASO 1.1 — Matriz ES / NO ES
Carga `kt-analysis` y construye la matriz. La columna DIFERENCIAS O CAMBIOS alimenta directamente las hipótesis del Paso 2.1.

## PASO 1.2 — Enunciado del Problema
Carga `kt-analysis`. El enunciado debe ser específico, medible y sin mencionar causas ni soluciones.

## PASO 2.1 — Hipótesis de Causas
Carga `ishikawa`. Usa la información de los Pasos 1.1 y 1.2 para generar hipótesis. Selecciona las 3–6 más probables para los 5 Porqués.

## PASO 2.2 + 2.3 — Cadenas Causales y Clasificación T/P
Carga `5-whys`. Construye la cadena causal para cada hipótesis prioritaria hasta identificar causas raíz Técnicas (T) y de Proceso (P).

## PASO 2.4 + 2.5 — Priorización y Validación
Carga `rca-prioritization`. Construye la matriz Impacto × Esfuerzo y el plan de acción priorizado.

---

## Formato de salida final

```
## 1. DEFINICIÓN DEL PROBLEMA
Objeto/KPI | Comportamiento actual | Comportamiento esperado | Síntoma | Dónde | Cuándo | Cuánto

## 1.1 ANÁLISIS KT (ES / NO ES)
[Matrices: QUÉ | DÓNDE | CUÁNDO | CUÁNTO]

## 1.2 ENUNCIADO DEL PROBLEMA

## 2.1 ISHIKAWA — HIPÓTESIS DE CAUSAS

## 2.2 5 PORQUÉS — CADENAS CAUSALES

## 2.3 CLASIFICACIÓN T/P

## 2.4 PRIORIZACIÓN

## 2.5 VALIDACIÓN CON DATOS (si aplica)
```
