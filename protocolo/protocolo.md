# Protocolo de Meta-análisis (PRISMA-P 2015)

> Este documento se redacta ANTES de iniciar screening. Cualquier cambio post-screening debe documentarse como enmienda al final.

## 1. Información administrativa

- **Título provisional**: 
- **Autores**: 
- **Fecha de versión**: 
- **Versión del protocolo**: 1.0
- **Pre-registro (PROSPERO/OSF)**: [número y fecha]
- **Fuentes de financiamiento**: 
- **Conflictos de interés**: 

## 2. Antecedentes y justificación

- **Descripción del problema clínico**: 
- **Estado actual de la evidencia (brecha que motiva la revisión)**: 
- **Por qué este meta-análisis es necesario AHORA**: 

## 3. Objetivo y pregunta PICO

### Pregunta clínica
[Una sola pregunta clara, contestable, relevante]

### Componentes PICO
- **P** (Población): 
- **I** (Intervención): 
- **C** (Comparador): 
- **O** (Outcomes):
  - **Primario**: 
  - **Secundarios**: 
- **S** (Setting, opcional): 
- **T** (Time/duración, opcional): 

### Tipos de estudio a incluir
- [ ] RCT
- [ ] Cohortes prospectivas
- [ ] Cohortes retrospectivas
- [ ] Casos y controles
- [ ] Cross-sectional
- [ ] Otros: 

## 4. Criterios de elegibilidad

### Criterios de inclusión
1. 
2. 
3. 

### Criterios de exclusión
1. 
2. 
3. 

### Filtros operacionales
- **Idioma**: [inglés, español, otros]
- **Rango de fechas**: 
- **Tipos de publicación**: [primarios, full-text; excluir abstracts congresos, cartas al editor, comentarios]
- **Acceso**: [con/sin restricción a full-text]

## 5. Fuentes de información y estrategia de búsqueda

### Bases de datos
- [ ] PubMed/MEDLINE
- [ ] Cochrane CENTRAL
- [ ] Embase (si acceso)
- [ ] Scopus / Web of Science
- [ ] LILACS / SciELO (literatura latinoamericana)
- [ ] ClinicalTrials.gov (estudios no publicados)
- [ ] Búsqueda manual en referencias de incluidos (snowballing)
- [ ] Búsqueda gris (Google Scholar, tesis)

### Strings de búsqueda
Ver `busqueda/strategy.md` (un string por DB, con sintaxis nativa).

### Fecha de búsqueda
- Búsqueda inicial: 
- Actualización (si aplica): 

## 6. Proceso de selección de estudios

### Screening
1. Importación de todas las referencias a Zotero (carpeta proyecto)
2. Deduplicación automatizada + manual
3. **Screening de título y abstract** por 2 revisores independientes (o 1 revisor + Claude como segundo, con discrepancias resueltas por discusión)
4. **Screening de full-text** por 2 revisores; razones de exclusión documentadas en `screening.csv`

### Software
- Zotero para gestión de referencias
- Notas estructuradas en Obsidian (1 paper = 1 nota markdown)

## 7. Extracción de datos

### Variables a extraer
- Identificación: autor, año, DOI, PMID, journal, país
- Diseño: tipo de estudio, duración, follow-up
- Población: n, edad, sexo, criterios diagnósticos
- Intervención: nombre, dosis, duración, vía
- Comparador: tipo, dosis, duración
- Outcomes:
  - Primario: definición, instrumento, momento
  - Secundarios: idem
- Efectos: tipo (OR/RR/HR/MD/SMD), valor, IC95%, p
- Financiamiento y conflictos de interés

### Plantilla
Ver `extraccion/extraction.csv` (vacío al inicio).

### Quién extrae
- 1 revisor extrae, otro verifica (o Claude verifica con el paper original)

## 8. Riesgo de sesgo

- **RCT**: ROB-2 (Cochrane Risk of Bias 2)
- **Observacionales**: Newcastle-Ottawa Scale (NOS) o ROBINS-I si interventional
- **Sistemáticas previas**: AMSTAR-2 si aplica

Cada paper en `extraccion/rob.csv` con dominio por dominio.

## 9. Síntesis de los resultados

### Síntesis cuantitativa (meta-análisis)
- **Modelo**: efectos aleatorios (DerSimonian-Laird o REML)
- **Medida de efecto**: [OR/RR/HR/MD/SMD] según outcome
- **Software**: Python (`statsmodels`, `PythonMeta`)
- **Heterogeneidad**: I², τ², Q, p
- **Subgrupos pre-especificados**: [listar]
- **Sensibilidad**: leave-one-out, comparación fixed vs random

### Síntesis cualitativa
- Tabla resumen de estudios incluidos
- Síntesis narrativa por outcome si meta no factible

## 10. Sesgo de publicación

- Funnel plot si k ≥ 10
- Test de Egger
- Trim-and-fill si asimetría sospechada

## 11. Calidad de la evidencia (GRADE)

Para outcomes clave aplicar GRADE: dominios de calidad (riesgo sesgo, inconsistencia, indirectness, imprecisión, sesgo publicación).

## 12. Enmiendas al protocolo

| Fecha | Versión | Cambio | Justificación |
|---|---|---|---|

## 13. Cronograma estimado

- Búsqueda inicial: 
- Screening T/A: 
- Screening full-text: 
- Extracción: 
- Análisis: 
- Redacción: 
- Submission: 
