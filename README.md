# Meta-analysis Optimization

Plantilla y workflow para conducir meta-análisis médicos siguiendo PRISMA 2020. Diseñada para reducir trabajo repetitivo, mantener trazabilidad completa y permitir reproducibilidad.

## Qué incluye

- **Workflow PRISMA 2020 paso a paso** (ver `CLAUDE.md`)
- **6 skills** (Claude Code) para automatizar cada etapa: búsqueda, screening, extracción, riesgo de sesgo, meta-análisis, diagrama PRISMA
- **Plantillas** para protocolo (PRISMA-P), strategy de búsqueda, extracción de datos, riesgo de sesgo
- **Script de meta-análisis** en Python (random/fixed effects, forest plot, funnel plot, sensibilidad)
- **Integración con MCPs**: Zotero, PubMed (vía BioMCP), GitHub, Scholar Gateway, Consensus

## Cómo empezar un meta-análisis nuevo

```bash
# Clona o copia este repo como punto de partida
git clone <este-repo> metaanalisis-<tema>
cd metaanalisis-<tema>

# Crea venv e instala deps
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Empieza editando el protocolo con tu PICO
$EDITOR protocolo/protocolo.md
```

Luego, en Claude Code, sigue el workflow PRISMA usando los skills:

| Etapa PRISMA | Skill | Output |
|---|---|---|
| 1. Protocolo | (manual) | `protocolo/protocolo.md` |
| 2. Búsqueda | `/prisma-search` | `busqueda/results-*.csv` |
| 3. Screening T/A | `/screen-paper` | `extraccion/screening.csv` |
| 4. Full-text | `/screen-paper` | actualiza screening + crea `papers/doi-*.md` |
| 5. Extracción | `/extract-data` | `extraccion/extraction.csv` + notas |
| 6. Riesgo de sesgo | `/assess-rob` | `extraccion/rob.csv` |
| 7. Meta-análisis | `/run-metaanalysis` | `analisis/stats.py` + plots |
| 8. PRISMA flow | `/prisma-flow` | `analisis/prisma-flow.md` |

## Convenciones clave

- **DOI como ID primario** de cada paper
- **1 paper = 1 archivo** `doi-XXX.md` con frontmatter YAML completo
- **Toda exclusión documenta su razón** en `screening.csv`
- **Random effects por defecto** para meta-análisis
- **Cada paso a su commit** con tag `[PRISMA-N]`

## Estructura

```
.
├── CLAUDE.md                # workflow + reglas operativas
├── .claude/skills/          # 6 skills invocables
├── protocolo/protocolo.md   # PRISMA-P
├── busqueda/                # strings + resultados por DB
├── extraccion/              # screening + extraction + rob (CSVs) + papers/
├── analisis/                # stats.py + plots + PRISMA flow
├── requirements.txt
└── README.md
```

## Licencia

MIT
