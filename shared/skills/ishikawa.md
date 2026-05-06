---
name: ishikawa
description: Diagrama de Ishikawa (Espina de pescado) para generación de hipótesis de causas raíz. Úsalo cuando necesites generar hipótesis de causas organizadas por categorías (Materiales, Máquinas, Personas, Mediciones, Entorno, Métodos), o cuando el usuario mencione "Ishikawa", "espina de pescado", "fishbone", "hipótesis de causas", "brainstorming de causas" en el contexto de resolución de problemas o RCA.
---

# Ishikawa — Hipótesis de Causas

## Propósito

Generar hipótesis de causas potenciales organizadas en 6 categorías estándar, evitando que el análisis se enfoque solo en las causas más obvias. Cada hipótesis será el punto de partida para el análisis de 5 Porqués.

**Input requerido antes de empezar:** Enunciado del Problema (Paso 1.2) + Análisis KT completo (Paso 1.1).

---

## Las 6 Categorías

Para cada categoría, genera 2–5 hipótesis usando las preguntas guía y la información del análisis KT.

**1. Materiales** — materias primas, componentes, insumos, proveedores
> ¿Podría haber variaciones, defectos o cambios en el material/componente que originen el problema?

**2. Máquinas / Herramientas** — equipos, herramientas, software, tecnología
> ¿Podría haber desgaste, mal ajuste, fallo o cambio en máquinas/herramientas que origine el problema?

**3. Personas** — operarios, supervisores, turnos, formación, comunicación
> ¿Podría haber variabilidad en tareas humanas, cambio de personas o errores humanos que originen o contribuyan al problema?

**4. Mediciones** — sistemas de medición, calibración, definición de KPIs, recolección de datos
> ¿Podría el sistema de medición estar generando datos incorrectos o inconsistentes?

**5. Entorno / Políticas** — condiciones ambientales, regulaciones, cultura organizacional, políticas
> ¿Podría haber condiciones específicas de entorno (temperatura, humedad, etc.), políticas o normativas que originen o contribuyan al problema?

**6. Métodos / Procedimientos** — procesos, instrucciones, secuencias, estándares
> ¿Podría haber deficiencias, ambigüedad o incumplimiento en métodos y procedimientos que originen el problema?

---

## Proceso de generación

1. **Ancla el efecto** con el Enunciado del Problema (Paso 1.2)
2. Para cada categoría, aplica las preguntas guía al contexto específico del problema
3. **Prioriza las DIFERENCIAS O CAMBIOS del análisis KT** como punto de partida: son las pistas más valiosas
4. Usa la columna ES del KT como fuente adicional de hipótesis probables
5. Usa la columna NO ES del KT para **descartar hipótesis** que no sean consistentes con esa información (si la hipótesis contradice el NO ES, tiene "coartada" y se descarta)

---

## Criterios de calidad para las hipótesis

Las hipótesis deben ser:
- **Específicas**: no "fallo del operario" → sí "operario no aplica el paso 3 del procedimiento X"
- **Comprobables**: deben poder validarse con datos o investigación
- **Con relación causa-efecto plausible**: basadas en el conocimiento del proceso y la tecnología

Evitar:
- Generalidades: "falla la comunicación en la empresa" (¿qué tipo, entre quiénes, cuándo?)
- Justificaciones disfrazadas: "los clientes son muy exigentes", "la tecnología es compleja"
- Causas expresadas como falta de solución: en lugar de "falta formación" → "el operario desconoce el procedimiento X"; en lugar de "falta automatizar" → "el proceso es muy manual y propenso a error"

---

## Selección de hipótesis prioritarias

Al terminar de generar, selecciona las **3–6 más probables** considerando:
- Relación directa y clara con el problema
- Respaldo en datos o evidencia del análisis KT
- Conocimiento experto del proceso y la tecnología

Estas son las que se analizarán con 5 Porqués.

---

## Formato de salida

```
## 2.1 ANÁLISIS ISHIKAWA — HIPÓTESIS DE CAUSAS

**Problema analizado:** [Enunciado del Problema]

### Materiales
- [M1]: descripción específica

### Máquinas / Herramientas
- [Mq1]: descripción específica

### Personas
- [P1]: descripción específica

### Mediciones
- [Me1]: descripción específica

### Entorno / Políticas
- [E1]: descripción específica

### Métodos / Procedimientos
- [Mo1]: descripción específica

---

### Hipótesis prioritarias para 5 Porqués
1. [Hipótesis] — Razón: [por qué es prioritaria]
2. [Hipótesis] — Razón: [por qué es prioritaria]
3. [Hipótesis] — Razón: [por qué es prioritaria]
```

Si una categoría no aplica, indícalo brevemente en lugar de forzar hipótesis.
