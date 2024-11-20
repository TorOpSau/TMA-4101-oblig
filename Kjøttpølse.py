import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funksjon som beskriver Newtons avkjølingslov
def newton_cooling(t, alpha, T_ambient, T_initial):
    return T_ambient + (T_initial - T_ambient) * np.exp(-alpha * t)

# Input: Målte data
# Tidspunkter i sekunder (eller annen tidsenhet)
time_data = np.array([0, 10, 20, 30, 40, 50])  # Eksempel: erstatt med dine målinger
# Målte temperaturer
temp_data = np.array([90, 80, 72, 65, 60, 55])  # Eksempel: erstatt med dine målinger

# Omgivelsestemperatur (må defineres)
T_ambient = 20  # Eksempelverdi, juster etter dine data

# Initial temperatur
T_initial = temp_data[0]

# Tilpasning for å finne alfa
popt, pcov = curve_fit(lambda t, alpha: newton_cooling(t, alpha, T_ambient, T_initial), 
                       time_data, temp_data, p0=[0.01])

# Ekstraher alfa fra tilpasning
alpha = popt[0]
print(f"Estimert alfa: {alpha}")

# Beregn modelltemperaturer basert på den estimerte alfa
time_model = np.linspace(min(time_data), max(time_data), 100)
temp_model = newton_cooling(time_model, alpha, T_ambient, T_initial)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(time_data, temp_data, color='red', label='Måledata')
plt.plot(time_model, temp_model, label=f'Modell (alpha={alpha:.4f})')
plt.axhline(T_ambient, color='gray', linestyle='--', label='Omgivelsestemperatur')
plt.xlabel('Tid (s)')
plt.ylabel('Temperatur (°C)')
plt.title('Newtons avkjølingslov')
plt.legend()
plt.grid()
plt.show()
