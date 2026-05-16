# Changelog del workflow

> Versionado del workflow + skills. Sigue [semver](https://semver.org/lang/es/) (mayor.menor.parche).

## [1.0.0] — 2026-05-15

### Added
- Estructura monorepo: `_template/` + `projects/` + `docs/` + `scripts/`
- 9 skills en `.claude/skills/`:
  - Core: `/prisma-search`, `/screen-paper`, `/extract-data`, `/assess-rob`, `/run-metaanalysis`, `/prisma-flow`
  - Admin: `/prospero-register`, `/grade-evidence`, `/manuscript-prisma`
- `STATUS.md` como panel de control por proyecto
- `scripts/new-project.sh` para inicializar meta-análisis nuevos
- Integración con MCPs: biomcp (con NCBI API key), openalex, zotero, github, Scholar Gateway, Consensus, Context7
- Acceso directo al vault de Obsidian vía filesystem (`/mnt/c/Users/aless/Documents/Obsidian Vault/Metaanalisis/`)

### Methodology
- PRISMA 2020 (Page et al, BMJ 2021;372:n71)
- PRISMA-P 2015 para protocolos (Moher et al, Syst Rev 2015;4:1)
- GRADE para certeza de evidencia
- ROB-2 / Newcastle-Ottawa Scale para riesgo de sesgo
- Random effects (DerSimonian-Laird) por defecto

---

<!-- Plantilla:

## [X.Y.Z] — YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Removed
- ...

-->
