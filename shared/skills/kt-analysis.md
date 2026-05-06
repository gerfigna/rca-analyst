---
name: kt-analysis
description: Análisis de Problemas Kepner-Tregoe (KT) — construye la matriz IS/IS NOT (ES/NO ES) para describir con precisión un problema. Úsalo cuando necesites estructurar la descripción de un problema en las dimensiones QUÉ, DÓNDE, CUÁNDO y CUÁNTO, identificar diferencias y cambios relevantes, o cuando el usuario mencione "Kepner-Tregoe", "análisis IS/IS NOT", "matriz ES/NO ES", "descripción del problema" en el contexto de RCA o resolución de problemas.
---

# Kepner-Tregoe — Matriz ES / NO ES

## Propósito

Describir el problema con precisión forzando la comparación entre LO QUE OCURRE y LO QUE NO OCURRE. Las diferencias entre ambas columnas revelan las pistas más valiosas para las hipótesis de causas.

---

## Verificación previa

Antes de construir la matriz, confirma que tienes:
- El objeto, componente o KPI afectado
- La desviación (diferencia entre comportamiento actual y esperado)
- Alguna información sobre dónde ocurre, cuándo y cuánto

Si falta información relevante → pregunta antes de continuar.

---

## Las 4 dimensiones

Para cada dimensión completa las columnas ES | NO ES | DIFERENCIAS O CAMBIOS.

**QUÉ**
- ¿Qué objeto/componente/KPI presenta el problema?
- ¿Cuál es exactamente la desviación (comportamiento actual vs. esperado)?
- ¿Qué otros objetos similares NO presentan el problema?

**DÓNDE**
- ¿En qué proceso, estación, máquina o área ocurre?
- ¿En qué parte física de la pieza/sistema ocurre el defecto?
- ¿Dónde podría ocurrir pero sabemos que NO ocurre?

**CUÁNDO**
- ¿Cuándo se observó por primera vez?
- ¿Con qué frecuencia o patrón ocurre?
- ¿En qué momentos NO ocurre?

**CUÁNTO**
- ¿Cuántas unidades, lotes o % están afectados?
- ¿Cuál es el impacto en coste, cliente o proceso?
- ¿Cuánto podría estar afectado pero sabemos que NO lo está?

---

## Columna DIFERENCIAS O CAMBIOS

Es la columna más importante. Para cada dimensión, compara ES vs NO ES y anota:
- **Diferencias**: qué es distinto entre lo que ES y lo que NO ES (ej. proveedor diferente, turno diferente, versión diferente)
- **Cambios**: qué cambió en el tiempo relacionado con la aparición del problema (ej. cambio de material, cambio de especificación, cambio de operario)

**Reglas estrictas:**
- Solo hechos y datos constatados — nunca suposiciones ni hipótesis
- Si no hay dato → escribe "Sin dato" (no dejes vacío ni inventes)
- No incluir posibles causas raíz (eso va en Ishikawa)

---

## Enunciado del Problema (Paso 1.2)

Al finalizar la matriz, construye una frase específica que contenga:
- El objeto/KPI concreto con el problema
- La desviación observada (comportamiento actual vs. esperado)

Formato orientativo:
> *"El [objeto/KPI] presenta [comportamiento actual] cuando debería [comportamiento esperado]."*

El enunciado debe ser:
- Específico y medible (incluir cifras cuando sea posible)
- Sin mencionar posibles causas ni soluciones
- De interpretación única

---

## Formato de salida

```
## 1.1 ANÁLISIS KT (ES / NO ES)

### QUÉ
| ES | NO ES | DIFERENCIAS O CAMBIOS |
|----|-------|-----------------------|
|    |       |                       |

### DÓNDE
| ES | NO ES | DIFERENCIAS O CAMBIOS |
|----|-------|-----------------------|
|    |       |                       |

### CUÁNDO
| ES | NO ES | DIFERENCIAS O CAMBIOS |
|----|-------|-----------------------|
|    |       |                       |

### CUÁNTO
| ES | NO ES | DIFERENCIAS O CAMBIOS |
|----|-------|-----------------------|
|    |       |                       |

## 1.2 ENUNCIADO DEL PROBLEMA
[Frase específica y medible]
```
