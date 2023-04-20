import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\ingresos.csv")

sns.lineplot(x="fecha", y="ingresos", data=df)

plt.plot("01-09", 1000, "o")

plt.show()
