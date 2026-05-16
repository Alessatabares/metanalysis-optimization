# Workflow de Meta-análisis Médico (PRISMA 2020)

Asistente para conducir meta-análisis siguiendo PRISMA 2020 y redactando el protocolo en paralelo. Optimizado para minimizar trabajo repetitivo y mantener trazabilidad completa para reproducibilidad.

## Filosofía operativa

- **PRISMA es la norma**, no una guía. Cada decisión debe quedar registrada con justificación.
- **Trazabilidad sobre velocidad**: si no se puede reproducir, no sirve.
- **Protocolo vivo**: se redacta en paralelo a la búsqueda, no después.
- **Una decisión = una nota**: cada inclusión/exclusión documentada con razón.
- **Datos crudos en tablas, no en prosa**: extracción a CSV/tabla, narrativa después.

## Flujo PRISMA 2020 — 9 pasos

```
1. PROTOCOLO       → protocolo/protocolo.md (PICO + criterios + métodos)
2. BÚSQUEDA        → busqueda/strategy.md + busqueda/results-*.csv
3. SCREENING       → extraccion/screening.csv (T/A → Full text)
4. ELEGIBILIDAD    → extraccion/papers/doi-*.md (1 por paper incluido)
5. EXTRACCIÓN      → extraccion/extraction.csv (datos cuantitativos)
6. RIESGO SESGO    → extraccion/rob.csv (ROB-2 o NOS)
7. SÍNTESIS        → analisis/stats.py (efecto + heterogeneidad)
8. PRISMA FLOW     → analisis/prisma-flow.md (diagrama)
9. REPORTE         → manuscrito.md (PRISMA checklist completo)
```

## Skills disponibles (invocar con /<skill>)

- `/prisma-search` — construye strings de búsqueda para PubMed/Cochrane/Embase desde un PICO
- `/screen-paper` — screening sistemático título/abstract o full-text con justificación
- `/extract-data` — crea nota estructurada del paper en `extraccion/papers/doi-*.md`
- `/assess-rob` — completa ROB-2 (RCT) o Newcastle-Ottawa (observacional)
- `/run-metaanalysis` — ejecuta meta-análisis con Python (random/fixed, forest, funnel, sensibilidad)
- `/prisma-flow` — actualiza diagrama PRISMA y verifica conteos

## MCP servers que usa el workflow

| MCP | Para qué |
|---|---|
| **pubmed** | Búsqueda E-utilities, recuperar abstracts, MeSH terms |
| **zotero** | Lectura/escritura de biblioteca, exportar BibTeX, gestionar colecciones |
| **obsidian** | Crear nota por paper (1 paper = 1 archivo), tags, links cruzados |
| **claude.ai Scholar Gateway** | Snowballing de citas, búsqueda semántica |
| **claude.ai Consensus** | Síntesis de evidencia preliminar por pregunta |
| **github** | Versionar protocolo + análisis (reproducibilidad obligatoria) |
| **Context7** | Documentación actualizada de scipy/statsmodels/pandas |

## Reglas duras

1. **Una pregunta PICO por proyecto**. Si surge una segunda, es OTRO meta-análisis.
2. **Pre-registrar protocolo** (PROSPERO o OSF) ANTES de iniciar screening si el alcance es serio.
3. **Doble screening cuando aplique** (idealmente 2 revisores). Aquí asumo 1 revisor + Claude como segundo independiente; documentar.
4. **DOI como ID primario** de cada paper. Nombres de archivo: `doi-10-XXXX-YYYY.md` (slash → guión).
5. **No modificar datos crudos**. Toda transformación va en script `stats.py`, no a mano en el CSV.
6. **Todo commit a GitHub con mensaje descriptivo** del paso PRISMA al que pertenece.
7. **Cada exclusión documenta la razón** en el CSV de screening — sin "no aplica" sin justificar.

## Estructura del proyecto

```
metaanalisis-<tema>/
├── CLAUDE.md                            # este archivo (copiar de template)
├── .claude/
│   └── skills/                          # workflow scripts
├── protocolo/
│   ├── protocolo.md                     # PICO + métodos (PRISMA-P)
│   └── prospero-registration.md         # número y fecha si pre-registrado
├── busqueda/
│   ├── strategy.md                      # strings exactos por DB (reproducible)
│   ├── results-pubmed.csv               # exportación PubMed
│   ├── results-cochrane.csv             # exportación Cochrane
│   └── results-merged-dedup.csv         # consolidado deduplicado
├── extraccion/
│   ├── screening.csv                    # T/A screening (incluir/excluir + razón)
│   ├── papers/                          # 1 nota markdown por incluido
│   │   └── doi-10-XXXX-YYYY.md
│   ├── extraction.csv                   # datos cuantitativos para meta
│   └── rob.csv                          # riesgo de sesgo
├── analisis/
│   ├── stats.py                         # script reproducible (versionado)
│   ├── prisma-flow.md                   # diagrama
│   ├── forest-plot.png                  # output
│   ├── funnel-plot.png                  # output
│   └── sensibilidad.md                  # análisis post-hoc
├── manuscrito.md                        # borrador final (PRISMA checklist)
└── requirements.txt                     # deps Python
```

## Convenciones de naming

- **Archivos de paper**: `doi-<doi-con-guiones>.md` (en `extraccion/papers/`)
- **Tags Obsidian**: `#metaanalisis/<tema>`, `#prisma/<paso>`, `#design/RCT|cohort|case-control`, `#rob/low|some|high`, `#included|#excluded`
- **Commits git**: `[PRISMA-<paso>] <descripcion corta>` (ej. `[PRISMA-2] Búsqueda PubMed n=347`)

## Plantilla de nota por paper (frontmatter obligatorio)

```yaml
---
doi: 10.XXXX/YYYY
title: "..."
authors: ["LastName F", "..."]
year: 2023
journal: "..."
pmid: 12345678
zotero_key: "ABC123"
study_design: RCT | cohort | case-control | cross-sectional | systematic-review
population_n: 500
population_description: "..."
intervention: "..."
comparator: "..."
outcomes:
  - name: "mortalidad 30d"
    effect_type: OR | RR | HR | MD | SMD
    effect: 0.85
    ci_low: 0.70
    ci_high: 1.02
    p: 0.08
follow_up: "12 meses"
funding: "..."
conflict_of_interest: "..."
rob_tool: ROB-2 | NOS
rob_overall: low | some_concerns | high | unclear
include: yes | no | maybe
exclusion_reason: "" # solo si include=no
prisma_stage: identified | screened | eligible | included | excluded
tags: ["..."]
---

# Resumen ejecutivo
(1 párrafo)

# PICO
- **P**: ...
- **I**: ...
- **C**: ...
- **O**: ...

# Resultados cuantitativos
| Outcome | n | Effect | 95% CI | p |
|---|---|---|---|---|

# Riesgo de sesgo
(dominio por dominio según ROB-2 o NOS)

# Notas para síntesis
- ...
```

## Estadística

- Python con `numpy`, `pandas`, `scipy.stats`, `statsmodels`, `matplotlib`, `meta-analysis` (PythonMeta o pymeta-analysis).
- **Modelo por defecto**: efectos aleatorios (DerSimonian-Laird o REML).
- Heterogeneidad: I², τ², Q de Cochran.
- Sesgo de publicación: funnel plot + test de Egger si k≥10.
- Sensibilidad: leave-one-out + análisis por subgrupos pre-especificados.
- Robustez: comparar con modelo de efectos fijos.

## Anti-patrones

- ❌ Buscar sin protocolo (genera sesgo).
- ❌ "Decidir después" criterios de inclusión.
- ❌ Excluir papers sin razón escrita.
- ❌ Cambiar el outcome primario después de ver resultados.
- ❌ Hacer estadística en Excel sin versionar.
- ❌ Crear notas de paper sin frontmatter completo (rompe agregación).
- ❌ Olvidar reportar resultados negativos o no significativos.

## Cómo empezar un nuevo meta-análisis

1. Copia esta plantilla: `cp -r metaanalisis-template metaanalisis-<tema>`
2. Edita `protocolo/protocolo.md` con tu PICO completo
3. Invoca `/prisma-search` para construir los strings de búsqueda
4. Pre-registra en PROSPERO (recomendado)
5. Ejecuta búsquedas y guarda CSVs en `busqueda/`
6. Importa a Zotero (carpeta del proyecto)
7. Invoca `/screen-paper` por cada paper o batch
8. Para incluidos, invoca `/extract-data` y `/assess-rob`
9. Cuando tengas ≥3 estudios para el outcome, invoca `/run-metaanalysis`
10. Genera diagrama PRISMA con `/prisma-flow`
11. Redacta manuscrito siguiendo PRISMA 2020 checklist
