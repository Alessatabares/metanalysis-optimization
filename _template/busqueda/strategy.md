# Estrategia de búsqueda

> Strings reproducibles por base de datos. Documenta cualquier modificación.

## Términos del PICO (mapeo)

| Componente | Términos libres | MeSH / Emtree / equivalentes |
|---|---|---|
| P | | |
| I | | |
| C | | |
| O | | |

## PubMed/MEDLINE

```
(("term1"[MeSH Terms] OR "term1"[Title/Abstract])
AND
("intervention"[MeSH Terms] OR "intervention"[Title/Abstract]))
AND ("randomized controlled trial"[Publication Type] OR "clinical trial"[Publication Type])
AND english[Language]
AND ("2010/01/01"[Date - Publication] : "3000"[Date - Publication])
```

**Fecha búsqueda**: 
**Resultados**: n=

## Cochrane CENTRAL

```
#1 MeSH descriptor: [term1] explode all trees
#2 ("term1") in Title Abstract Keyword
#3 #1 OR #2
#4 MeSH descriptor: [intervention] explode all trees
#5 ("intervention") in Title Abstract Keyword
#6 #4 OR #5
#7 #3 AND #6
```

**Fecha búsqueda**: 
**Resultados**: n=

## Embase

```
('term1'/exp OR 'term1':ti,ab,kw)
AND ('intervention'/exp OR 'intervention':ti,ab,kw)
AND ('randomized controlled trial'/de OR 'controlled clinical trial'/de)
AND [english]/lim
```

**Fecha búsqueda**: 
**Resultados**: n=

## Scopus

```
TITLE-ABS-KEY("term1" AND "intervention")
AND PUBYEAR > 2009
AND LANGUAGE("english")
AND DOCTYPE("ar")
```

**Fecha búsqueda**: 
**Resultados**: n=

## LILACS

```
(term1) AND (intervention) [Spanish/Portuguese versions]
```

**Fecha búsqueda**: 
**Resultados**: n=

## Búsquedas adicionales

- **Snowballing forward**: citas que citan a los incluidos clave (Scholar Gateway)
- **Snowballing backward**: referencias de cada incluido
- **Búsqueda gris**: Google Scholar primeras 200 entradas, ClinicalTrials.gov (estudios completados sin publicar)

## Resumen de conteos (para PRISMA flow)

| Fuente | Resultados | Fecha |
|---|---|---|
| PubMed | | |
| Cochrane | | |
| Embase | | |
| Scopus | | |
| LILACS | | |
| Otros | | |
| **Total identificados** | | |
| **Duplicados removidos** | | |
| **A screening** | | |
