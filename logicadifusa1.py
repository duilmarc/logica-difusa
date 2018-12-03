import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

cercania_mineria_l = np.arange(0,2000,10)
cercania_mineria_i = np.arange(0,2000,10) # kilometros
calidad_agua = np.arange(0,11, 1)#calidad de agua
PenfermedadesM  = np.arange(0,11,1)


cercania_mineria_baja_l = fuzz.zmf(cercania_mineria_l, 300, 750)#gamma_lineal(cercania_mineria_l, [1000, 2000])#fuzz.trimf(cercania_mineria_l, [0, 1000, 2000])
cercania_mineria_media_l = fuzz.trapmf(cercania_mineria_l, [400,700,1300,1500])
cercania_mineria_alta_l = fuzz.smf(cercania_mineria_l, 700, 2000)

cercania_mineria_baja_i = fuzz.zmf(cercania_mineria_i, 300, 750)#gamma_lineal(cercania_mineria_i, [1000, 2000])#fuzz.trimf(cercania_mineria_i, [0, 1000, 2000])
cercania_mineria_media_i= fuzz.trapmf(cercania_mineria_i, [400,700,1300,1500])
cercania_mineria_alta_i = fuzz.smf(cercania_mineria_i, 700, 2000)

calidad_agua_bajo = fuzz.zmf(calidad_agua,1,4) 
calidad_agua_media = fuzz.trapmf(calidad_agua,[2,4,6,8])
calidad_agua_alta = fuzz.smf(calidad_agua,5,10)

PenfermedadesM_baja = fuzz.zmf(PenfermedadesM, 4, 10)
PenfermedadesM_media = fuzz.trapmf(PenfermedadesM,[2,4,6,8 ])
PenfermedadesM_alta = fuzz.smf(PenfermedadesM, 4,10)

fig, (ax0, ax1, ax2,ax3) = plt.subplots(nrows=4, figsize=(8, 9))

fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)
f2_ax1 = fig2.add_subplot(spec2[0, 0])
f2_ax2 = fig2.add_subplot(spec2[0, 1])
f2_ax3 = fig2.add_subplot(spec2[1, 0])
f2_ax4 = fig2.add_subplot(spec2[1, 1])

ax0.plot(cercania_mineria_l, cercania_mineria_baja_l, 'b', linewidth=1.5, label='Cercano')
ax0.plot(cercania_mineria_l, cercania_mineria_media_l, 'g', linewidth=1.5, label='Intermedio')
ax0.plot(cercania_mineria_l, cercania_mineria_alta_l, 'r', linewidth=1.5, label='Lejos')
ax0.set_title('Cercania a la mineria legal')
ax0.legend()

ax3.plot(cercania_mineria_i, cercania_mineria_baja_i, 'b', linewidth=1.5, label='Cercano')
ax3.plot(cercania_mineria_i, cercania_mineria_media_i, 'g', linewidth=1.5, label='Intermedio')
ax3.plot(cercania_mineria_i, cercania_mineria_alta_i, 'r', linewidth=1.5, label='Lejos')
ax3.set_title('Cercania a la mineria ilegal')
ax3.legend()

ax1.plot(calidad_agua, calidad_agua_bajo, 'b', linewidth=1.5, label='No tratable')
ax1.plot(calidad_agua, calidad_agua_media, 'g', linewidth=1.5, label='Tratable')
ax1.plot(calidad_agua, calidad_agua_alta, 'r', linewidth=1.5, label='Potable')
ax1.set_title('Calidad de agua')
ax1.legend()

ax2.plot(PenfermedadesM, PenfermedadesM_baja, 'b', linewidth=1.5, label='Posibilidad Baja')
ax2.plot(PenfermedadesM, PenfermedadesM_media, 'g', linewidth=1.5, label='Posibilidad Media')
ax2.plot(PenfermedadesM, PenfermedadesM_alta, 'r', linewidth=1.5, label='Posibilidad Alta')
ax2.set_title('Enfermedades')
ax2.legend()


for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()


#cuando el agua tiene un grado de pertenencia de 6 y cercano es =5
cercania= input('Ingresa la cercania a la mineria')
calidad= input('Ingree la calidad de agua de su distrito')

cercania = 1500
calidad = 5

