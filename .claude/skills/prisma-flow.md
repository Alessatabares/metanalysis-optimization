---
name: prisma-flow
description: Actualiza y valida el diagrama de flujo PRISMA 2020. Cuenta automáticamente identificados, duplicados, screened, eligible, included, excluded con razones. Genera diagrama mermaid + tabla de conteos.
---

# Skill: PRISMA Flow Diagram

Mantén el diagrama de flujo PRISMA actualizado y consistente con los archivos.

## Inputs

- `busqueda/results-*.csv` (identificados por fuente)
- `extraccion/screening.csv` (decisiones de screening)
- `extraccion/papers/*.md` (incluidos finales)

## Workflow

1. **Contar identificados** por DB (sumando `results-pubmed.csv`, `results-cochrane.csv`, etc.)
2. **Contar duplicados removidos** (`results-merged-dedup.csv` vs suma de fuentes)
3. **Contar screening T/A**: 
   - Total screened
   - Excluded en T/A (con conteo por razón)
   - Continuaron a full-text
4. **Contar full-text**:
   - Sought for retrieval
   - Not retrieved (no full-text)
   - Assessed
   - Excluded (con razones)
5. **Contar incluidos** (archivos en `extraccion/papers/` con `prisma_stage: included`)
6. **Generar diagrama mermaid** en `analisis/prisma-flow.md`:

```markdown
# Diagrama de flujo PRISMA 2020

\`\`\`mermaid
flowchart TD
    A["Identificados por bases de datos<br/>PubMed n=XXX<br/>Cochrane n=XXX<br/>Embase n=XXX<br/>Total n=XXX"] --> B[Después de deduplicación<br/>n=XXX]
    A2["Identificados por otras fuentes<br/>Snowballing n=XXX<br/>Búsqueda gris n=XXX"] --> B
    B --> C[Screened por título/abstract<br/>n=XXX]
    C --> D[Excluidos en T/A<br/>n=XXX<br/>wrong_population n=X<br/>wrong_intervention n=X<br/>wrong_design n=X<br/>...]
    C --> E[Solicitados full-text<br/>n=XXX]
    E --> F[No recuperados<br/>n=XXX]
    E --> G[Evaluados full-text<br/>n=XXX]
    G --> H[Excluidos full-text<br/>n=XXX<br/>razones...]
    G --> I[Incluidos en revisión<br/>n=XXX<br/>De los cuales:<br/>RCT n=X<br/>Cohort n=X]
    I --> J[Incluidos en meta-análisis<br/>n=XXX por outcome]
\`\`\`

## Conteos detallados

[tabla con cada paso y conteo]
```

7. **Validar coherencia**:
   - Total identificados = duplicados + (screened)
   - Screened = excluded T/A + sought full-text
   - Sought = not retrieved + assessed
   - Assessed = excluded full-text + included
   - Si no cuadra: error en CSVs → reportar discrepancia

## Reglas

- **Conteos vienen de archivos, no de memoria**. Si los CSV cambian, regenerar.
- **Razones de exclusión vienen del CSV** (columna `reason`).
- **Diagrama incluido siempre en el manuscrito** (figura 1).
- **Versión versionada en cada cambio** (commit).

## Output

- `analisis/prisma-flow.md` actualizado
- Validación de consistencia (warnings si conteos no cuadran)
