from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
plot_pacf(y, ax=ax)   # -----> line showing difference from acf plot <-----
plt.xlabel("Lag [hours]")
plt.ylabel("Correlation Coefficient")
plt.title("Partial Autocorrelation")

# Don't delete the code below 👇
plt.savefig("images/3-5-7.png", dpi=150)
