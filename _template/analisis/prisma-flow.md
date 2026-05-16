# Diagrama de flujo PRISMA 2020

> Regenerar con `/prisma-flow` cada vez que cambien los CSV.

```mermaid
flowchart TD
    A["Identificados por bases de datos<br/>PubMed n=0<br/>Cochrane n=0<br/>Embase n=0<br/>Total n=0"] --> B["Después de deduplicación<br/>n=0"]
    A2["Identificados por otras fuentes<br/>Snowballing n=0<br/>Búsqueda gris n=0"] --> B
    B --> C["Screened título/abstract<br/>n=0"]
    C --> D["Excluidos T/A<br/>n=0"]
    C --> E["Solicitados full-text<br/>n=0"]
    E --> F["No recuperados<br/>n=0"]
    E --> G["Evaluados full-text<br/>n=0"]
    G --> H["Excluidos full-text<br/>n=0<br/>(razones)"]
    G --> I["Incluidos en revisión<br/>n=0"]
    I --> J["Incluidos en meta-análisis<br/>n=0"]
```

## Conteos por etapa

| Etapa | n | Notas |
|---|---|---|
| Identificados (PubMed) | 0 | |
| Identificados (Cochrane) | 0 | |
| Identificados (Embase) | 0 | |
| Identificados (otras) | 0 | |
| **Total identificados** | **0** | |
| Duplicados removidos | 0 | |
| A screening | 0 | |
| Excluidos T/A | 0 | desglose abajo |
| A full-text | 0 | |
| Excluidos full-text | 0 | desglose abajo |
| **Incluidos en revisión** | **0** | |
| **Incluidos en meta** | **0** | por outcome |

## Razones de exclusión

| Razón | T/A | Full-text |
|---|---|---|
| wrong_population | 0 | 0 |
| wrong_intervention | 0 | 0 |
| wrong_comparator | 0 | 0 |
| wrong_outcome | 0 | 0 |
| wrong_design | 0 | 0 |
| wrong_language | 0 | 0 |
| conference_abstract | 0 | 0 |
| no_full_text | 0 | 0 |
| duplicate | 0 | 0 |
| editorial_or_commentary | 0 | 0 |
