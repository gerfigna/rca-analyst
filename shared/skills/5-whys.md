---
name: 5-whys
description: Técnica de los 5 Porqués para análisis en profundidad de causas raíz. Construye cadenas causales "¿Por qué?" hasta llegar a causas raíz accionables, clasificándolas como Técnicas (T) o de Proceso (P). Úsalo cuando necesites profundizar en las hipótesis de causas, o cuando el usuario mencione "5 porqués", "5 whys", "cadena causal", "análisis en profundidad", "causa raíz técnica", "causa raíz de proceso" en el contexto de RCA o resolución de problemas.
---

# 5 Porqués — Análisis en Profundidad

## Propósito

Construir cadenas causales desde una hipótesis hasta su causa raíz accionable. El número de "¿por qués?" varía (habitualmente entre 4 y 7); lo que importa es llegar a una causa que cumpla el criterio de parada.

**Input requerido:** hipótesis prioritarias del análisis Ishikawa (Paso 2.1).

---

## Construcción de la cadena causal

Para cada hipótesis prioritaria:

1. Toma la hipótesis como **Causa 1.0**
2. Pregunta: ¿Por qué ocurre? → Causa 1.1
3. Pregunta: ¿Por qué ocurre la Causa 1.1? → Causa 1.2
4. Continúa hasta cumplir el criterio de parada
5. La cadena puede ramificarse: una causa puede tener varias sub-causas (1.2.a, 1.2.b…), cada una con su propia sub-cadena

**Si falta información para completar un nivel → indica el gap y pregunta antes de continuar.**

---

## Criterio de parada

Para cuando la causa:
- Es **accionable** (se puede actuar concretamente sobre ella) **y** su eliminación resuelve o reduce significativamente el problema — es una causa raíz
- Está fuera del control del equipo o la empresa (ley física, regulación externa irreversible)
- Si llevas más de 7 niveles sin encontrar una causa accionable, reconsidera si la hipótesis inicial era válida

**No pares si:**
- La causa raíz encontrada es Técnica (T) — continúa al menos un nivel más para encontrar la causa de Proceso (P) que la originó
- La causa es vaga ("error humano", "falta de control") — profundiza más

---

## Clasificación de Causas Raíz: T vs P

Cada cadena debe producir al menos una causa raíz de cada tipo:

**Causa Raíz Técnica (T)**
- Problema físico, técnico o de ingeniería (desgaste, parámetro fuera de especificación, defecto en material, instrucción ambigua, error en manipulación…)
- Su eliminación resuelve o reduce el problema significativamente
- Aparece antes en la cadena (más cerca del síntoma)

**Causa Raíz de Proceso (P)** *(también llamada Causa Sistémica)*
- Relacionada con el sistema de trabajo, gestión, diseño del proceso o procedimiento (plan de mantenimiento impreciso, procedimientos no actualizados, formación irregular…)
- Explica por qué existe la Causa Raíz Técnica
- Aparece después en la cadena (más alejada del síntoma)
- Podría generar otros problemas similares en el futuro

**Regla clave:** cuando encuentres una CRT, continúa la cadena para identificar la CRP correspondiente. Ambas son causas raíz y deben registrarse.

---

## Reglas de calidad

- Aplica los mismos criterios de calidad de hipótesis definidos en `ishikawa.md`: específicas, comprobables, con relación causa-efecto plausible, sin generalidades ni justificaciones disfrazadas
- **Nunca aceptar "error humano" como causa raíz final** — profundiza: ¿desconocimiento del procedimiento? ¿instrucciones ambiguas? ¿presión de tiempo? ¿falta de supervisión?

---

## Formato de salida

```
## 2.2 ANÁLISIS 5 PORQUÉS

### Cadena Causal 1: [Nombre de la hipótesis]

| Nivel | Causa | ¿Por qué ocurre? |
|-------|-------|-----------------|
| Causa 1.0 | [Hipótesis inicial] | Porque... |
| Causa 1.1 | [Causa más profunda] | Porque... |
| Causa 1.2 | [Causa más profunda] | Porque... |
| Causa 1.3 | [Causa raíz técnica] ← CRT | — |
| Causa 1.4 | [Causa raíz de proceso] ← CRP | — |

**CRT:** descripción clara y específica
**CRP:** descripción clara y específica

---

### Cadena Causal 2: [Nombre de la segunda hipótesis]
[Mismo formato]

---

## 2.3 RESUMEN DE CAUSAS RAÍZ

| ID | Causa Raíz | Tipo | Cadena |
|----|-----------|------|--------|
| CR-1 | descripción | T | Cadena 1 |
| CR-2 | descripción | P | Cadena 1 |
| CR-3 | descripción | T | Cadena 2 |
| CR-4 | descripción | P | Cadena 2 |
```
