import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv("gasolina.csv")
df_gasolina.head()

sns.set_palette(sns.color_palette("pastel"))
plt.figure(figsize = (15,8))
grafico = sns.barplot(x = "dia", y = "venda", data=df_gasolina)
grafico.set(title= "Fuel price per day", xlabel="Days", ylabel="Value of Sell")

grafico.figure.savefig("./graficoFuel.png")