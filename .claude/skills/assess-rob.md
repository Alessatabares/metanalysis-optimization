---
name: assess-rob
description: Aplica herramienta de riesgo de sesgo apropiada según el diseño (ROB-2 para RCT, Newcastle-Ottawa para observacionales). Completa dominio por dominio con justificación y actualiza rob.csv.
---

# Skill: Risk of Bias Assessment

## Inputs

- DOI del paper
- Diseño (lo lee del frontmatter del paper o se pregunta)

## Workflow

1. **Determinar herramienta**:
   - RCT → **ROB-2** (Cochrane, 5 dominios)
   - Cohort/case-control → **Newcastle-Ottawa Scale (NOS)** o ROBINS-I si la pregunta es de intervención
   - Cross-sectional → AXIS o JBI checklist
   - Systematic review previa → AMSTAR-2

2. **Leer el paper completo** (no solo abstract).

3. **Para ROB-2 evaluar 5 dominios**:
   - D1: Bias arising from the randomization process
   - D2: Bias due to deviations from intended interventions
   - D3: Bias due to missing outcome data
   - D4: Bias in measurement of the outcome
   - D5: Bias in selection of the reported result
   - **Overall**: Low / Some concerns / High

4. **Para NOS evaluar (cohorte 8 estrellas máx, 9 case-control)**:
   - Selection (4 puntos)
   - Comparability (2 puntos)
   - Outcome/Exposure (3 puntos)

5. **Documentar en `extraccion/rob.csv`** con justificación específica por dominio.

6. **Actualizar frontmatter del paper** (`rob_overall: low/some_concerns/high`).

## Reglas

- **Cada juicio requiere cita textual** del paper (página/tabla).
- **No "default a low"** sin verificar — si el paper no reporta cegamiento, NO es low.
- **Some concerns ≠ ignorar**: documentar qué te concierne específicamente.
- **High risk no excluye** automáticamente — informa el análisis de sensibilidad.

## Output

- Fila en `rob.csv`
- Update del frontmatter del paper
- Si todos los papers están evaluados, generar tabla resumen para manuscrito
