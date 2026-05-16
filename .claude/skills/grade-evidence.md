---
name: grade-evidence
description: Aplica GRADE (Grading of Recommendations Assessment, Development and Evaluation) a cada outcome del meta-análisis. Evalúa 5 dominios (risk of bias, inconsistency, indirectness, imprecision, publication bias) y genera tabla Summary of Findings (SoF) lista para manuscrito.
---

# Skill: GRADE Evidence Assessment

GRADE convierte tu evidencia en una calificación reproducible (High/Moderate/Low/Very Low) para cada outcome. Es el estándar para guidelines, Cochrane y revistas top.

## Inputs

- `extraccion/extraction.csv` (datos por outcome)
- `extraccion/rob.csv` (riesgo de sesgo por estudio)
- `analisis/results-<outcome>.md` (resultados meta-análisis: pooled effect, I², k, n)
- `analisis/funnel-<outcome>.png` (si k≥10)
- Diseño base de los estudios (de los frontmatter de `extraccion/papers/*.md`)

## Workflow

### Por cada outcome

1. **Punto de inicio**:
   - RCTs → **HIGH** (4 estrellas)
   - Estudios observacionales → **LOW** (2 estrellas)
   - Otros diseños → considerar caso por caso

2. **Aplicar 5 dominios de downgrade**:

   **Dominio 1: Risk of Bias**
   - Leer `rob.csv` para los estudios de este outcome.
   - Si la mayoría de estudios o los de mayor peso son "High" o "Some concerns" → bajar 1 nivel.
   - Si "Very serious" → bajar 2 niveles.
   - Documentar qué dominio del ROB falla más (allocation, blinding, attrition, etc.).

   **Dominio 2: Inconsistency (heterogeneidad)**
   - Leer I² del meta-análisis.
   - I² < 25% → no bajar
   - I² 25-50% → considerar bajar 1 si explicación clínica plausible
   - I² 50-75% → bajar 1 nivel
   - I² > 75% → bajar 2 niveles
   - Verificar también: ¿los efectos van en direcciones opuestas? ¿solapan los CI?

   **Dominio 3: Indirectness**
   - ¿Población estudiada coincide con la población de la pregunta? (e.g. estudios en adultos pero pregunta sobre niños = bajar)
   - ¿Intervención y comparador son los que importan?
   - ¿Outcomes son los del paciente o sustitutos? (e.g. HbA1c vs eventos cardiovasculares = sustituto)
   - 1 problema serio → bajar 1; 2+ problemas → bajar 2.

   **Dominio 4: Imprecision**
   - Tamaño de muestra total (n) y número de eventos.
   - Threshold OIS (Optimal Information Size): si n total < OIS calculado, bajar.
   - CI95% del pooled effect: si cruza el null o incluye efectos clínicamente irrelevantes y muy beneficiosos a la vez → bajar.
   - Eventos < 300 (binarios) o n < 400 (continuos) suele justificar bajar 1.

   **Dominio 5: Publication bias**
   - Si k ≥ 10: funnel plot + test de Egger.
   - Egger p < 0.10 o asimetría visual → bajar 1.
   - Si k < 10: no se puede evaluar formalmente; documentar limitación.
   - Si hay estudios registrados sin publicar (buscar en ClinicalTrials.gov vía biomcp), sospecha alta.

3. **Considerar upgrades** (raros, solo para observacionales):
   - Large effect size (RR > 2 o < 0.5): +1
   - Very large effect (RR > 5 o < 0.2): +2
   - Dose-response gradient: +1
   - Plausible confounders bias toward null pero efecto sigue significativo: +1

4. **Calcular calidad final**:
   - 4 puntos → High ⊕⊕⊕⊕
   - 3 puntos → Moderate ⊕⊕⊕◯
   - 2 puntos → Low ⊕⊕◯◯
   - 1 punto o menos → Very Low ⊕◯◯◯

5. **Generar `analisis/grade-summary.md`**:

```markdown
# GRADE Summary of Findings

## Outcome: [nombre]

| Dominio | Juicio | Justificación |
|---|---|---|
| Risk of bias | not serious / serious / very serious | ... |
| Inconsistency | not serious / serious / very serious | I²=X%, ... |
| Indirectness | not serious / serious / very serious | ... |
| Imprecision | not serious / serious / very serious | n=X, eventos=Y, ... |
| Publication bias | undetected / suspected / strongly suspected | Egger p=X (si k≥10) |

**Calidad de la evidencia: [HIGH / MODERATE / LOW / VERY LOW]**

**Resumen:** Hay evidencia de calidad [X] que sugiere [efecto del meta] con un efecto de [valor + CI].

---

[repetir para cada outcome]

## Tabla SoF (Summary of Findings)

| Outcome | Estudios (n) | Participantes | Efecto absoluto (riesgo en control) | Efecto absoluto (riesgo con intervención) | Effect relativo (95% CI) | Calidad evidencia GRADE |
|---|---|---|---|---|---|---|
```

## Reglas

- **NUNCA marcar "not serious" sin verificar todos los estudios contribuyentes**.
- **Cada juicio requiere justificación específica**, no genérica.
- **No usar GRADE para subgrupos exploratorios** (solo outcomes pre-especificados).
- **Si solo hay 1 estudio**: no se puede aplicar Inconsistency ni Publication bias, documentarlo.
- **Output debe ser pegable directamente** en la tabla SoF del manuscrito.

## Output

- `analisis/grade-summary.md` con un bloque por outcome + tabla SoF consolidada
- Commit con tag `[PRISMA-7] GRADE assessment for X outcomes`
