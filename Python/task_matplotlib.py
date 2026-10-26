import matplotlib.pyplot as plt

time = [0, 2, 4, 6, 8, 10]
expression = [5, 8, 12, 11, 17, 23]

plt.plot(time, expression, marker="o")
plt.xlabel("Время, ч")
plt.ylabel("Экспрессия гена")
plt.title("Изменение экспрессии гена")
plt.grid(True)
plt.savefig("expression_plot.png", dpi=150, bbox_inches="tight")
plt.show()
