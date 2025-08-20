# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Generate synthetic data ---
np.random.seed(42)

n = 200
# Acquisition cost between $50 and $500
acquisition_cost = np.random.uniform(50, 500, n)
# Lifetime value, generally higher for lower cost but with randomness
lifetime_value = acquisition_cost * np.random.uniform(2, 6, n) + np.random.normal(0, 200, n)

data = pd.DataFrame({
    "Acquisition Cost ($)": acquisition_cost,
    "Lifetime Value ($)": lifetime_value
})

# --- 2. Styling ---
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# --- 3. Create scatterplot ---
plt.figure(figsize=(8,8))  # 8 in * 64 dpi = 512 px
sns.scatterplot(
    data=data,
    x="Acquisition Cost ($)",
    y="Lifetime Value ($)",
    hue="Acquisition Cost ($)",   # color gradient by acquisition cost
    palette="viridis",
    alpha=0.8,
    edgecolor="w",
    s=80
)

# --- 4. Titles & Labels ---
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight="bold")
plt.xlabel("Acquisition Cost ($)", fontsize=12)
plt.ylabel("Lifetime Value ($)", fontsize=12)
plt.legend(title="Acquisition Cost", loc="upper left", bbox_to_anchor=(1,1))

# --- 5. Save chart ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
