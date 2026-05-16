"""Plantilla de análisis estadístico - meta-análisis.

Reemplazar OUTCOME_NAME por el outcome a analizar.
Ejecutar: python analisis/stats.py
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.meta_analysis import combine_effects

OUTCOME_NAME = "PRIMARY_OUTCOME"  # cambiar
EFFECT_TYPE = "OR"  # OR, RR, HR, MD, SMD

df = pd.read_csv("extraccion/extraction.csv")
sub = df[df["outcome"] == OUTCOME_NAME].copy()

if len(sub) < 3:
    raise SystemExit(f"Solo {len(sub)} estudios para {OUTCOME_NAME}; meta no recomendable")

if EFFECT_TYPE in ("OR", "RR", "HR"):
    sub["log_effect"] = np.log(sub["effect"])
    sub["se"] = (np.log(sub["ci_high"]) - np.log(sub["ci_low"])) / (2 * 1.96)
    effect_log = True
else:
    sub["log_effect"] = sub["effect"]
    sub["se"] = (sub["ci_high"] - sub["ci_low"]) / (2 * 1.96)
    effect_log = False

res = combine_effects(
    sub["log_effect"].values,
    sub["se"].values ** 2,
    method_re="dl",
)
print(res.summary_frame(alpha=0.05))
print(f"I^2 = {res.i2:.1%}")
print(f"Q (p) = {res.q:.2f} ({res.q_p:.3f})")
print(f"tau^2 = {res.tau2:.4f}")

fig, ax = plt.subplots(figsize=(10, max(4, 0.5 * len(sub) + 2)))
y = np.arange(len(sub))[::-1]
ax.errorbar(
    sub["effect"], y,
    xerr=[sub["effect"] - sub["ci_low"], sub["ci_high"] - sub["effect"]],
    fmt="s", markersize=8,
)
null = 1 if effect_log else 0
ax.axvline(null, color="gray", linestyle="--")
ax.set_yticks(y)
ax.set_yticklabels(sub["first_author"] + " (" + sub["year"].astype(str) + ")")
ax.set_xlabel(f"{EFFECT_TYPE}")
if effect_log:
    ax.set_xscale("log")
ax.set_title(f"Forest plot: {OUTCOME_NAME}")
plt.tight_layout()
plt.savefig(f"analisis/forest-{OUTCOME_NAME}.png", dpi=300)
print(f"Saved: analisis/forest-{OUTCOME_NAME}.png")

if len(sub) >= 10:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(sub["log_effect"], sub["se"])
    ax.invert_yaxis()
    ax.set_xlabel("log(Effect)" if effect_log else "Effect")
    ax.set_ylabel("SE")
    ax.set_title(f"Funnel plot: {OUTCOME_NAME}")
    plt.tight_layout()
    plt.savefig(f"analisis/funnel-{OUTCOME_NAME}.png", dpi=300)
    print(f"Saved: analisis/funnel-{OUTCOME_NAME}.png")
