import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec

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

mpl.style.use('seaborn')

fig, axs = plt.subplots(2, 2)


axs[0,0].plot(cercania_mineria_l, cercania_mineria_baja_l, 'b', linewidth=1.5, label='Cercano')
axs[0,0].plot(cercania_mineria_l, cercania_mineria_media_l, '-', linewidth=1.5, label='Intermedio')
axs[0,0].plot(cercania_mineria_l, cercania_mineria_alta_l, 'g', linewidth=1.5, label='Lejos')
axs[0,0].set_title('Cercania ala mineria legal')
axs[0,0].legend()

axs[0,1].plot(cercania_mineria_i, cercania_mineria_baja_i, 'b', linewidth=1.5, label='Cercano')
axs[0,1].plot(cercania_mineria_i, cercania_mineria_media_i, 'g', linewidth=1.5, label='Intermedio')
axs[0,1].plot(cercania_mineria_i, cercania_mineria_alta_i, 'r', linewidth=1.5, label='Lejos')
axs[0,1].set_title('Cercania a la mineria ilegal')
axs[0,1].legend()

axs[1,0].plot(calidad_agua, calidad_agua_bajo, 'b', linewidth=1.5, label='No tratable')
axs[1,0].plot(calidad_agua, calidad_agua_media, 'g', linewidth=1.5, label='Tratable')
axs[1,0].plot(calidad_agua, calidad_agua_alta, 'r', linewidth=1.5, label='Potable')
axs[1,0].set_title('Calidad de agua')
axs[1,0].legend()

axs[1,1].plot(PenfermedadesM, PenfermedadesM_baja, 'b', linewidth=1.5, label='Posibilidad Baja')
axs[1,1].plot(PenfermedadesM, PenfermedadesM_media, 'g', linewidth=1.5, label='Posibilidad Media')
axs[1,1].plot(PenfermedadesM, PenfermedadesM_alta, 'r', linewidth=1.5, label='Posibilidad Alta')
axs[1,1].set_title('Enfermedades')
axs[1,1].legend()




#cuando el agua tiene un grado de pertenencia de 6 y cercano es =5

cercania = 320
calidad = 3

cerca_ilegal = fuzz.interp_membership(cercania_mineria_i,cercania_mineria_baja_i, cercania)
media_ilegal = fuzz.interp_membership(cercania_mineria_i,cercania_mineria_media_i, cercania)
lejos_ilegal = fuzz.interp_membership(cercania_mineria_i,cercania_mineria_alta_i, cercania)

cerca_legal = fuzz.interp_membership(cercania_mineria_l,cercania_mineria_baja_l, cercania)
media_legal = fuzz.interp_membership(cercania_mineria_l,cercania_mineria_media_l, cercania)
lejos_legal = fuzz.interp_membership(cercania_mineria_l,cercania_mineria_alta_l, cercania)

no_tratable=fuzz.interp_membership(calidad_agua,calidad_agua_bajo,calidad)
tratable=fuzz.interp_membership(calidad_agua,calidad_agua_media,calidad)
potable=fuzz.interp_membership(calidad_agua,calidad_agua_alta,calidad)


# determinando enfermedad_baja 

# si la mineria es ilegal lejos o legal lejos y el agua es no tratable
regla1 = np.fmin(np.fmax(lejos_ilegal,lejos_legal),no_tratable)
salida1 = np.fmin(regla1,PenfermedadesM_baja)

# si la minera ilegal cerca o legal cerca y el agua es potable
regla2 = np.fmin(np.fmax(cerca_ilegal,cerca_legal),potable)
salida2 = np.fmin(regla2, PenfermedadesM_baja)

#si la mineria es cerca ilegal o cerca legal  y el agua es tratable
regla3 = np.fmin(np.fmax(cerca_ilegal,cerca_legal),tratable)
salida3= np.fmin(regla3, PenfermedadesM_baja)

#si la mineria es media legal o media ilegal y el agua es no tratable
regla4 = np.fmin(np.fmax(media_legal,media_ilegal),no_tratable)
salida4= np.fmin(regla4, PenfermedadesM_baja)

#si la mineria es cerca legal o lejos ilegaal y el agua es potable
regla5 = np.fmin(np.fmax(cerca_legal,lejos_ilegal),potable)
salida5= np.fmin(regla5, PenfermedadesM_baja)


salida_baja= np.fmax(salida1,
					np.fmax(salida2,
						np.fmax(salida3,
							np.fmax(salida4,salida5))))

#determinando enfermedad_media

#si la mineria es legal lejos y el agua es tratable
regla6 = np.fmax(lejos_ilegal,tratable)
salida6=np.fmax(regla6,PenfermedadesM_media)
#si la mineria es ilegal lejos y el agua es tratable
regla7 = np.fmax(lejos_ilegal,tratable)
salida7=np.fmax(regla6,PenfermedadesM_media)
#si la mineria es legal media y el agua es tratable
regla8 = np.fmax(media_legal,tratable)
salida8=np.fmax(regla6,PenfermedadesM_media)
#si la mineria es legal cerca y el agua es tratable
regla9 = np.fmax(media_legal,tratable)
salida9=np.fmax(regla6,PenfermedadesM_media)

salida_media= np.fmax(salida6,
					np.fmax(salida7,
						np.fmax(salida8,salida9)))

#determinando enfermedad_alta 

#si mineria es ilegal y cerca entonces la enfermedad es alta
salida10=np.fmin(cerca_ilegal,PenfermedadesM_alta)
#Si la mineria  ilegal cerca y hay mala calidad de agua la enfermedad es alta
regla11 = np.fmin(cerca_ilegal, no_tratable)
salida11=np.fmin(regla11,PenfermedadesM_alta)
#Si la mineria  ilegal cerca y hay mala calidad de agua la enfermedad es alta
regla12 = np.fmin(cerca_ilegal, no_tratable)
salida12=np.fmin(regla12,PenfermedadesM_alta)
#Si la mineria ilegar media y hay media calidad de agua
regla13 = np.fmin(media_ilegal, tratable)
salida13=np.fmin(regla13,PenfermedadesM_alta)
#Si la mineria legal cerca y mala calidad de agua
regla14 = np.fmin(cerca_legal,no_tratable)
salida14=np.fmin(regla14,PenfermedadesM_alta)


salida_alta= np.fmax(salida10,np.fmax(salida11,np.fmax(salida12,np.fmax(salida13,salida14))))

enfermedad_ejex=np.zeros_like(PenfermedadesM)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(PenfermedadesM, enfermedad_ejex, salida_baja, facecolor='b', alpha=0.2)
ax0.plot(PenfermedadesM, salida_baja, 'b', linewidth=2, linestyle='--', label='posibilidad_baja')
ax0.fill_between(PenfermedadesM, enfermedad_ejex, salida_media, facecolor='g', alpha=0.1)
ax0.plot(PenfermedadesM, salida_media, 'g', linewidth=2, linestyle='--',label='posibilidad_media')
ax0.fill_between(PenfermedadesM, enfermedad_ejex, salida_alta, facecolor='r', alpha=0.3)
ax0.plot(PenfermedadesM, salida_alta, 'r', linewidth=2, linestyle='--',label='posibilidad_alta')
ax0.set_title('Funciones de Salida')
ax0.legend()


# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()


##############desfuzificando
union_salidas=np.fmax(salida_baja,
                     np.fmax(salida_media,salida_alta ))
centroide = fuzz.defuzz(PenfermedadesM, union_salidas, 'centroid')
print("respuesta",centroide)
salida_centroide = fuzz.interp_membership(PenfermedadesM, union_salidas, centroide)  # for plot
print("correspondencia en la grafica",salida_centroide)
##############visualizacion de datos
fig3, ax5 = plt.subplots(figsize=(8, 3))

ax5.plot(PenfermedadesM, PenfermedadesM_baja, 'b', linewidth=2, linestyle='--', label='posibilidad_baja')
ax5.plot(PenfermedadesM, PenfermedadesM_media, 'g', linewidth=2, linestyle='--',label='posibilidad_media')
ax5.plot(PenfermedadesM, PenfermedadesM_alta, 'r', linewidth=2, linestyle='--',label='posibilidad_alta')
ax5.plot(PenfermedadesM, union_salidas, 'c', linewidth=2, linestyle='--',label='salida')
ax5.fill_between(PenfermedadesM, enfermedad_ejex, union_salidas, facecolor='Orange', alpha=0.3)
ax5.plot([centroide, centroide], [0, salida_centroide], 'k', linewidth=1.5, alpha=0.9)
ax5.legend()
plt.show()
