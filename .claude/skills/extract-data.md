---
name: extract-data
description: Extrae datos cuantitativos y cualitativos de un paper incluido. Crea archivo doi-XXX.md en extraccion/papers/ con frontmatter completo, y agrega fila a extraccion/extraction.csv para meta-análisis.
---

# Skill: Data Extraction

Extracción estructurada de datos para meta-análisis.

## Inputs

- DOI del paper a extraer
- Paper accesible (vía Zotero MCP - PDF en storage local)

## Workflow

1. **Localizar paper** en Zotero (por DOI o título) vía Zotero MCP
2. **Leer full-text** completo (no solo abstract)
3. **Crear archivo** `extraccion/papers/doi-<doi-sanitized>.md` con:

```yaml
---
doi: 10.XXXX/YYYY
title: "..."
authors: ["LastName F", "..."]
year: 2023
journal: "..."
pmid: 12345678
zotero_key: "ABC123"
study_design: RCT
population_n: 500
population_description: "..."
intervention: "..."
comparator: "..."
outcomes:
  - name: "primary outcome"
    effect_type: OR
    effect: 0.85
    ci_low: 0.70
    ci_high: 1.02
    p: 0.08
follow_up: "12 months"
funding: "..."
conflict_of_interest: "..."
rob_tool: ROB-2
rob_overall: low
include: yes
prisma_stage: included
tags: ["..."]
---

# Resumen ejecutivo
(1 párrafo, lo esencial)

# PICO completo
- P: ...
- I: ...
- C: ...
- O: ...

# Resultados cuantitativos (tabla)
| Outcome | n int | events int | n con | events con | Effect | 95% CI | p |
|---|---|---|---|---|---|---|---|

# Riesgo de sesgo (ROB-2 o NOS)
(dominio por dominio)

# Limitaciones declaradas por autores

# Notas para síntesis
```

4. **Agregar fila a `extraccion/extraction.csv`** con todas las columnas
5. **Crear nota en Obsidian** (vía Obsidian MCP) en `papers/doi-XXX.md` con el mismo contenido (o link)
6. **Actualizar `prisma-flow.md`** moviendo el conteo a "included"

## Reglas

- **NUNCA imputar valores**. Si el paper no reporta SD, registrarlo como NA con nota.
- **Citar textualmente** datos clave (con número de tabla/figura).
- **Si hay subgrupos**, extraer cada uno como fila separada.
- **Outcomes múltiples = filas múltiples** en extraction.csv (long format).
- **Si los datos están solo en gráficos**, usar WebPlotDigitizer y documentar la incertidumbre.

## Tips de extracción rápida

- Para RCT con sample size grande, el ITT está casi siempre en Table 1 o Table 2.
- Riesgo relativo y odds ratio raramente vienen reportados; si solo tienes n/N, calcular después en `stats.py`.
- Para outcomes continuos, necesitas n + mean + SD por grupo.
- Para outcomes binarios, necesitas n + events por grupo.
