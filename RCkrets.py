import numpy as np
import matplotlib.pyplot as plt

# Konstantverdier
V_inn_maalt = 7.77  # Spenningen fra batteriet (volt)
R_maalt = 0.999*10**6  # Motstanden (ohm)
C = 100e-6  # Kapasiteten til kondensatoren (farad)
tau_maalt = R_maalt * C  # Tidskonstanten ved ideell tilpasning av måling

V_inn = 9  #Spenning fra ønsket batteri (volt)
R = 1*10**6 #Ønsket motstand (ohm)
tau = R * C # Tidskontanten ved ideel modell


# Tidsparametere
t_max = 60 # Maksimal tid (sekunder)
dt = 0.01  # Tidsskritt (sekunder)
t = np.arange(0, t_max + dt, dt)  # Tidsvektor

# Beregning av spenningen over kondensatoren (ideell tilpasning av RC-krets)
V_ideal_maalt = V_inn_maalt * (1 - np.exp(-t / tau_maalt))
# Beregning av spenningen over kondensatoren (ideell tilpasning av RC-krets)
V_ideal = V_inn * (1 - np.exp(-t / tau))

# Måledata
maalte_tider = np.arange(0,61)  # Tid i sekunder
maalte_spenninger = np.array([0, 98.7e-3, 143e-3, 0.209, 0.296, 0.358, 0.439, 0.5, 0.559, 0.637, 0.695, 0.753, 0.829, 0.885, 0.959, 1.014, 1.068, 1.095, 1.166, 1.219, 1.271, 1.340, 1.391, 1.442, 1.509, 1.558, 1.607, 1.671, 1.719, 1.767, 1.829, 1.875, 1.921, 1.982, 2.13, 2.08, 2.12, 2.16, 2.22, 2.26, 2.32, 2.36, 2.40, 2.44, 2.50, 2.54, 2.59, 2.62, 2.66, 2.72, 2.75, 2.79, 2.84, 2.88, 2.92, 2.96, 3.00, 3.03, 3.08, 3.11, 3.14])  # Spenning i volt


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, V_ideal_maalt, label="Ideell RC-krets med målte komponenter", color="blue", linewidth=2)
plt.plot(t, V_ideal, label="Ideell RC-krets", color="green", linewidth=2)
plt.plot(maalte_tider, maalte_spenninger, linestyle = '-', color="red", marker = "o", label="Målte verdier", zorder=5)

# Plotinnstillinger
plt.title("Spenning over kondensatoren i en RC-krets")
plt.xlabel("Tid (s)")
plt.ylabel("Spenning (V)")
plt.legend()
plt.grid(True)
plt.show()

diff_ideel_maalt = 0
diff_ideel = 0
for i in range(len(maalte_spenninger)):
    diff_ideel_maalt += abs(maalte_spenninger[i]-V_inn_maalt * (1 - np.exp(-i / tau_maalt)))
    diff_ideel += abs(maalte_spenninger[i]-V_inn * (1 - np.exp(-i / tau)))

diff_ideel_maalt = diff_ideel_maalt/len(maalte_spenninger)
diff_ideel = diff_ideel/len(maalte_spenninger)
print(diff_ideel_maalt)
print(diff_ideel)
