---
name: prospero-register
description: Genera el texto exacto para cada campo del formulario PROSPERO desde protocolo/protocolo.md. Crea prospero-submission.md con cada campo numerado listo para copy-paste a https://www.crd.york.ac.uk/prospero/
---

# Skill: PROSPERO Registration Builder

PROSPERO no tiene API. El formulario web tiene ~45 campos con reglas estrictas (límites de caracteres, formato específico). Este skill mapea tu protocolo a cada campo y te ahorra el trabajo de averiguar qué va dónde.

## Inputs

- `protocolo/protocolo.md` completo (no acepta protocolo incompleto)
- Confirmar que NO has iniciado screening (PROSPERO solo acepta protocolos prospectivos)

## Workflow

1. **Validar protocolo completo**: si falta cualquier sección, abortar y listar qué falta.
2. **Leer protocolo** y mapear a campos PROSPERO 2024.
3. **Generar `protocolo/prospero-submission.md`** con esta estructura — un campo por sección, numerado, con el límite de caracteres y el texto generado:

```markdown
# PROSPERO submission — copia cada campo

> URL: https://www.crd.york.ac.uk/prospero/
> Cuenta requerida (gratis).
> Tiempo estimado: 30 min copy-paste.

## 1. Review title (limit: 200 char)
[título generado del protocolo]

## 2. Anticipated start date / Anticipated completion date
- Start: [fecha del protocolo]
- Completion: [fecha estimada]

## 3. Stage of review
- [ ] Pre-registration (recomendado, marca este si aún no inicias screening)
- [ ] Ongoing
- [ ] Completed

## 4. Named contact (autor responsable, email institucional)
[de protocolo]

## 5. Named contact address
[institución + dirección física]

## 6. Organisational affiliation
[universidad/hospital]

## 7. Review team members and their organisational affiliations
[de protocolo, lista con afiliación]

## 8. Funding sources/sponsors
[de protocolo o "None"]

## 9. Conflicts of interest
[de protocolo o "None declared"]

## 10. Collaborators
[opcional]

## 11. Review question(s) (limit: 1000 char)
[PICO formulado como pregunta]

## 12. Searches (limit: 1500 char)
[strings de busqueda con bases, fechas, limites de fecha]

## 13. URL to search strategy
[link al GitHub del proyecto donde está busqueda/strategy.md]

## 14. Condition or domain being studied (limit: 500 char)
[de protocolo P]

## 15. Participants/population (limit: 1500 char)
[de protocolo P + criterios inclusion/exclusion]

## 16. Intervention(s), exposure(s) (limit: 1500 char)
[de protocolo I]

## 17. Comparator(s)/control (limit: 1500 char)
[de protocolo C]

## 18. Types of study to be included (limit: 1000 char)
[lista de diseños aceptados, e.g. "RCT only"]

## 19. Context (limit: 1000 char)
[setting clínico, países, idiomas, fechas]

## 20. Main outcome(s) (limit: 1500 char)
[primario con definición, instrumento, momento de medición]

## 21. Additional outcome(s) (limit: 1500 char)
[secundarios]

## 22. Data extraction (limit: 1500 char)
[variables extraídas + quién extrae + verificación]

## 23. Risk of bias (quality) assessment (limit: 1500 char)
[ROB-2 o NOS + dominios]

## 24. Strategy for data synthesis (limit: 1500 char)
[meta random effects, heterogeneidad, modelo, software]

## 25. Analysis of subgroups or subsets (limit: 1500 char)
[subgrupos pre-especificados o "None planned"]

## 26. Type and method of review
- Marcar: [Systematic review with meta-analysis]

## 27. Language
- English / Spanish / etc.

## 28. Country
- [del autor]

## 29. Other registration details
- [si registraste también en OSF, ClinicalTrials.gov, etc.]

## 30. Reference and/or URL for published protocol
- [si tienes pre-print del protocolo]

## 31. Dissemination plans
- [publicación en revista, conferencia, etc.]

## 32. Keywords (5-7 separados por coma)
[de los términos PICO]
```

4. **Validaciones automáticas antes de devolver al usuario**:
   - Cada campo respeta su límite de caracteres
   - PICO completo
   - Outcomes pre-especificados (PROSPERO requiere outcomes ANTES de search)
   - Fechas coherentes

5. **Instrucciones finales al usuario**:
   - "Abre https://www.crd.york.ac.uk/prospero/"
   - "Crea cuenta o entra"
   - "New registration → Systematic review"
   - "Copia cada campo de prospero-submission.md al campo correspondiente"
   - "Submit → te dan un número de registro (CRD42024XXXXX)"
   - "Pega el número en `protocolo/protocolo.md` sección 'Pre-registro'"
   - "Commit con tag `[PRISMA-1] PROSPERO registered as CRD42024XXXXX`"

## Reglas

- **NUNCA inventar campos no presentes en el protocolo**. Si falta un dato, marcar "[FALTA EN PROTOCOLO]" y abortar antes de generar el output.
- **Respetar límites de caracteres**. Si el texto excede, comprimir manteniendo info esencial (no truncar a la mitad de frase).
- **PROSPERO rechaza** outcomes vagos como "improvement", "clinical response". Forzar definición operacional (instrumento + cutoff + momento).
- **Cambios post-registro** requieren amendment en PROSPERO + documentar en sección "Enmiendas al protocolo" del protocolo.md.

## Si falta algo

- Outcome primario sin definición operacional → preguntar al usuario, no inventar.
- Sin lista de revisores → preguntar (PROSPERO no acepta "TBD").
- Sin fechas → preguntar.
