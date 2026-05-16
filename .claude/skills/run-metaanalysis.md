---
name: run-metaanalysis
description: Ejecuta el meta-análisis con Python sobre extraction.csv. Modelo de efectos aleatorios por default, calcula heterogeneidad, genera forest plot, funnel plot, análisis de sensibilidad leave-one-out. Versiona scripts y outputs.
---

# Skill: Run Meta-analysis

## Inputs

- `extraccion/extraction.csv` con al menos 3 estudios para el outcome
- Outcome a analizar (nombre exacto del CSV)
- Tipo de efecto (OR, RR, HR, MD, SMD)

## Workflow

1. **Verificar pre-requisitos**:
   - Al menos 3 estudios con datos completos
   - Variables suficientes según effect_type:
     - Binario (OR/RR): events + n por grupo
     - Continuo (MD/SMD): mean + SD + n por grupo
     - HR: log(HR) + SE
2. **Generar script `analisis/stats.py`** versionado (git):

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.meta_analysis import combine_effects

# 1. Cargar
df = pd.read_csv('extraccion/extraction.csv')
outcome_df = df[df['outcome'] == 'OUTCOME_NAME'].copy()

# 2. Calcular log(OR) y SE para binarios
# Para OR: log(OR) = log((a/b)/(c/d)); SE = sqrt(1/a + 1/b + 1/c + 1/d)
outcome_df['log_effect'] = np.log(outcome_df['effect'])
outcome_df['se'] = (np.log(outcome_df['ci_high']) - np.log(outcome_df['ci_low'])) / (2 * 1.96)

# 3. Meta random effects (DerSimonian-Laird via statsmodels)
res = combine_effects(
    outcome_df['log_effect'].values,
    outcome_df['se'].values**2,
    method_re='dl'
)
print(res.summary_frame())

# 4. Heterogeneidad: I², Q, τ²
print(f"I² = {res.i2:.1%}")
print(f"Q (p) = {res.q:.2f} ({res.q_p:.3f})")
print(f"τ² = {res.tau2:.4f}")

# 5. Forest plot (matplotlib)
fig, ax = plt.subplots(figsize=(10, 6))
y = np.arange(len(outcome_df))[::-1]
ax.errorbar(outcome_df['effect'], y, 
            xerr=[outcome_df['effect']-outcome_df['ci_low'], 
                  outcome_df['ci_high']-outcome_df['effect']],
            fmt='s', markersize=8)
ax.axvline(1, color='gray', linestyle='--')
ax.set_yticks(y)
ax.set_yticklabels(outcome_df['first_author'] + ' (' + outcome_df['year'].astype(str) + ')')
ax.set_xlabel('Effect size (OR)')
ax.set_xscale('log')
plt.tight_layout()
plt.savefig('analisis/forest-plot.png', dpi=300, bbox_inches='tight')

# 6. Funnel plot (si k >= 10)
if len(outcome_df) >= 10:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(outcome_df['log_effect'], outcome_df['se'])
    ax.invert_yaxis()
    ax.set_xlabel('log(Effect)')
    ax.set_ylabel('SE')
    plt.tight_layout()
    plt.savefig('analisis/funnel-plot.png', dpi=300)

# 7. Sensitivity: leave-one-out
# (loop excluyendo un estudio cada vez, reportar pooled effect)
```

3. **Ejecutar y guardar outputs**:
   - `analisis/forest-plot.png`
   - `analisis/funnel-plot.png` (si k ≥ 10)
   - `analisis/sensibilidad.md` con resultados leave-one-out

4. **Interpretar**:
   - I² < 25%: baja heterogeneidad
   - I² 25-50%: moderada
   - I² 50-75%: sustancial
   - I² > 75%: considerable (justifica investigar subgrupos)
   - Test de Egger p < 0.10 sugiere asimetría → considerar sesgo de publicación

5. **Reportar en formato PRISMA**:
   - Pooled effect (95% CI)
   - k estudios, n total
   - I², τ², Q p-value
   - Modelo usado (random/fixed)
   - Subgrupos pre-especificados
   - Sensibilidad

## Reglas

- **Random effects por defecto** (asumir heterogeneidad metodológica/clínica).
- **Reportar fixed effects como secundario**, no como principal a menos que I² ≈ 0.
- **Si I² > 50%, investigar antes de combinar**: subgrupos, meta-regresión, exclusión justificada.
- **Nunca p-hacking**: outcomes pre-especificados en protocolo, no cambiar después de ver datos.

## Output

- Script versionado en `analisis/stats.py`
- Plots en `analisis/*.png`
- Resumen en `analisis/results-<outcome>.md`
- Commit a GitHub con tag `[PRISMA-7]`
