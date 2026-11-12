import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

print("1. Cargando datos del paciente...")

record = wfdb.rdrecord('100', pn_dir='mitdb')
señal = record.p_signal[:, 0]
frecuencia_muestreo = record.fs

print("2. BUscando los latidos (Picos R)...")


distancia_minima = int(0.3 * frecuencia_muestreo)
picos, _= find_peaks(señal, distance=distancia_minima, height=0.5)

print("Se detectaron {len(picos)} latidos en esta señal")

intervalos = np.diff(picos) / frecuencia_muestreo
tiempo_promedio_latido = np.mean(intervalos)
bpm = 60 / tiempo_promedio_latido

print(f"Frecuencia cardiaca calculada: {bpm:.2f} BMP")
plt.figure(figsize=(12, 4))
plt.plot(señal[:2000], color='gray', label='Señal ECG')
plt.plot(picos[picos < 2000], señal[picos [picos < 2000]], "x", color='red', markersize=10, label='Latidos por minutos')

plt.title(f"Analisis de IA: {bpm:.0f} BPM")
plt.xlabel("Muestras")
plt.ylabel("Voltaje (mV)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
#Fin del codigo