import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datele experimentale (fără ultraviolet, care este o anomalie evidentă)
lungimi_unda_nm = np.array([578, 546, 436, 405])
tensiuni = np.array([0.730, 0.857, 1.259, 1.343])

c = 3e8      # Viteza luminii (m/s)
e = 1.6e-19  # Sarcina elementară (C)

# Calculul frecvențelor
frecvente = c / (lungimi_unda_nm * 1e-9)

# Regresia liniară
panta, intercept, _, _, _ = linregress(frecvente, tensiuni)

h_exp = panta * e # constanta lui Planck
L_extr_eV = -intercept

print(f"Constanta lui Planck (h): {h_exp:.4e} J*s")
print(f"Lucrul mecanic de extracție (L_extr): {L_extr_eV:.2f} eV")

plt.scatter(frecvente, tensiuni, color='blue')
plt.plot(frecvente, panta * frecvente + intercept, color='red', linestyle='--')
plt.xlabel('Frecvența (Hz)')
plt.ylabel('Tensiunea de stopare (V)')
plt.grid(True)
plt.savefig('../data/grafic.png')
plt.show()