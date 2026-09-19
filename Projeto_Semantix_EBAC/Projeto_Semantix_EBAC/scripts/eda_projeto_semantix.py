from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "base_capitais_educacao_2023.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["delta_ideb"] = df["ideb_2023"] - df["ideb_2021"]

# Estatística descritiva
print(df[["ideb_2021","ideb_2023","ioeb_2021","ioeb_2023","delta_ideb","delta_ioeb"]].describe())

# Correlação descritiva
print("\nCorrelação IOEB 2023 x IDEB 2023:")
print(df[["ioeb_2023","ideb_2023"]].corr())

# K-Means exploratório
base = df.dropna(subset=["ideb_2021","ideb_2023"]).copy()
X = StandardScaler().fit_transform(base[["ideb_2023","delta_ideb"]])

scores = {}
for k in [2,3,4]:
    model = KMeans(n_clusters=k, random_state=42, n_init=20)
    labels = model.fit_predict(X)
    scores[k] = silhouette_score(X, labels)

best_k = max(scores, key=scores.get)
print("\nSilhouette:", scores)
print("K escolhido:", best_k)

model = KMeans(n_clusters=best_k, random_state=42, n_init=20)
base["cluster"] = model.fit_predict(X)

# Gráfico
ax = base.plot.scatter(x="ideb_2023", y="delta_ideb", figsize=(10,6))
for _, row in base.iterrows():
    ax.annotate(row["capital"], (row["ideb_2023"], row["delta_ideb"]),
                fontsize=8, xytext=(3,3), textcoords="offset points")
ax.axhline(0, linewidth=1)
ax.set_title("Segmentação exploratória das capitais")
ax.set_xlabel("IDEB 2023")
ax.set_ylabel("Variação do IDEB (2023-2021)")
plt.tight_layout()
plt.savefig(OUT / "cluster_reproduzido.png", dpi=180)
plt.show()
