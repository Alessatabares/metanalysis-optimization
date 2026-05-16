---
name: manuscript-prisma
description: Genera el manuscrito completo del meta-análisis siguiendo PRISMA 2020 (27 items). Pulla automáticamente de protocolo.md, extraction.csv, rob.csv, prisma-flow.md, grade-summary.md, results-*.md. Output listo para someter, con checklist PRISMA marcado.
---

# Skill: Manuscript Builder (PRISMA 2020)

Convierte todos los datos ya recolectados en un manuscrito completo siguiendo PRISMA 2020 (publicado en BMJ 2021;372:n71). Te ahorra ~20 horas de redacción manual.

## Inputs (todos deben existir y estar completos)

- `protocolo/protocolo.md`
- `busqueda/strategy.md` + `busqueda/results-*.csv`
- `extraccion/screening.csv` + `extraccion/extraction.csv` + `extraccion/rob.csv`
- `extraccion/papers/doi-*.md` (notas por paper)
- `analisis/prisma-flow.md`
- `analisis/results-*.md` por outcome
- `analisis/grade-summary.md` (si ya corriste `/grade-evidence`)
- `analisis/forest-*.png` y `analisis/funnel-*.png`

## Workflow

1. **Validar pre-requisitos**: si falta cualquier input crítico, listar qué falta y abortar.

2. **Generar `manuscrito.md`** con estructura PRISMA 2020:

```markdown
# [Título: descriptivo + identifica como "systematic review and meta-analysis"]

[Autores con afiliaciones + corresponding author]

## Abstract (item 2: structured abstract, max 300 palabras)

### Background
[1 frase con justificación]

### Objectives
[pregunta PICO en 1 frase]

### Methods
- Sources: [DBs + fechas]
- Eligibility: [diseño + población clave]
- Risk of bias: [ROB-2 o NOS]
- Synthesis: [random effects, software]
- Registration: PROSPERO CRDxxxxx

### Results
- k=X studies (n=Y participants)
- Pooled effect for [primary outcome]: [valor] (95% CI [X-Y])
- Heterogeneity: I²=X%
- GRADE: [calidad]

### Conclusions
[1-2 frases con implicación clínica]

**Keywords:** [5-7]
**Funding:** [...]
**Registration:** PROSPERO CRD42024XXXXX

---

## Introduction (items 3-4)

### Rationale (item 3)
[copia desde protocolo/sección Antecedentes, expandir con citas relevantes]

### Objectives (item 4)
[copia pregunta PICO desde protocolo, formato declarativo:
"This systematic review and meta-analysis aimed to..."]

---

## Methods (items 5-21)

### Eligibility criteria (item 5)
**Population:** [...]
**Intervention:** [...]
**Comparator:** [...]
**Outcomes:** [primary, secondary]
**Study designs:** [...]
**Setting/timing/language:** [...]

### Information sources (item 6)
[Lista DBs + fechas búsqueda + actualización]

### Search strategy (item 7)
[Strings completos por DB en Apéndice; resumen en texto]

### Selection process (item 8)
[Cuántos revisores, cómo se resolvieron discrepancias]

### Data collection process (item 9)
[Cómo se extrajeron datos, formulario, doble verificación]

### Data items (item 10)
- (10a) Outcomes: [definición operacional, instrumentos, momento]
- (10b) Otras variables: [lista de moderadores/predictores]

### Study risk of bias assessment (item 11)
[ROB-2 / NOS, dominios, quién evaluó]

### Effect measures (item 12)
[OR/RR/HR/MD/SMD por outcome]

### Synthesis methods (item 13)
- 13a: Eligibility for synthesis
- 13b: Data preparation (e.g. conversión a log)
- 13c: Tabulation/visualización
- 13d: **Modelo (random effects DL/REML), heterogeneidad (I², τ²)**
- 13e: Exploración de heterogeneidad (subgrupos, meta-regresión)
- 13f: Sensibilidad (leave-one-out, fixed vs random)

### Reporting bias assessment (item 14)
[Funnel + Egger si k≥10]

### Certainty assessment (item 15)
[GRADE, ver `analisis/grade-summary.md`]

---

## Results (items 16-22)

### Study selection (item 16)
[Generar desde `analisis/prisma-flow.md`:
"De n=X identificados, n=Y after dedup, n=Z screened by T/A, n=W full-text assessed, n=V included.
Razones principales de exclusión full-text: ..."]

**Figure 1.** PRISMA flow diagram [insertar diagrama de prisma-flow.md]

### Study characteristics (item 17)
[Tabla 1 generada desde extraction.csv: autor/año, país, diseño, n, intervención, comparador, follow-up, outcomes reportados]

### Risk of bias in studies (item 18)
[Tabla/figura desde rob.csv: dominio por dominio, % en cada categoría]
[Figura 2: ROB summary]

### Results of individual studies (item 19)
[Forest plot por outcome con estudios individuales]

### Results of syntheses (item 20)
- (20a) Resumen de estudios y características
- (20b) Para cada outcome: pooled effect + CI + heterogeneidad
- (20c) Investigación de heterogeneidad (subgrupos pre-especificados)
- (20d) Sensibilidad

[insertar forest plots]

### Reporting biases (item 21)
[Funnel plot + Egger interpretation]

### Certainty of evidence (item 22)
[Tabla SoF desde grade-summary.md]

---

## Discussion (items 23-24)

### Summary of evidence (item 23a)
[Hallazgos principales en contexto de evidencia previa]

### Limitations of evidence (item 23b)
- Limitaciones de los estudios incluidos
- Limitaciones de outcomes (sustitutos, follow-up corto, etc.)

### Limitations of review (item 23c)
- Limitaciones metodológicas de esta revisión

### Implications (item 23d)
- Para práctica clínica
- Para investigación futura

### Conclusions (item 24)
[1-2 párrafos con conclusión clave]

---

## Other information (items 24-27)

### Registration (item 24)
PROSPERO CRDxxxxx (URL completa)

### Protocol (item 25)
[link al protocolo en GitHub]

### Support (item 26)
Funding: [...]

### Competing interests (item 27)
[declaración]

### Availability of data (item 27)
[Github repo con extraction.csv, scripts, etc.]

---

## References
[Bibliografía generada desde Zotero, formato Vancouver o el de la revista target]

---

# PRISMA 2020 Checklist (anexo)

| Item | Sección | Reportado en |
|---|---|---|
| 1 | Title | ✓ |
| 2 | Abstract | ✓ |
| 3 | Rationale | Introduction |
| 4 | Objectives | Introduction |
| 5 | Eligibility | Methods |
| 6 | Information sources | Methods |
| ... (los 27 items) ... |

```

3. **Crear `manuscrito.md`** y nota correspondiente en Obsidian (`Metaanalisis/synthesis/manuscript-draft.md`).

4. **Validaciones finales**:
   - Todos los outcomes pre-especificados están reportados (no solo los significativos)
   - PRISMA checklist 27/27 cubierto
   - Cada cita en el texto tiene su referencia
   - Tablas y figuras numeradas y referenciadas

## Reglas

- **NUNCA inventar datos**. Si una métrica no está en los CSVs, marcar "[FALTA]" y reportar al final.
- **NUNCA cambiar el outcome primario** entre protocolo y manuscrito sin documentar como amendment.
- **Reportar resultados negativos** con el mismo detalle que los positivos.
- **Forest/funnel plots** referenciados en el texto, no solo insertados.
- **Limitations sección honesta**: si hay sesgo de publicación sospechoso o evidencia GRADE Low, decirlo claramente.
- **Conclusiones proporcionales a la evidencia**: si GRADE es Low/Very Low, NO recomendaciones fuertes.

## Customización por revista

Pregúntale al usuario la revista target. Cada una tiene quirks:
- **BMJ**: Methods completos en Apéndice + Methods condensados en main text
- **Lancet**: Methods en Methods, no en supplementary
- **Cochrane**: usa formato MECIR + tabla GRADE expandida
- **PLoS Medicine**: requiere CONSORT/STROBE adherido en estudios incluidos

## Output

- `manuscrito.md` con draft completo
- `manuscrito-checklist-prisma.md` con 27 items mapeados
- Nota espejo en Obsidian
- Commit con tag `[PRISMA-9] Manuscript draft v1`

## Próximos pasos sugeridos al usuario

1. Revisar draft sección por sección
2. Pulir Discussion (lo más subjetivo, requiere tu juicio clínico)
3. Editar referencias en formato de la revista target
4. Pedir revisión a coautores
5. Submission
