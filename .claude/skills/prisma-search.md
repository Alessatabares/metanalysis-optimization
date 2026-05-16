---
name: prisma-search
description: Construye strings de búsqueda sistemática (PubMed/Cochrane/Embase/Scopus) desde un PICO. Identifica MeSH terms, sinónimos, filtros. Ejecuta búsquedas vía PubMed MCP y reporta conteos para PRISMA flow.
---

# Skill: PRISMA Search Builder

Tu trabajo es construir y ejecutar estrategias de búsqueda sistemática reproducibles.

## Inputs esperados

- PICO del usuario (de `protocolo/protocolo.md`)
- Bases de datos a usar
- Filtros opcionales (años, idioma, tipo de estudio)

## Workflow

1. **Leer `protocolo/protocolo.md`** para extraer P-I-C-O exactos
2. **Identificar conceptos clave** y para cada uno listar:
   - Término MeSH principal
   - Términos libres (incluir variantes: plurales, sinónimos, acrónimos)
   - Truncamientos (`*` en PubMed)
3. **Construir cadenas booleanas** por base:
   - Bloques de (sinónimos OR sinónimos) unidos con AND
   - Aplicar filtros nativos (Publication Type, Language, Date)
4. **Ejecutar en PubMed** vía MCP pubmed: reportar n bruto
5. **Guardar resultados** en `busqueda/strategy.md` con strings exactos + fecha + conteos
6. **Exportar CSV** de los hits (PMID, título, autores, año, abstract, DOI) a `busqueda/results-pubmed.csv`

## Reglas

- **Nunca optimizar para reducir n**. Una búsqueda demasiado específica pierde estudios.
- **Documentar cada cambio** en la estrategia y por qué.
- **Buscar duplicados entre bases** (DOI o PMID) durante deduplicación en pandas.
- **Reportar fecha exacta** de búsqueda (las DBs cambian).

## Output esperado

- `busqueda/strategy.md` con todos los strings y conteos
- `busqueda/results-<db>.csv` por cada base
- Conteo para diagrama PRISMA (identificados, duplicados, a screening)

## Comandos útiles

```bash
# Deduplicar resultados consolidados (preferir DOI > PMID > título normalizado)
.venv/bin/python -c "
import pandas as pd
dfs = [pd.read_csv(f'busqueda/results-{db}.csv') for db in ['pubmed', 'cochrane']]
all_refs = pd.concat(dfs, ignore_index=True)
dedup = all_refs.drop_duplicates(subset=['doi'], keep='first')
print(f'Antes: {len(all_refs)}, Después: {len(dedup)}, Duplicados: {len(all_refs) - len(dedup)}')
dedup.to_csv('busqueda/results-merged-dedup.csv', index=False)
"
```
