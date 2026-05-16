---
name: screen-paper
description: Hace screening sistemático de papers (título/abstract o full-text) contra los criterios de inclusión/exclusión del protocolo. Documenta cada decisión con justificación en screening.csv y marca el stage PRISMA correspondiente.
---

# Skill: Paper Screening

Screening sistemático contra criterios pre-especificados.

## Inputs esperados

- DOI o PMID o título del paper (uno o varios)
- Fase: `title_abstract` o `full_text`

## Workflow por paper

1. **Leer criterios** de `protocolo/protocolo.md` (sección "Criterios de elegibilidad")
2. **Recuperar paper**:
   - Si solo DOI/PMID: buscar abstract vía PubMed MCP
   - Si full-text: leer PDF de Zotero vía Zotero MCP
3. **Evaluar criterio por criterio**:
   - Listar cada criterio
   - Marcar SÍ/NO/INCIERTO + cita textual del paper
4. **Decisión final**: include / exclude / maybe (full-text needed)
5. **Registrar en `extraccion/screening.csv`** una fila:
   - doi, pmid, title, authors, year, journal
   - stage = "title_abstract" o "full_text"
   - decision = "include" / "exclude" / "maybe"
   - reason = razón CONCRETA (no "no cumple")
   - reviewer = "claude" o nombre
   - date = ISO date

## Reglas

- **Una razón de exclusión por paper** (la primera que rompe un criterio). Si hay múltiples, listar todas.
- **Razones estandarizadas** (facilita PRISMA flow):
  - `wrong_population`
  - `wrong_intervention`
  - `wrong_comparator`
  - `wrong_outcome`
  - `wrong_design`
  - `wrong_language`
  - `out_of_date_range`
  - `duplicate`
  - `no_full_text`
  - `conference_abstract`
  - `editorial_or_commentary`
- **"Maybe" obliga a full-text** en siguiente ronda.
- **Si include en T/A → siguiente fase**. Si include en full-text → invocar `/extract-data`.

## Output esperado

- Una fila por paper en `screening.csv`
- Si included a full-text, crear placeholder en `extraccion/papers/doi-XXX.md` con frontmatter mínimo
- Update `analisis/prisma-flow.md` con conteos nuevos
