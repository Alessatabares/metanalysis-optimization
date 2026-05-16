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

**Core workflow:**
- `/prisma-search` — construye strings de búsqueda para PubMed/Cochrane/Embase desde un PICO
- `/screen-paper` — screening sistemático título/abstract o full-text con justificación
- `/extract-data` — crea nota estructurada del paper en `extraccion/papers/doi-*.md`
- `/assess-rob` — completa ROB-2 (RCT) o Newcastle-Ottawa (observacional)
- `/run-metaanalysis` — ejecuta meta-análisis con Python (random/fixed, forest, funnel, sensibilidad)
- `/prisma-flow` — actualiza diagrama PRISMA y verifica conteos

**Pasos administrativos / submission:**
- `/prospero-register` — genera texto completo para los 32 campos del formulario PROSPERO (sin API; copy-paste guiado)
- `/grade-evidence` — aplica GRADE (5 dominios) por outcome y genera tabla Summary of Findings para manuscrito
- `/manuscript-prisma` — genera draft de manuscrito siguiendo PRISMA 2020 (27 items) desde los datos ya extraídos

## MCP servers que usa el workflow

| MCP | Para qué |
|---|---|
| **biomcp** | PubMed E-utilities + ClinicalTrials.gov + MyVariant.info (con NCBI API key) |
| **openalex** | Catálogo libre 240M+ papers, redes de citas, alternativa a Web of Science |
| **zotero** | Lectura/escritura de biblioteca, exportar BibTeX, gestionar colecciones |
| **Obsidian (filesystem directo)** | Crear nota por paper (1 paper = 1 archivo), tags, links cruzados — sin MCP, acceso directo al vault |
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

## Estructura del monorepo

```
metanalysis-optimization/
├── README.md
├── CLAUDE.md                            # este archivo — reglas globales
├── .claude/skills/                      # 9 skills compartidos
├── _template/                           # archivos plantilla (copiados al iniciar proyecto)
│   ├── STATUS.md
│   ├── protocolo/protocolo.md
│   ├── busqueda/strategy.md
│   ├── extraccion/{screening,extraction,rob}.csv
│   └── analisis/{stats.py,prisma-flow.md}
├── projects/                            # ⭐ meta-análisis reales (uno por carpeta)
│   ├── meta-<tema>-<intervencion>/
│   │   ├── STATUS.md
│   │   ├── protocolo/
│   │   ├── busqueda/
│   │   ├── extraccion/papers/
│   │   ├── analisis/
│   │   └── manuscrito.md
│   └── (otros)
├── docs/
│   ├── lessons-learned.md               # mejoras al workflow con fecha
│   └── changelog.md                     # versionado del workflow
├── scripts/
│   └── new-project.sh                   # crea proyecto nuevo desde _template
└── requirements.txt
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

1. Desde la raíz del repo: `./scripts/new-project.sh meta-<tema>-<intervencion>`
2. Eso crea `projects/meta-<tema>-<intervencion>/` con todos los archivos plantilla copiados desde `_template/`
3. Editar `projects/meta-X/STATUS.md` con título + PICO
4. Editar `projects/meta-X/protocolo/protocolo.md` con el protocolo completo PRISMA-P
5. Decir a Claude: "trabajemos en projects/meta-X, empecemos el workflow PRISMA"

A partir de ahí Claude lee `STATUS.md` y aplica los skills correspondientes paso a paso.

## Mejora continua del workflow

Cuando trabajando en un proyecto identifiques que un skill, plantilla o convención se puede mejorar:

1. Dile a Claude: "esto se puede mejorar porque..."
2. Claude edita el archivo correspondiente en `.claude/skills/` o `_template/`
3. Claude documenta el cambio en `docs/lessons-learned.md` con fecha y justificación
4. Si es cambio mayor, también actualiza `docs/changelog.md`
5. Commit con tag `[workflow] descripcion del cambio`

Los proyectos en `projects/` heredan automáticamente las mejoras (comparten skills y plantillas vía el monorepo).
